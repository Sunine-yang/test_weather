#-*-coding:GBK -*-
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from tools.read_yaml import ReadYaml
from tools.easy_mysql import EasyMysql
from lib.test_api import TestAPI
from analysis.comparison_results import Result_check
from tools.test_html import Test_mail
from analysis.data_analysis import Data_analysis
from analysis.url_data import Url_data
class Test_weather_api:
    def __init__(self,service):
        self.service=service
        self.baseURL = ReadYaml().read_yaml()
        self.result_check=Result_check('Air_Quality_Ranking')
    def url_data_exist_check(self,sql_data,url_data):
        for i in range(0,len(sql_data)):
            if str(sql_data[i][2]) in str(url_data["data"]):
                pass
            else:
                result = '%s,%s |'\
                         % (sql_data[i][2],sql_data[i][3])
                check_data=self.result_check.comparison_not_in_check(str(sql_data[i][0]),str(url_data),'| 数据不存在')
                if check_data=='':
                    pass
                else:
                    self.result_check.list_data.append(result+check_data)
    def get_city_code(self):
        global result
        print('weather  aqi  start...........................')
        Url_data().wait_aqi_json('baseURL')
        Url_data().wait_aqi_sql_data('requests','city_code','aqi')
        get_data = Url_data().read_aqi_json()
        sql_data_all = Url_data().read_sql_data('aqi')
        code_result=self.result_check.comparison_check(TestAPI.get('requests', 'baseURL').status_code, 200,'状态码:(%s/%s)')
        data_sum='url_len :%s  |  sql_len:%s 数据总量错误'%(len(get_data["data"]),len(sql_data_all))
        self.result_check.list_data.append(data_sum)
        self.url_data_exist_check(sql_data_all,get_data)

        for i in range(len(get_data["data"])):
            try:
                key_check=self.except_check(get_data["data"][i])
                sql_data = EasyMysql.query_one(self.baseURL['requests']['sql'] % get_data["data"][i]["cityCode"])
                result='%s,%s |'%(get_data["data"][i]["cityCode"],sql_data[3])
                length=self.result_check.comparison_check(len(get_data["data"][i]),5,'| 字节长度:(%s/%s)')
                cityName=self.result_check.comparison_in_check(get_data["data"][i]["cityName"],sql_data[3],'| cityName:(%s/%s)')
                aqi=self.result_check.comparison_check(int(get_data["data"][i]["aqi"]),int(sql_data[4]),'| aqi:(%s/%s)')
                level=self.result_check.comparison_check(int(get_data["data"][i]["lv"]),int(sql_data[15]),'| level:(%s/%s)')
                cityProv=self.result_check.comparison_none_check(get_data["data"][i]["cityProv"],'| cityProv:(%s)')
                lv_aqi=self.test_aqi_level(get_data["data"][i])
                result_data = length + cityName + aqi + level + str(lv_aqi)+cityProv + key_check+code_result
                if result_data != '':
                    self.result_check.list_data.append(result + result_data)

                else:
                    print(result +'检验通过')

            except Exception as e:

                self.result_check.list_data.append(result + '| %s 不存在' % e)
                self.result_check.logger.warning(e)



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
                result = '%s 不存在' % list_key_data[i]
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
    def air_quality_start(self,name):
        self.get_city_code()
        self.result_check.wait_data_log('空气排行榜 错误数：%d'%(len(self.result_check.list_data)))
        self.result_check.all_wait_data()
        if Data_analysis.document_check('Air_Quality_Ranking')==None:
            pass
        else:
            Test_mail("[vivo]-[%s]-[数据]-[空气排行榜]-[%d]"%(name,(len(self.result_check.list_data))), 'Air_Quality_Ranking').smtp_on()
            Data_analysis.data_delete('Air_Quality_Ranking')
        self.result_check.list_data.clear()



if __name__ == '__main__':
    Test_weather_api('baseURL').air_quality_start('广州')