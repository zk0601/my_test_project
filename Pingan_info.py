# coding=utf-8
import requests
import json
import re
import os
import csv
import time
from Pingan_code import code_dict


statistic_file = os.path.join(os.path.dirname(__file__), "statistic.csv")
item_file = os.path.join(os.path.dirname(__file__), "detail.csv")


class PingAn(object):
    def __init__(self):
        self.url_prefix = 'https://life.pingan.com/life/sales/queryAgentsInfo.do?'

    def statistic(self, provincecode, provincename, city_dict):
        total = 0
        for name, code in city_dict.items():
            url = self.url_prefix + 'provinceCode=%s&cityCode=%s&regionCode=&sex=&age=&pageSize=6&pageNo=1&jsoncallback=success_jsoncallback' % (provincecode, code)
            ret = requests.get(url)
            content = str(ret.content.decode('gb18030'))
            pattern = r"success_jsoncallback\((.*)\)"
            content = re.match(pattern, content).group(1)
            content = json.loads(content)
            total += content["pageBean"]["totalResults"]
            with open(statistic_file, 'a', encoding='utf-8-sig') as ff:
                writer = csv.writer(ff)
                writer.writerow([provincename, name, content["pageBean"]["totalResults"]])
        with open(statistic_file, 'a', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow([provincename, "total", total])

    def iteminfo(self, provincecode, provincename, citycode, cityname):
        url = self.url_prefix + 'provinceCode=%s&cityCode=%s&regionCode=&sex=&age=&pageSize=6&pageNo=1&jsoncallback=success_jsoncallback' % (provincecode, citycode)
        ret = requests.get(url)
        content = str(ret.content.decode('gb18030'))
        pattern = r"success_jsoncallback\((.*)\)"
        content = re.match(pattern, content).group(1)
        content = json.loads(content)
        total_page = content["pageBean"]["totalPageSize"]
        page = 1
        while page <= total_page+1:
            try:
                url = self.url_prefix + 'provinceCode=%s&cityCode=%s&regionCode=&sex=&age=&pageSize=6&pageNo=%s&jsoncallback=success_jsoncallback' % \
                      (provincecode, citycode, page)
                ret = requests.get(url)
                content = str(ret.content.decode('gb18030'))
                pattern = r"success_jsoncallback\((.*)\)"
                content = re.match(pattern, content).group(1)
                content = json.loads(content)
                userlist = content["resultList"]
                for user in userlist:
                    district = user['DESCRIPTION']
                    name = user['NAME']
                    introduction = '暂无'
                    if 'SELFINTRODUCE' in user:
                        introduction = user['SELFINTRODUCE']
                    home = user['HOMEADDR']
                    with open(item_file, 'a', encoding='utf-8-sig') as f:
                        info = [provincename, cityname, district, name, introduction, home]
                        writer = csv.writer(f)
                        writer.writerow(info)
                page += 1
            except Exception as e:
                print(e)
                time.sleep(20)
                continue


if __name__ == '__main__':
    a = PingAn()
    # a.statistic(1, "北京", {"北京": 1})
    # a.iteminfo(76, "北京", 173, "北京")
    for province, item in code_dict.items():
        a.statistic(item['code'], province, item['city'])
        print("finish statistic of %s" % province)
        for city, code in item['city'].items():
            a.iteminfo(item['code'], province, code, city)
            print("finish detail of %s" % city)
            time.sleep(5)
