# -*- coding: utf-8 -*-
import logging
import datetime
import os
import xlwt
from copy import copy

from django.core.mail import EmailMultiAlternatives
from django.core.management import BaseCommand
from django.db.models import Q

from dataRepository.models import *

logger = logging.getLogger(__name__)

"""
执行方式
配置环境变量
export PYTHONPATH=/Users/yeju/Documents/work/eju/dataRepository
export DJANGO_SETTINGS_MODULE=projects.dataRepository.settings
python projects/dataRepository/manage.py data_report_everyweek
"""

G_RECIPIENT_LIST = [
    'zhoukun@ehousechina.com',
    'yeju@ehousechina.com'
]

city_list = ['上海', '宁波', '西安', '郑州', '沈阳', '杭州', '天津', '重庆', '武汉', '南京', '无锡', '苏州', '合肥', '青岛', '成都', '北京']
origin_list = ['链家', '贝壳', '安居客', '58同城']
comm_unite_goal = {'上海': 19328, '宁波': 3153, '西安': 5420, '郑州': 5774, '沈阳': 3567, '杭州': 6510, '天津': 7067,
                   '重庆': 9696, '武汉': 6532, '南京': 5999, '无锡': 3821, '苏州': 5486, '合肥': 2987, '青岛': 4321, '成都': 12751, '北京': 11801}
comm_lj_goal = {'上海': 31482, '宁波': 2747, '西安': '无法获取', '郑州': 6190, '沈阳': 3296, '杭州': 6002, '天津': 7175,
                '重庆': 8621, '武汉': 0, '南京': 0, '无锡': 0, '苏州': 0, '合肥': 0, '青岛': 0, '成都': 0, '北京': 0}
comm_bk_goal = {'上海': 31430, '宁波': 2733, '西安': 5627, '郑州': 6183, '沈阳': 3290, '杭州': 5975, '天津': 7161,
                '重庆': 8604, '武汉': 7743, '南京': 5842, '无锡': 3413, '苏州': 5891, '合肥': '-', '青岛': '-', '成都': '-', '北京': '-'}
comm_ajk_goal = {'上海': 36234, '宁波': 3916, '西安': 5961, '郑州': 6147, '沈阳': 4398, '杭州': 11163, '天津': 12295,
                 '重庆': 10249, '武汉': 6189, '南京': 8351, '无锡': 3662, '苏州': 5824, '合肥': '-', '青岛': '-', '成都': '-', '北京': '-'}
comm_58_goal = {'上海': '无法获取', '宁波': '无法获取', '西安': '无法获取', '郑州': '无法获取', '沈阳': '无法获取', '杭州': '无法获取', '天津': '无法获取',
                '重庆': '无法获取', '武汉': '无法获取', '南京': '无法获取', '无锡': '无法获取', '苏州': '无法获取', '合肥': '无法获取', '青岛': '无法获取',
                '成都': '无法获取', '北京': '无法获取'}

lj_ershou_goal = {'上海': 75534, '宁波': '-', '西安': '-', '郑州': '-', '沈阳': '-', '杭州': '-', '天津': '-',
                  '重庆': '-', '武汉': '-', '南京': '-', '无锡': '-', '苏州': '-', '合肥': '-', '青岛': '-', '成都': '-', '北京': '-'}
lj_rent_goal = {'上海': 21184, '宁波': '-', '西安': '-', '郑州': '-', '沈阳': '-', '杭州': '-', '天津': '-',
                '重庆': '-', '武汉': '-', '南京': '-', '无锡': '-', '苏州': '-', '合肥': '-', '青岛': '-', '成都': '-', '北京': '-'}
bk_ershou_goal = {'上海': 75442, '宁波': 13372, '西安': 44364, '郑州': 63925, '沈阳': 51789, '杭州': 32113, '天津': 78898,
                  '重庆': 84599, '武汉': 98968, '南京': 61201, '无锡': 19922, '苏州': 31518, '合肥': '-', '青岛': '-', '成都': '-', '北京': '-'}
bk_rent_goal = {'上海': 57737, '宁波': 10869, '西安': 37969, '郑州': 60414, '沈阳': 20570, '杭州': 52548, '天津': 20039,
                '重庆': 30840, '武汉': 85766, '南京': 54054, '无锡': 9213, '苏州': 9374, '合肥': '-', '青岛': '-', '成都': '-', '北京': '-'}
