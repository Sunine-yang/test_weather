#-*-coding:GBK -*-
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
"""
    �˴�����·������Linux��ȡʱ��ַ
"""
from test_cases_run.test_weatheraqi import Test_weather_api
class Test_api_start:

    def vivo_aqi(self):
        Test_weather_api('baseURL').air_quality_start('����')
    def test_aqi_start(self):
        self.vivo_aqi()


if __name__ == '__main__':
    Test_api_start().test_aqi_start()