#-*-coding:GBK -*-
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
"""
    此处加设路径方便Linux读取时地址
"""
import time
from setup_path import Setup_Istall
from test_cases_run.test_typhoon_api import Test_Typhoon
from test_cases_run.test_location_api import Test_Location
from test_cases_run.test_weatheraqi import Test_weather_api
from tools.html_report_my import Test_mail
class Test_start:
    Setup_Istall.set_up_install()
    time.sleep(60)
    def vivo_api(self):
        try:
            while True:
                Test_weather_api('shanghai_baseURL').air_quality_start('上海')
                Test_Typhoon("shanghai_weather_typhoon_list", 'shanghai_weather_typhoon').typhoon_start('上海')
                Test_Location().location_start('baseURL1','上海')
                time.sleep(self.time_info())
        except Exception as e:
            print('运行出错')
            Test_mail(e).smtp_on()
        finally:
            self.vivo_api()

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
