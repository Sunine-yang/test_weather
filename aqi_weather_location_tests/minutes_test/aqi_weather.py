#-*-coding:GBK -*-
import os
import sys

from analysis.url_data import Url_data

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from analysis.comparison_results import Result_check
from analysis.data_analysis import Data_analysis
from tools.easy_mysql import EasyMysql
from tools.read_yaml import ReadYaml
from tools.test_html import Test_mail

class Aqi_Minutes:
    def __init__(self):
        self.result_check = Result_check('aqi_weather')
        self.baseURL=ReadYaml.read_yaml()
    def aqi_weather(self):
        Url_data().wait_aqi_json('baseURL')
        Url_data().wait_aqi_sql_data('requests','city_code','aqi')
        get_data = Url_data().read_aqi_json()
        for i in range(len(get_data["data"])):
            if get_data["data"][i]['cityName'] == '����':
                key_check = self.except_check(get_data["data"][i])
                sql_data = EasyMysql.query_one(self.baseURL['requests']['sql'] % get_data["data"][i]["cityCode"])
                result = '%s,%s |' % (get_data["data"][i]["cityCode"], sql_data[3])
                length = self.result_check.comparison_check(len(get_data["data"][i]), 5, '| �ֽڳ���:(%s/%s)')
                cityName = self.result_check.comparison_in_check(get_data["data"][i]["cityName"], sql_data[3],'| cityName:(%s/%s)')
                aqi = self.result_check.comparison_check(int(get_data["data"][i]["aqi"]), int(sql_data[4]),'| aqi:(%s/%s)')
                level = self.result_check.comparison_check(int(get_data["data"][i]["lv"]), int(sql_data[15]),'| level:(%s/%s)')
                cityProv = self.result_check.comparison_none_check(get_data["data"][i]["cityProv"],'| cityProv:(%s)')
                lv_aqi = self.test_aqi_level(get_data["data"][i])
                result_data = length + cityName + aqi + level + str(lv_aqi)+cityProv + key_check
                if result_data != '':
                    self.result_check.list_data.append(result + result_data)
                else:
                    print(result +'�����ȷ')

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
    def except_check(self,url_data):
        list_key_data = ['cityName', 'aqi', 'lv', 'cityProv','cityCode']
        result_data = []
        for i in range(len(list_key_data)):
            if list_key_data[i] not in str(url_data):
                result = '%s ������' % list_key_data[i]
                result_data.append(result)
            else:
                pass
        if result_data == []:
            return ''
        else:
            data = str(result_data).replace("[", ' ')
            data1 = data.replace("]", '')
            data2=data1.replace(",","| ")
            return data2
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
                Test_mail("[vivo]-[����]-[API]-[�����������а�]-[��%d��]" % a, 'aqi_weather').smtp_on()
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
            Test_mail("[vivo]-[����]-[API]-[�����������а�]-[��%d��]" % a, 'aqi_weather').smtp_on()
            Data_analysis.data_delete('aqi_weather')
            self.result_check.list_data.clear()
        elif  a>=1 and a<=4:
            if self.result_check.list_data == []:
                a = 0
            else:
                a+=1
                self.aqi_weather()
                self.result_check.all_wait_data()
                Test_mail("[vivo]-[����]-[API]-[�����������а�]-[��%d��]"%a , 'aqi_weather').smtp_on()
                Data_analysis.data_delete('aqi_weather')
                self.result_check.list_data.clear()




if __name__ == '__main__':
    Aqi_Minutes().api_start()
