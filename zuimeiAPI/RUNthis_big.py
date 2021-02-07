# coding=<encoding name> ： # coding=utf-8
import time

from common.big import Big
from common.liveInfos import LiveInfos
from common.search import Search
from text.del_txt import re_file_search_big
from util.data_deal import DateDeal
from util.fast import do_fast
from util.send_email import SendEmail

a = Big()
b = LiveInfos()
c = Search()
email = SendEmail()
# 拿数据
datedeal = DateDeal()
# 拿 城市编码 ，城市名称， 经度， 纬度
accucode, cityname, geolong, geolat = datedeal.china_date()

print('------------------    开始执行    -----------------------')
start_time = time.time()
# 大颗粒-accucode
do_fast(a.code_to_name, accucode, cityname)
# 生活指数
do_fast(b.liveInfos_api, accucode, cityname)
# 搜索
c.search_api()


time.sleep(2)
email.send_email()
time.sleep(5)
re_file_search_big()
end_time = time.time()
print(f'执行完毕，耗时：{end_time - start_time}')
print('------------------    执行结束    -----------------------')
print(f'------------------    共耗时{end_time - start_time}    -----------------------')