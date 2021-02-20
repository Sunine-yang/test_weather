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
from test_cases_run.million_large_partices import Large_Particles
from tools.test_html import Test_mail
class Test_start:
    def vivo_api(self):
        try:
            for i in range(300):
                Large_Particles('shanghai').large_particles_start(i, '上海')
        except Exception as e:
            Test_mail('上海300万站点检测').error_mail(str(e))


if __name__ == '__main__':
    Test_start().vivo_api()