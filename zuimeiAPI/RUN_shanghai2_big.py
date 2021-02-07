# coding=<encoding name> ： # coding=utf-8
import time

from common.big import Big
from common.liveInfos import LiveInfos
from common.search import Search
from getpathInfo import text_Path_shanghai
from text.del_txt import re_file_search_big
from util.data_deal import DateDeal
from util.fast import do_fast
from util.send_email import SendEmail

a = Big(path=text_Path_shanghai(), url_data='pub.zuimeitianqi.com')
b = LiveInfos(path=text_Path_shanghai(), url_data='pub.zuimeitianqi.com')
c = Search(path=text_Path_shanghai(), url_data='pub.zuimeitianqi.com')
email = SendEmail(path=text_Path_shanghai(), name='上海2')
# 拿数据
datedeal = DateDeal()
# 拿 城市编码 ，城市名称， 经度， 纬度
accucode, cityname, geolong, geolat = datedeal.china_date()

print('------------------    开始执行    -----------------------')
start_time = time.time()
# 大颗粒-accucode
# 大颗粒-accucode
do_fast(a.code_to_name, accucode, cityname)
# 生活指数
do_fast(b.liveInfos_api, accucode, cityname)
# 搜索
c.search_api()


time.sleep(2)
email.send_email(path=text_Path_shanghai())
time.sleep(5)
re_file_search_big(path=text_Path_shanghai())
end_time = time.time()
print(f'执行完毕，耗时：{end_time - start_time}')
print('------------------    执行结束    -----------------------')
print(f'------------------    共耗时{end_time - start_time}    -----------------------')