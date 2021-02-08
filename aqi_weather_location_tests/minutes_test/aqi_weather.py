#-*-coding:GBK -*-
import os
import sys

from analysis.url_data import Url_data
from lib.test_api import TestAPI

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from analysis.comparison_results import Result_check
from analysis.data_analysis import Data_analysis
from tools.easy_mysql import EasyMysql
from tools.read_yaml import ReadYaml
from tools.test_html import Test_mail
from tools.write_read_json import Write_Read_Json
class Aqi_Minutes:
    def __init__(self,service):
        self.service = service
        self.result_check = Result_check('aqi_weather')
        self.baseURL=ReadYaml.read_yaml(self.service)[self.service]
        self.json=Write_Read_Json
    def aqi_weather(self):
        global sql_data
        get_data = TestAPI.get_location(self.baseURL['minutes_aqi_url']).json()
        for i in range(len(get_data["data"])):
            try:
                if get_data["data"][i]['cityCode'] == '106566':
                    print(get_data["data"][i]['cityName'])
                    sql_data = EasyMysql(self.service).query_one(self.baseURL['minutes_aqi_sql'] %'106566')
                    print(sql_data)
                    length = self.result_check.comparison_check(len(get_data["data"][i]), 5, '| 字节长度:(%s/%s)')
                    result = '%s,%s |' % (sql_data[1], sql_data[2])
                    cityName=self.result_check.comparison_check(sql_data[2],get_data["data"][i]["cityName"],'| cityName:(%s/%s)')
                    aqi = self.result_check.comparison_check(int(sql_data[4]), int(get_data["data"][i]["aqi"]),'| aqi:(%s/%s)')
                    level = self.result_check.comparison_check(int(sql_data[5]), int(get_data["data"][i]["lv"]), '| level:(%s/%s)')
                    cityProv = self.result_check.comparison_check(sql_data[3], get_data["data"][i]["cityProv"],'| cityProv:(%s/%s)')
                    lv_aqi = self.test_aqi_level(get_data["data"][i])
                    result_data = length + cityName + aqi + level + str(lv_aqi)+cityProv+cityName
                    if result_data != '':
                        self.result_check.list_data.append(result + result_data)
                    else:
                        print(result +'检测正确')
            except Exception as e:
                self.result_check.list_data.append( sql_data + '| %s 不存在'%e)

    def test_aqi_level(self, url_data):
        if url_data["lv"] == 1 and int(url_data["aqi"]) > 0 and int(url_data["aqi"]) <= 50:
            return ''
        elif url_data["lv"] == 2 and int(url_data["aqi"]) > 50 and int(url_data["aqi"]) <= 100:
            return ''
        elif url_data["lv"] == 3 and int(url_data["aqi"]) > 100 and int(url_data["aqi"]) <= 150:
            return ''
        elif url_data["lv"] == 4 and int(url_data["aqi"]) > 150 and int(url_data["aqi"]) <= 200:
            return ''
        elif url_data["lv"] == 5 and int(url_data["aqi"]) > 200 and int(url_data["aqi"]) <= 300:
            return ''
        elif url_data["lv"] == 6 and int(url_data["aqi"]) > 300:
            return ''
        else:
            return '%s-%s'%(url_data["lv"],url_data["aqi"])

    def api_start(self):
        global a
        a = 0
        self.aqi_weather()
        if a==0:
            if self.result_check.list_data == []:
                a=0
            else:
                a += 1
                self.aqi_weather()
                self.result_check.all_wait_data()
                Test_mail("[vivo]-[广州]-[API]-[空气质量排行榜]-[第%d次]" % a, 'aqi_weather').smtp_on()
                Data_analysis.data_delete('aqi_weather')
                self.result_check.list_data.clear()
        elif a>4:
            for i in range(5):
                if self.result_check.list_data == []:
                    a = 0
                    break
                else:
                    a += 1
                    self.result_check.list_data.append('***********************')
                    self.aqi_weather()
                    self.result_check.all_wait_data()
            Test_mail("[vivo]-[广州]-[API]-[空气质量排行榜]-[第%d次]" % a, 'aqi_weather').smtp_on()
            Data_analysis.data_delete('aqi_weather')
            self.result_check.list_data.clear()
        elif  a>=1 and a<=4:
            if self.result_check.list_data == []:
                a = 0
            else:
                a+=1
                self.aqi_weather()
                self.result_check.all_wait_data()
                Test_mail("[vivo]-[广州]-[API]-[空气质量排行榜]-[第%d次]"%a , 'aqi_weather').smtp_on()
                Data_analysis.data_delete('aqi_weather')
                self.result_check.list_data.clear()




if __name__ == '__main__':
    Aqi_Minutes('guangzhou').aqi_weather()
