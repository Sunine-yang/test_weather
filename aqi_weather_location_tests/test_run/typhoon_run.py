#-*-coding:GBK -*-
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
"""
    �˴�����·������Linux��ȡʱ��ַ
"""
from test_cases_run.test_typhoon_api import Test_Typhoon
class Test_Typhoon_start:

    def vivo_api(self):
        Test_Typhoon("typhoon").typhoon_start('����')

    def test_api_start(self):
        self.vivo_api()


if __name__ == '__main__':
    Test_Typhoon_start().test_api_start()