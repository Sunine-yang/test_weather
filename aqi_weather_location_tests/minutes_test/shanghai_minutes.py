#-*-coding:GBK -*-
import os
import sys
import time
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from minutes_test.aqi_weather import Aqi_Minutes
from minutes_test.location import Location_Minutes
from minutes_test.typhoon_test import Typhoon_Minutes
import threading
from tools.html_report_my import Test_mail
def threading_start():

    service='shanghai'
    while True:
        try:
            threads = [threading.Thread(target=Aqi_Minutes(service, '%s_aqi' % service).api_start('上海')),
                       threading.Thread(target=Location_Minutes(service, '%s_location' % service).location_start('上海')),
                       threading.Thread(target=Typhoon_Minutes(service, '%s_typhoon' % service).typhoon_start('上海'))]
            for t in threads:
                # 启动线程
                t.start()

        except Exception as e:
            Test_mail('shanghai_minutes:|'+str(e)).smtp_on()
        time.sleep(60)

threading_start()