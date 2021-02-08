#-*-coding:GBK -*-
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
"""
    �˴�����·������Linux��ȡʱ��ַ
"""
import time
from test_cases_run.test_typhoon_api import Test_Typhoon
from test_cases_run.test_location_api import Test_Location
from test_cases_run.test_weatheraqi import Test_weather_api
from test_cases_run.test_cn_typhoon import Test_CNTyphoon
from tools.html_report_my import Test_mail
class Test_start:

    services = 'shanghai'
    def vivo_api(self):
        try:

            Test_weather_api(self.services).air_quality_start('�Ϻ�')
            Test_CNTyphoon(self.services).cnscene_typhoon_start('�Ϻ�')
            Test_Typhoon(self.services).weather_typhoon_start('�Ϻ�')
            Test_Location(self.services).location_start('�Ϻ�')

        except Exception as e:
            print('���д���')
            Test_mail(str(e)).smtp_on()


    def time_info(self):
        total_time = time.strftime("%H:%M:%S", time.localtime(float(time.time())))
        ti = str(total_time)
        h, m, s = ti.strip().split(':')
        seconds = int(h) * 3600 + int(m) * 60 + int(s)
        if seconds>32400 and seconds<54000:
            result=54000-seconds
            return result
        elif seconds>54000 :
            result=86400-seconds+32400
            return result

if __name__ == '__main__':
    Test_start().vivo_api()
