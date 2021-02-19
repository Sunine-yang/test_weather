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
from analysis.data_analysis import Data_analysis
class Test_start:
    Data_analysis.delete_logs()
    services = 'guangzhou'
    def vivo_api(self):
        try:

            Test_weather_api(self.services).air_quality_start('����')
            Test_CNTyphoon(self.services).cnscene_typhoon_start('����')
            Test_Typhoon(self.services).weather_typhoon_start('����')
            Test_Location(self.services).location_start('����')

        except Exception as e:
            print('���д���')
            Test_mail('guangzhou:'+str(e)).smtp_on()


if __name__ == '__main__':
    Test_start().vivo_api()