ajk_ershou_goal = {'上海': '无法获取', '宁波': '无法获取', '西安': '无法获取', '郑州': '无法获取', '沈阳': '无法获取', '杭州': '无法获取', '天津': '无法获取',
                   '重庆': '无法获取', '武汉': '无法获取', '南京': '无法获取', '无锡': '无法获取', '苏州': '无法获取', '合肥': '无法获取', '青岛': '无法获取',
                   '成都': '无法获取', '北京': '无法获取'}
ajk_rent_goal = {'上海': '无法获取', '宁波': '无法获取', '西安': '无法获取', '郑州': '无法获取', '沈阳': '无法获取', '杭州': '无法获取', '天津': '无法获取',
                 '重庆': '无法获取', '武汉': '无法获取', '南京': '无法获取', '无锡': '无法获取', '苏州': '无法获取', '合肥': '无法获取', '青岛': '无法获取',
                 '成都': '无法获取', '北京': '无法获取'}
five8_ershou_goal = {'上海': '无法获取', '宁波': '无法获取', '西安': '无法获取', '郑州': '无法获取', '沈阳': '无法获取', '杭州': '无法获取', '天津': '无法获取',
                     '重庆': '无法获取', '武汉': '无法获取', '南京': '无法获取', '无锡': '无法获取', '苏州': '无法获取', '合肥': '无法获取', '青岛': '无法获取',
                     '成都': '无法获取', '北京': '无法获取'}
five8_rent_goal = {'上海': '无法获取', '宁波': '无法获取', '西安': '无法获取', '郑州': '无法获取', '沈阳': '无法获取', '杭州': '无法获取', '天津': '无法获取',
                   '重庆': '无法获取', '武汉': '无法获取', '南京': '无法获取', '无锡': '无法获取', '苏州': '无法获取', '合肥': '无法获取', '青岛': '无法获取',
                   '成都': '无法获取', '北京': '无法获取'}


