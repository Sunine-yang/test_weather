#-*-coding:GBK -*-
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
"""
    �˴�����·������Linux��ȡʱ��ַ
"""
from test_cases_run.test_location_api import Test_Location
class Test_Location_start:

    def vivo_Location(self):
        Test_Location('baseURL').location_start('����')
        Test_Location('baseURL1').location_start('�Ϻ�')

    def test_api_start(self):
        self.vivo_Location()


if __name__ == '__main__':
    Test_Location_start().test_api_start()