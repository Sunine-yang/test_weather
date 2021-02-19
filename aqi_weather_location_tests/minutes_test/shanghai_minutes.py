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
from multiprocessing import Process
service='shanghai'
def func1():
    Aqi_Minutes(service,'%s_aqi'%service).api_start('上海')
def func2():
    Location_Minutes(service,'%s_location'%service).location_start('上海')
def func3():
    Typhoon_Minutes(service,'%s_typhoon'%service).typhoon_start('上海')
if __name__ == '__main__':
    proc1 = Process(target=func1)
    proc1.start()
    proc2 = Process(target=func2)
    proc2.start()
    proc3 = Process(target=func3)
    proc3.start()