class Command(BaseCommand):
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    file_name = '楼盘字典数据%s.xls' % today
    report_path = os.path.join('.', file_name)
    blue_style = None
    grey_style = None
    green_style = None
    orange_style = None

    def __init__(self, *args, **kwargs):
        super(Command).__init__(*args, **kwargs)
        self.city_list = city_list
        self.init_style()
        now = datetime.datetime.now()
        now = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second, microseconds=now.microsecond)
        self.date_range = [datetime.datetime.now() - datetime.timedelta(days=7), now]

    def add_arguments(self, parser):
        parser.add_argument('-e', '--email', action='store', dest='email', type=str, required=False, help=u'email地址，多个使用英文逗号分隔')

    def handle(self, *args, **options):
        email_list = options['email']
        if email_list:
            G_RECIPIENT_LIST.extend(email_list.split(','))
        logger.info('email_list: %s' % G_RECIPIENT_LIST)
        self.make_report()
        self.send_email()

    def send_email(self):
        logger.info('开始发送邮件')
        html = """
        <!DOCTYPE html>
           <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>楼盘字典统计报表</title>
            </head>
            <body>
            </body
        </html>"""
        from_mail = 'cyjz@ehousechina.com'
        subject = '【楼盘字典数据报表】楼盘字典数据%s' % datetime.datetime.now().strftime('%Y%m%d')
        msg = EmailMultiAlternatives(
            subject,
            html,
            from_mail,
            G_RECIPIENT_LIST,
            headers={'From': '简单家<cyjz@ehousechina.com>'}
        )
        msg.attach_file(self.report_path)
        msg.content_subtype = 'html'
        msg.encoding = 'utf-8'
        msg.send()
        logger.info('邮件发送结束')

    def init_style(self):
        # 对齐方式,中horz代表水平对齐方式，vert代表垂直对齐方式
        al = xlwt.Alignment()
        al.horz = xlwt.Alignment.HORZ_CENTER
        al.vert = xlwt.Alignment.VERT_CENTER

        # 单元格边框设置
        borders = xlwt.Borders()
        borders_level = xlwt.Borders.THIN
        borders.left = borders_level
        borders.right = borders_level
        borders.top = borders_level
        borders.bottom = borders_level

        # 字体设置
        font = xlwt.Font()
        font.name = u'宋体'
        font.colour_index = 0
        blue_font = copy(font)
        blue_font.height = 460   # 单元格大小
        blue_font.bold = True
        grey_font = copy(font)
        grey_font.height = 300
        grey_font.bold = True
        other_font = copy(font)
        other_font.height = 220
        other_font.bold = False

        # 背景颜色设置
        pattern = xlwt.Pattern()
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        blue_pattern = copy(pattern)
        blue_pattern.pattern_fore_colour = 31
        grey_pattern = copy(pattern)
        grey_pattern.pattern_fore_colour = 67
        green_pattern = copy(pattern)
        green_pattern.pattern_fore_colour = 57
        orange_pattern = copy(pattern)
        orange_pattern.pattern_fore_colour = 51

        style = xlwt.XFStyle()
        style.alignment = al
        style.borders = borders
        blue_style = copy(style)
        blue_style.font = blue_font
        blue_style.pattern = blue_pattern
        grey_style = copy(style)
        grey_style.font = grey_font
        grey_style.pattern = grey_pattern
        green_style = copy(style)
        green_style.font = other_font
        green_style.pattern = green_pattern
        orange_style = copy(style)
        orange_style.font = other_font
        orange_style.pattern = orange_pattern
        self.blue_style = blue_style
        self.grey_style = grey_style
        self.green_style = green_style
        self.orange_style = orange_style

    def make_report(self):
        workbook = xlwt.Workbook(encoding='utf8')
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        worksheet = workbook.add_sheet(today)

        # 调整列宽
        first_col = worksheet.col(0)
        first_col.width = 256 * 20

        # 构造模板
        worksheet.write_merge(0, 0, 0, 3, '城市', self.blue_style)
        for index, city in enumerate(self.city_list):
            worksheet.write(0, 4+index, city, self.grey_style)
        worksheet.write_merge(1, 17, 0, 0, '小区', self.blue_style)
        worksheet.write_merge(18, 41, 0, 0, '房源', self.blue_style)
        worksheet.write_merge(1, 3, 1, 2, '标准', self.grey_style)
        worksheet.write_merge(4, 6, 1, 2, '链家', self.grey_style)
        worksheet.write_merge(7, 10, 1, 2, '贝壳', self.grey_style)
        worksheet.write_merge(11, 14, 1, 2, '安居客', self.grey_style)
        worksheet.write_merge(15, 17, 1, 2, '58同城', self.grey_style)
        worksheet.write(1, 3, '目标', self.orange_style)
        worksheet.write(2, 3, '已入库', self.orange_style)
        worksheet.write(3, 3, '周新增', self.orange_style)
        worksheet.write(4, 3, '目标', self.green_style)
        worksheet.write(5, 3, '已入库', self.green_style)
        worksheet.write(6, 3, '周新增', self.green_style)
        worksheet.write(7, 3, '目标', self.orange_style)
        worksheet.write(8, 3, '源数据', self.orange_style)
        worksheet.write(9, 3, '已入库', self.orange_style)
        worksheet.write(10, 3, '周新增', self.orange_style)
        worksheet.write(11, 3, '目标', self.green_style)
        worksheet.write(12, 3, '源数据', self.green_style)
        worksheet.write(13, 3, '已入库', self.green_style)
        worksheet.write(14, 3, '周新增', self.green_style)
        worksheet.write(15, 3, '目标', self.orange_style)
        worksheet.write(16, 3, '已入库', self.orange_style)
        worksheet.write(17, 3, '周新增', self.orange_style)

        worksheet.write_merge(18, 23, 1, 1, '链家', self.grey_style)
        worksheet.write_merge(24, 29, 1, 1, '贝壳', self.grey_style)
        worksheet.write_merge(30, 35, 1, 1, '安居客', self.grey_style)
        worksheet.write_merge(36, 41, 1, 1, '58同城', self.grey_style)
        temp = ['目标', '已入库', '周新增']
        for i in range(18, 42, 6):
            worksheet.write_merge(i, i+2, 2, 2, '二手房', self.grey_style)
            worksheet.write_merge(i+3, i+5, 2, 2, '租房', self.grey_style)
            for t, n in enumerate(range(i, i+3)):
                worksheet.write(n, 3, temp[t], self.green_style)
            for t, n in enumerate(range(i+3, i+6)):
                worksheet.write(n, 3, temp[t], self.orange_style)

        # 插入数据
        # 小区-标准
        unit_goal_row, unit_done_row, unit_weekadd_row = 1, 2, 3
        for index, col in enumerate(range(4, 4 + len(self.city_list))):
            worksheet.write(unit_goal_row, col, comm_unite_goal[self.city_list[index]], self.orange_style)
            city = UniteCity.objects.only('id').filter(name=self.city_list[index]).first()
            if not city:
                count, recent_count = 0, 0
            else:
                count = UniteCommunity.objects.filter(city_id=city.id).count()
                recent_count = UniteCommunity.objects.filter(city_id=city.id, create_time__range=self.date_range).count()
            worksheet.write(unit_done_row, col, count, self.orange_style)
            worksheet.write(unit_weekadd_row, col, recent_count, self.orange_style)

        # 小区-链家
        lj_goal_row, lj_done_row, lj_weekadd_row = 4, 5, 6
        for index, col in enumerate(range(4, 4 + len(self.city_list))):
            worksheet.write(lj_goal_row, col, comm_lj_goal[self.city_list[index]], self.green_style)
            city = LJCity.objects.only('id').filter(name=self.city_list[index]).first()
            if not city:
                count, recent_count = 0, 0
            else:
                count = LJCommunity.objects.filter(city_id=city.id).count()
                recent_count = LJCommunity.objects.filter(city_id=city.id, create_time__range=self.date_range).count()
            worksheet.write(lj_done_row, col, count, self.green_style)
            worksheet.write(lj_weekadd_row, col, recent_count, self.green_style)

        # 小区-贝壳
        bk_goal_row, bk_source_row, bk_done_row, bk_weekadd_row = 7, 8, 9, 10
        for index, col in enumerate(range(4, 4 + len(self.city_list))):
            worksheet.write(bk_goal_row, col, comm_bk_goal[self.city_list[index]], self.orange_style)
            source_count = BKComm.objects.filter(city=self.city_list[index]).count()
            count = BKComm.objects.filter(~Q(unite_id=0), city=self.city_list[index]).count()
            recent_count = BKComm.objects.filter(~Q(unite_id=0), city=self.city_list[index], create_time__range=self.date_range).count()
            worksheet.write(bk_source_row, col, source_count, self.orange_style)
            worksheet.write(bk_done_row, col, count, self.orange_style)
            worksheet.write(bk_weekadd_row, col, recent_count, self.orange_style)

        # 小区-安居客(无create_time)
        ajk_goal_row, ajk_source_row, ajk_done_row, ajk_weekadd_row = 11, 12, 13, 14
        for index, col in enumerate(range(4, 4 + len(self.city_list))):
            worksheet.write(ajk_goal_row, col, comm_ajk_goal[self.city_list[index]], self.green_style)
            source_count = AJKComm.objects.filter(city=self.city_list[index]).count()
            count = AJKComm.objects.filter(~Q(unite_id=0), city=self.city_list[index]).count()
            worksheet.write(ajk_source_row, col, source_count, self.green_style)
            worksheet.write(ajk_done_row, col, count, self.green_style)
            worksheet.write(ajk_weekadd_row, col, '-', self.green_style)

        # 小区-58(暂无)
        five8_goal_row, five8_done_row, five8_weekadd_row = 15, 16, 17
        for index, col in enumerate(range(4, 4 + len(self.city_list))):
            worksheet.write(five8_goal_row, col, comm_58_goal[self.city_list[index]], self.orange_style)
            worksheet.write(five8_done_row, col, 0, self.orange_style)
            worksheet.write(five8_weekadd_row, col, 0, self.orange_style)

        # 房源-链家-二手房
        lj_ershou_goal_row, lj_ershou_done_row, lj_ershou_weekadd_row = 18, 19, 20
        for index, col in enumerate(range(4, 4 + len(self.city_list))):
            worksheet.write(lj_ershou_goal_row, col, lj_ershou_goal[self.city_list[index]], self.green_style)
            city = UniteCity.objects.only('id').filter(name=self.city_list[index]).first()
            if not city:
                count, recent_count = 0, 0
            else:
                count = UniteErShou.objects.filter(origin_id=2, city_id=city.id).count()
                recent_count = UniteErShou.objects.filter(origin_id=2, city_id=city.id, create_time__range=self.date_range).count()
            worksheet.write(lj_ershou_done_row, col, count, self.green_style)
            worksheet.write(lj_ershou_weekadd_row, col, recent_count, self.green_style)

        # 房源-链家-租房
        lj_rent_goal_row, lj_rent_done_row, lj_rent_weekadd_row = 21, 22, 23
        for index, col in enumerate(range(4, 4 + len(self.city_list))):
            worksheet.write(lj_rent_goal_row, col, lj_rent_goal[self.city_list[index]], self.orange_style)
            city = UniteCity.objects.only('id').filter(name=self.city_list[index]).first()
            if not city:
                count, recent_count = 0, 0
            else:
                count = UniteRent.objects.filter(origin_id=2, city_id=city.id).count()
                recent_count = UniteRent.objects.filter(origin_id=2, city_id=city.id, create_time__range=self.date_range).count()
            worksheet.write(lj_rent_done_row, col, count, self.orange_style)
            worksheet.write(lj_rent_weekadd_row, col, recent_count, self.orange_style)

        # 房源-贝壳-二手房
        bk_ershou_goal_row, bk_ershou_done_row, bk_ershou_weekadd_row = 24, 25, 26
        for index, col in enumerate(range(4, 4 + len(self.city_list))):
            worksheet.write(bk_ershou_goal_row, col, bk_ershou_goal[self.city_list[index]], self.green_style)
            city = UniteCity.objects.only('id').filter(name=self.city_list[index]).first()
            if not city:
                count, recent_count = 0, 0
            else:
                count = UniteErShou.objects.filter(origin_id=4, city_id=city.id).count()
                recent_count = UniteErShou.objects.filter(origin_id=4, city_id=city.id, create_time__range=self.date_range).count()
            worksheet.write(bk_ershou_done_row, col, count, self.green_style)
            worksheet.write(bk_ershou_weekadd_row, col, recent_count, self.green_style)

        # 房源-贝壳-租房
        bk_rent_goal_row, bk_rent_done_row, bk_rent_weekadd_row = 27, 28, 29
        for index, col in enumerate(range(4, 4 + len(self.city_list))):
            worksheet.write(bk_rent_goal_row, col, bk_rent_goal[self.city_list[index]], self.orange_style)
            city = UniteCity.objects.only('id').filter(name=self.city_list[index]).first()
            if not city:
                count, recent_count = 0, 0
            else:
                count = UniteRent.objects.filter(origin_id=4, city_id=city.id).count()
                recent_count = UniteRent.objects.filter(origin_id=4, city_id=city.id, create_time__range=self.date_range).count()
            worksheet.write(bk_rent_done_row, col, count, self.orange_style)
            worksheet.write(bk_rent_weekadd_row, col, recent_count, self.orange_style)

        # 房源-安居客-二手房
        ajk_ershou_goal_row, ajk_ershou_done_row, ajk_ershou_weekadd_row = 30, 31, 32
        for index, col in enumerate(range(4, 4 + len(self.city_list))):
            worksheet.write(ajk_ershou_goal_row, col, ajk_ershou_goal[self.city_list[index]], self.green_style)
            city = UniteCity.objects.only('id').filter(name=self.city_list[index]).first()
            if not city:
                count, recent_count = 0, 0
            else:
                count = UniteErShou.objects.filter(origin_id=3, city_id=city.id).count()
                recent_count = UniteErShou.objects.filter(origin_id=3, city_id=city.id, create_time__range=self.date_range).count()
            worksheet.write(ajk_ershou_done_row, col, count, self.green_style)
            worksheet.write(ajk_ershou_weekadd_row, col, recent_count, self.green_style)

        # 房源-安居客-租房
        ajk_rent_goal_row, ajk_rent_done_row, ajk_rent_weekadd_row = 33, 34, 35
        for index, col in enumerate(range(4, 4 + len(self.city_list))):
            worksheet.write(ajk_rent_goal_row, col, ajk_rent_goal[self.city_list[index]], self.orange_style)
            city = UniteCity.objects.only('id').filter(name=self.city_list[index]).first()
            if not city:
                count, recent_count = 0, 0
            else:
                count = UniteRent.objects.filter(origin_id=3, city_id=city.id).count()
                recent_count = UniteRent.objects.filter(origin_id=3, city_id=city.id, create_time__range=self.date_range).count()
            worksheet.write(ajk_rent_done_row, col, count, self.orange_style)
            worksheet.write(ajk_rent_weekadd_row, col, recent_count, self.orange_style)

        # 房源-58-二手房(暂无)
        five8_ershou_goal_row, five8_ershou_done_row, five8_ershou_weekadd_row = 36, 37, 38
        for index, col in enumerate(range(4, 4 + len(self.city_list))):
            worksheet.write(five8_ershou_goal_row, col, five8_ershou_goal[self.city_list[index]], self.green_style)
            worksheet.write(five8_ershou_done_row, col, 0, self.green_style)
            worksheet.write(five8_ershou_weekadd_row, col, 0, self.green_style)

        # 房源-58-租房(暂无)
        five8_rent_goal_row, five8_rent_done_row, five8_rent_weekadd_row = 39, 40, 41
        for index, col in enumerate(range(4, 4 + len(self.city_list))):
            worksheet.write(five8_rent_goal_row, col, five8_rent_goal[self.city_list[index]], self.orange_style)
            worksheet.write(five8_rent_done_row, col, 0, self.orange_style)
            worksheet.write(five8_rent_weekadd_row, col, 0, self.orange_style)

        col_lenght, row_lenght = 4 + len(self.city_list), 42
        for i in range(col_lenght):
            worksheet.col(i).width = 256 * 12
        for i in range(row_lenght):
            tall_style = xlwt.easyxf('font:height 560;')
            worksheet.row(i).set_style(tall_style)
        workbook.save(self.report_path)
