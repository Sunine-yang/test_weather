#-*-coding:GBK -*-
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
"""
    此处加设路径方便Linux读取时地址
"""
from test_cases_run.test_typhoon_api import Test_Typhoon
class Test_Typhoon_start:

    def vivo_api(self):
        Test_Typhoon("typhoon").typhoon_start('广州')

    def test_api_start(self):
        self.vivo_api()


if __name__ == '__main__':
    Test_Typhoon_start().test_api_start()