# coding=<encoding name> ： # coding=utf-8
import time
from foreign.foreign_liveInfos import ForeignLiveInfos
from getpathInfo import text_Path_shanghai
from text.del_txt import re_foreign_live
from util.fast import do_fast
from util.foreign_data_deal import ForeignDateDeal
from util.send_email_foreign_live import SendEFL

b = ForeignLiveInfos(path=text_Path_shanghai())
# 拿数据
datedeal = ForeignDateDeal()
email = SendEFL(path=text_Path_shanghai(), name='上海2')
# 拿 城市编码 ，城市名称， 经度， 纬度
# 104768
accucode1, cityname1, province1, country1, timezone1, geolong1, geolat1 = datedeal.foreign_date(' limit 0, 110000')
# accucode2, cityname2, province2, country2, timezone2, geolong2, geolat2 = datedeal.foreign_date(' limit 20000, 20000')
# accucode3, cityname3, province3, country3, timezone3, geolong3, geolat3 = datedeal.foreign_date(' limit 40000, 20000')
# accucode4, cityname4, province4, country4, timezone4, geolong4, geolat4 = datedeal.foreign_date(' limit 60000, 20000')
# accucode5, cityname5, province5, country5, timezone5, geolong5, geolat5 = datedeal.foreign_date(' limit 80000, 30000')

print('------------------    开始执行    -----------------------')
start_time = time.time()

do_fast(b.foreign_liveInfos_api, accucode1, cityname1)
time.sleep(2)
email.send_email_foreign_live(path=text_Path_shanghai())
time.sleep(5)
re_foreign_live(path=text_Path_shanghai())

end_time = time.time()
print(f'执行完毕，耗时：{end_time - start_time}')
print('------------------    执行结束    -----------------------')
print(f'------------------    共耗时{end_time - start_time}    -----------------------')
