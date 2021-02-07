import time

from common.dailys import Ninety
from getpathInfo import text_Path_shanghai
from text.del_txt import re_file_ninety
from util.data_deal import DateDeal
from util.fast import do_fast
from util.send_email_ninety import SendEN

b = Ninety(path=text_Path_shanghai())
mail = SendEN(path=text_Path_shanghai(), name='上海2')
datedeal = DateDeal()
# 拿 城市编码 ，城市名称， 经度， 纬度
accucode, cityname, geolong, geolat = datedeal.china_date()

nineemptytxt = ''
nineerrotxt = ''
print('------------------    开始执行    -----------------------')
start_time = time.time()
# 九十日
do_fast(b.dailys_api, accucode, cityname)
# time.sleep(2)
mail.send_email_nine(path=text_Path_shanghai())
# time.sleep(5)
re_file_ninety(path=text_Path_shanghai())
end_time = time.time()
print(f'执行完毕，耗时：{end_time - start_time}')
print('------------------    执行结束    -----------------------')
print(f'------------------    共耗时{end_time - start_time}    -----------------------')