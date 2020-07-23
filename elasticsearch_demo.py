# -*- coding: utf-8 -*-
from decimal import DivisionByZero

import elasticsearch
import logging
from elasticsearch_dsl import DocType, Integer, Text, Keyword
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl.field import Date, String, Float

from django.conf import settings

from dataRepository.models import UniteCommunity, UniteCommAlias

connections.create_connection(hosts=settings.ELASTICS['default']['HOSTS'])

logger = logging.getLogger(__name__)


class ElasticCommunity(DocType):
    """
    标准小区
    """
    id = Integer()
    state = Integer()
    city_id = Integer()
    district_id = Integer()
    area_id = Integer()
    address = Text(analyzer='snowball')
    ershou_count = Integer()
    rent_count = Integer()
    longitude = Float()
    latitude = Float()
    origin_id = Integer()
    pinyin = Text(analyzer='snowball')
    pinyin_initial = Text(analyzer='snowball')
    name = Text(analyzer='snowball')

    comm_alias_origin_id = Text(analyzer='snowball')
    comm_alias = Text(analyzer='snowball')
    name_search = Text(analyzer='snowball')

    class Meta:
        index = settings.ELASTICS['default']['INDEX']

    def save(self, **kwargs):
        try:
            rs = super(ElasticCommunity, self).save(**kwargs)
        except:
            logger.error('保存ElasticCommunity报错', exc_info=1)
            rs = False
        return rs

    def save_comm(self, comm_id):
        comm = UniteCommunity.objects.filter(id=comm_id).first()
        if not comm:
            logger.error('没有对应的小区：{}'.format(comm_id))
            return False

        comm_alias = UniteCommAlias.objects.filter(unite_comm_id=comm_id).all()
        alias, alias_origin_id = "", ""
        for item in comm_alias:
            alias_origin_id = alias_origin_id + str(item.origin_id) + ' '
            alias = alias + item.comm_alias + ' '

        self.meta.id = comm_id
        self.id = comm_id
        self.state = comm.state
        self.city_id = comm.city_id
        self.district_id = comm.district_id
        self.area_id = comm.area_id
        self.name = comm.name
        self.pinyin = comm.pinyin
        self.pinyin_initial = comm.pinyin_initial
        self.address = comm.address
        self.ershou_count = comm.ershou_count
        self.rent_count = comm.rent_count
        self.origin_id = comm.origin_id
        self.longitude = comm.longitude
        self.latitude = comm.latitude

        self.comm_alias_origin_id = alias_origin_id.strip()
        self.comm_alias = alias.strip()
        self.name_search = self.name + ' ' + self.comm_alias
        rs = self.save()
        return rs


try:
    ElasticCommunity.init()
except:
    try:
        ElasticCommunity._doc_type.refresh()
    except elasticsearch.exceptions.ConnectionError:
        logger.error('elastic service Connection error')


def comm_search(request):
    """
    查询小区列表
    """
    page = int(request.GET.get('page', 1))
    if page < 1:
        return JSONResponse(error=consts.ERROR['PARA_ERR'])
    page -= 1
    page_size = int(request.GET.get('page_size', 10))
    city_id = int(request.GET.get('city_id', 0))
    if not city_id:
        return JSONResponse(error=consts.ERROR['PARA_ERR'])
    key = request.GET.get('key', '')

    data = {}
    communities = ElasticCommunity().search().filter('term', state=0)

    if city_id > 0:
        communities = communities.filter('term', city_id=city_id)

    if key:
        match_phrase = {
            "bool": {
                "should": [
                    {"match_phrase": {"name_search": key}},
                    {"wildcard": {"pinyin": key + "*"}},
                    {"wildcard": {"pinyin_initial": key + "*"}}
                ]
            }
        }
        communities = communities.query(match_phrase)

    communities = communities.sort('-ershou_count')[page * page_size:page * page_size + page_size].execute()
    if communities:
        communities = communities['hits']['hits']

        comm_ids = [comm['_source']['id'] for comm in communities]
        comm_info_list = UniteCommInfo.objects.filter(comm_id__in=comm_ids).all()
        comm_info_dict = {comm_info.comm_id: comm_info for comm_info in comm_info_list}

        comm_list = []
        for community in communities:
            comm_id = community['_source']['id']
            comm_info_db = comm_info_dict.get(comm_id)
            if not comm_info_db:
                logger.error('小区info不存在，comm_id: %s' % comm_id)
                continue
            comm = {
                'id': comm_id,
                'name': community['_source']['name'],
                'count': community['_source']['ershou_count'],
                'rent_count': community['_source']['rent_count'],
                'location': community['_source']['address'],
                'build_year': comm_info_db.build_year,
            }
            comm_list.append(comm)

        data['payload'] = comm_list
    else:
        data['payload'] = []

    return JSONResponse(data=data)