#-*-coding:GBK -*-
import os
import sys

from tools.easy_mysql import EasyMysql

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from tools.read_yaml import ReadYaml
from lib.test_api import TestAPI
from analysis.comparison_results import Result_check
from tools.test_html import Test_mail
from analysis.data_analysis import Data_analysis
from tools.write_read_json import Write_Read_Json
from tools.write_data_txt import Write_Data_txt
class Test_weather_api:
    def __init__(self,service):

        self.txt=Write_Data_txt
        self.json=Write_Read_Json
        self.service=service
        self.baseURL = ReadYaml().read_yaml()
        self.result_check=Result_check('Air_Quality_Ranking')
    def url_data_exist_check(self,sql_data_all,url_data):
        for i in range(0,len(sql_data_all)):
            if str(sql_data_all[i][2]) in str(url_data["data"]):
                pass
            else:
                result = '%s,%s |'\
                         % (sql_data_all[i][1],sql_data_all[i][2])
                check_data=self.result_check.comparison_not_in_check(str(sql_data_all[i][1]),str(url_data), '| %s 数据缺失')
                if check_data=='':
                    pass
                else:
                    self.result_check.list_data.append(result+check_data)
    def get_city_code(self):
        global result, length
        print('weather  aqi  start...........................')
        get_url = TestAPI.get_location(self.baseURL[self.service]['aqi_rul']).json()
        sql_data = EasyMysql.query_all(self.baseURL[self.service]['aqi_sql'])
        self.json.write_json('/aqi_data/aqi',get_url)
        self.txt.write_data('/sql_data/aqi','w+',str(sql_data))
        get_data=self.json.read_json('/aqi_data/aqi')
        sql_data_all=eval(self.txt.read_data('/sql_data/aqi'))

        code_result=self.result_check.comparison_check(TestAPI.get_location(self.baseURL[self.service]['aqi_rul']).status_code, 200,'状态码:(%s/%s)')
        data_sum=self.result_check.comparison_check(len(get_data["data"]),len(sql_data_all),'url_len :%s  |  sql_len:%s 数据总量错误')
        if data_sum=='':
            pass
        else:
            self.result_check.list_data.append(data_sum)
        self.url_data_exist_check(sql_data_all,get_data)
        for i in range(len(sql_data_all)):
            for j in range(len(get_data["data"])):
                try:
                    if get_data["data"][j]["cityCode"]==sql_data_all[i][1]:
                        length = self.result_check.comparison_check(len(get_data["data"][j]), 5, '| 字节长度:(%s/%s)')
                        result = '%s,%s |' % (sql_data_all[i][1], sql_data_all[i][2])
                        aqi = self.result_check.comparison_check(int(get_data["data"][j]["aqi"]), int(sql_data_all[i][4]),'| aqi:(%s/%s)')
                        level = self.result_check.comparison_check(int(get_data["data"][j]["lv"]), int(sql_data_all[i][5]),'| level:(%s/%s)')
                        cityProv = self.result_check.comparison_check(get_data["data"][j]["cityProv"],sql_data_all[i][3],'| cityProv:(%s/%s)')
                        lv_aqi = self.test_aqi_level(get_data["data"][j])
                        result_data = length  + aqi + level + str(lv_aqi) + cityProv + code_result
                        if result_data != '':
                                print(result_data)
                                self.result_check.list_data.append(result + result_data)
                        else:
                            print(result + '检验通过')
                    else:
                            pass
                except Exception as e:
                        self.result_check.list_data.append(result+'| %s 不存在'%e)

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
    Test_weather_api('guangzhou').air_quality_start('广州')