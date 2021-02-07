# coding=<encoding name> ： # coding=utf-8
import time
from common.foreign_big import ForeignBig
from getpathInfo import text_Path_shanghai
from text.del_txt import re_foreign_big
from util.fast import do_fast
from util.foreign_data_deal import ForeignDateDeal
from util.send_email_foreign_big import SendEFB

a = ForeignBig(path=text_Path_shanghai())
# 拿数据
datedeal = ForeignDateDeal()
email = SendEFB(path=text_Path_shanghai(), name='上海2')
# 拿 城市编码 ，城市名称， 经度， 纬度
# 104768
accucode1, cityname1, province1, country1, timezone1, geolong1, geolat1 = datedeal.foreign_date(' limit 0, 110000')

print('------------------    开始执行    -----------------------')
start_time = time.time()

do_fast(a.foreign_code_to_name, accucode1, cityname1)
time.sleep(2)
email.send_email_foreign_big(path=text_Path_shanghai())
time.sleep(5)
re_foreign_big(path=text_Path_shanghai())

end_time = time.time()
print(f'执行完毕，耗时：{end_time - start_time}')
print('------------------    执行结束    -----------------------')
print(f'------------------    共耗时{end_time - start_time}    -----------------------')
