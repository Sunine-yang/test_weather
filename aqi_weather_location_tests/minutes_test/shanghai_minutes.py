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

    service='shanghai_minutes'
    while True:
        try:
            threads = [threading.Thread(target=Aqi_Minutes(service).api_start()),
                       threading.Thread(target=Location_Minutes(service).location_start()),
                       threading.Thread(target=Typhoon_Minutes(service).typhoon_start())]
            for t in threads:
                # 启动线程
                t.start()
            time.sleep(60)
        except Exception as e:
            Test_mail(str(e)).smtp_on()

threading_start()