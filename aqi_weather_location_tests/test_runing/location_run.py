#-*-coding:GBK -*-
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
"""
    此处加设路径方便Linux读取时地址
"""
from test_cases_run.test_location_api import Test_Location
class Test_Location_start:

    def vivo_Location(self):
        Test_Location('baseURL').location_start('广州')
        Test_Location('baseURL1').location_start('上海')

    def test_api_start(self):
        self.vivo_Location()


if __name__ == '__main__':
    Test_Location_start().test_api_start()