import requests
from bs4 import BeautifulSoup
import json
import re

# url = 'https://life.pingan.com/kehufuwu/fuwugongju/return_select.jsp?provice=1&city=1'
url = 'https://life.pingan.com/life/sales/queryAgentsInfo.do?provinceCode=1&cityCode=1&regionCode=&sex=&age=&pageSize=6&pageNo=2&jsoncallback=success_jsoncallback'
ret = requests.get(url)
a = str(ret.content.decode('gbk'))
print(a)
pattern = r"success_jsoncallback\((.*)\)"
b = re.match(pattern, a).group(1)
# b = b.replace('\\', '\\\\')
print(b)
c = json.loads(b)
print(c["resultList"][0]["NAME"])
# soup = BeautifulSoup(ret.content)
# print(soup)
# print(ret.encoding)
