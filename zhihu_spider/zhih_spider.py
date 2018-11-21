import requests
import json
import random
from zhihu_spider.ip import get_random_ip, get_ip_list

num=10
user_all=[]
USER_AGENTS = [

    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",

    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",

    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",

    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",

    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",

    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",

    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",

    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",

    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",

    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",

    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",

    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",

    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",

    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",

    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",

    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",

    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",

    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",

    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",

    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",

    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",

    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",

    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",

    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",

    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",

    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",

    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",

    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",

    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",

    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",

    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",

    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",

    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",

    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"

]
def get_url(url):          #获取链接内容
    header_info = {
        "User-Agent": random.choice(USER_AGENTS)
    }
    user_url =url
    response =requests.get(user_url, headers=header_info, proxies=get_random_ip(get_ip_list()))
    data = response.content
    data = data.decode('utf-8')           #设置字符集
    return data


def get_follower(userID):             #解析内容，获取关注用户
    list=[]
    url = 'https://www.zhihu.com/api/v4/members/'+userID+'/followees?' \
          'include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%' \
          '2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20'
    data = get_url(url)
    data = json.loads(data)
    print(data)
    for user in data['data']:
        list.append(user['url_token'])
    return list

def digui(list):
    global num  # 全局变量，爬取多少次
    temporary = []  # 存放本次爬取的用户名
    for url in list:
        if (num == 10):
            return 0
        else:
            num = num + 1
            print(num)
            list = get_follower(url)
            user_all.extend(list)  # 全局变量，存放所有爬取的用户名
            temporary.extend(list)  # 存放本次爬取的用户名
            print(list)
    digui(temporary)

def get_userInfo(userID):
    info=[]
    url="https://www.zhihu.com/api/v4/members/"+userID+"?include=locations%2Cemployments%2Cgender%2Ceducations%2Cbusiness%2Cvoteup_count%2Cthanked_Count%2Cfollower_count%2Cfollowing_count%2Ccover_url%2Cfollowing_topic_count%2Cfollowing_question_count%2Cfollowing_favlists_count%2Cfollowing_columns_count%2Cavatar_hue%2Canswer_count%2Carticles_count%2Cpins_count%2Cquestion_count%2Ccolumns_count%2Ccommercial_question_count%2Cfavorite_count%2Cfavorited_count%2Clogs_count%2Cmarked_answers_count%2Cmarked_answers_text%2Cmessage_thread_token%2Caccount_status%2Cis_active%2Cis_bind_phone%2Cis_force_renamed%2Cis_bind_sina%2Cis_privacy_protected%2Csina_weibo_url%2Csina_weibo_name%2Cshow_sina_weibo%2Cis_blocking%2Cis_blocked%2Cis_following%2Cis_followed%2Cmutual_followees_count%2Cvote_to_count%2Cvote_from_count%2Cthank_to_count%2Cthank_from_count%2Cthanked_count%2Cdescription%2Chosted_live_count%2Cparticipated_live_count%2Callow_message%2Cindustry_category%2Corg_name%2Corg_homepage%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics"
    data=get_url(url)
    data = json.loads(data)
    if 'avatar_url' in data:
        info.append(data['avatar_url'])       #头像
    else:
        info.append('')
    if 'url_token' in data:
        info.append(data['url_token'])  # id
    else:
        info.append('')
    if 'name' in data:
        info.append(data['name'])
    else:
        info.append('')
    if 'gender' in data:
        info.append(data['gender'])  # 性别
    else:
        info.append('')
    try:
        if 'name' in data['locations'][0]:
            info.append(data['locations'][0]['name'])  # 居住地
        else:
            info.append('')
    except:
        info.append('')

    if 'business' in data:
        info.append(data['business']['name'])  # 所在行业
    else:
        info.append('')
    try:
        if "school" in data['educations'][0]:
            info.append(data['educations'][0]['school']['name'])  # 学校
        else:
            info.append('')
    except:
        info.append('')
    try:
        if 'major' in data['educations'][0]:
            info.append(data['educations'][0]['major']['name'])      #专业
        else:
            info.append('')
    except:
        info.append('')
    if 'follower_count' in data:
        info.append(data['follower_count'])  # 粉丝
    else:
        info.append('')
    if 'following_count' in data:
        info.append(data['following_count'])  # 关注
    else:
        info.append('')
    if 'voteup_count' in data:
        info.append(data['voteup_count'])  # 获赞
    else:
        info.append('')
    if 'thanked_count' in data:
        info.append(data['thanked_count'])  # 感谢
    else:
        info.append('')
    if 'favorited_count' in data:
        info.append(data['favorited_count'])  # 收藏
    else:
        info.append('')
    if 'answer_count' in data:
        info.append(data['answer_count'])  # 回答数
    else:
        info.append('')
    if 'following_question_count' in data:
        info.append(data['following_question_count'])  # 关注的问题
    else:
        info.append('')
    try:
        if 'company' in data['employments'][0]:
            info.append(data['employments'][0]["company"]['name'])  # 公司
        else:
            info.append('')
    except:
        info.append('')

    try:
        if 'job' in data['employments'][0]:
            info.append(data['employments'][0]["job"]['name'])  # 职位
        else:
            info.append('')
    except:
        info.append('')

    return info

# def write_sql_info(list):                #用户信息写入数据库
#     db = pymysql.connect("localhost","root","123456","zhihu_user",charset='utf8')
#     # 使用cursor()方法获取操作游标
#     cursor = db.cursor()
#     # SQL 插入语句
#     sql = """INSERT INTO user_info(avatar_url,url_token,name,gender,locations,business,school,major,follower_count,
# following_count,voteup_count,thanked_count,favorited_count,answer_count,following_question_count,company,job)
#                          VALUES ('""" + list[0] + """','""" + list[1] + """','""" + list[2] + """','""" + list[3] + """',
#                          '""" + list[4] + """','""" + list[5] + """','""" + list[6] + """','""" + list[7] + """',
#                          '""" + list[8] + """','""" + list[9] + """','""" + list[10] + """','""" + list[11] + """',
#                          '""" + list[12] + """','""" +list[13] + """','""" + list[14] + """','""" + list[15] + """','""" + list[16] + """ ')"""
#     try:
#         # 执行sql语句
#         print('写入用户成功')
#         cursor.execute(sql)
#         # 提交到数据库执行
#         db.commit()
#     except:
#         print("已存在")
#         # 如果发生错误则回滚info
#         db.rollback()
#         # 关闭数据库连接
#
#     db.close()

if __name__ == '__main__':

    with open('./url.txt', 'r') as f:
        lines = f.readlines()  # 读取所有行
        last_line = lines[-1]  # 取最后一行
    user_id = last_line  # 继续上一次的爬取
    user = get_follower(user_id)
    if (user == None):
        print("没有关注的人")
    else:
        digui(user)
    user_all = list(set(user_all))  # 去掉重复的用户重
    f = open('./url.txt', 'a')  # 写入文本文件
    for text in user_all:
        f.write('\n' + text)
    user_list = user_all
    f.close()
    for id in user_list:
        user_id = id
        info = get_userInfo(user_id)
        info = [str(i) for i in info]  # 转为字符串
        print(info)
        # write_sql_info(info)  # 写入数据库

