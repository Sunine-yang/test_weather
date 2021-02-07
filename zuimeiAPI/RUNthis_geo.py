# coding=<encoding name> ： # coding=utf-8
import time

from common.geo import Geo
from text.del_txt import re_file_search_big_geo
from util.data_deal import DateDeal
from util.fast import do_fast
from util.send_email_geo import SendEG

a = Geo()
mail = SendEG()

# 拿数据
datedeal = DateDeal()
# 拿 城市编码 ，城市名称， 经度， 纬度
accucode, cityname, geolong, geolat = datedeal.china_date()

print('------------------    开始执行    -----------------------')
start_time = time.time()
# 大颗粒-accucode
do_fast(a.geo_to_name, geolong, geolat, cityname)
# 大颗粒-经纬度
# 搜索
time.sleep(2)
mail.send_email_geo()
time.sleep(5)
re_file_search_big_geo()
end_time = time.time()
print(f'执行完毕，耗时：{end_time - start_time}')
print('------------------    执行结束    -----------------------')
print(f'------------------    共耗时{end_time - start_time}    -----------------------')