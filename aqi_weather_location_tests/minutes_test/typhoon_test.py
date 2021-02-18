#-*-coding:GBK -*-
import sys,time,os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from analysis.comparison_results import Result_check
from analysis.data_analysis import Data_analysis
from lib.test_api import TestAPI
from tools.easy_mysql import EasyMysql
from tools.read_yaml import ReadYaml
from tools.test_html import Test_mail
from tools.write_read_json import Write_Read_Json
from tools.write_data_txt import Write_Data_txt
from test_cases_run.test_cn_typhoon import Test_CNTyphoon
from analysis.url_data import Url_data
class Typhoon_Minutes:
    def __init__(self,service,path_file):
        self.services = service
        self.path_file=path_file
        self.result_check = Result_check(self.path_file)
        self.read_ymal=ReadYaml.read_yaml(self.services)[self.services]
        self.json=Write_Read_Json
        self.txt=Write_Data_txt
        self.num=0
    def weather_typhoon_list_check(self):
        global result
        print('typhoon  start...........................')
        Url_data(self.services).get_number_list()
        data_num=eval(self.txt.read_data('/aqi_data/typhoon_list'))
        url_list = TestAPI.get_location(self.read_ymal["typhoon_list_url"]).json()
        code = self.result_check.comparison_check(
            TestAPI.get_location(self.read_ymal["typhoon_list_url"]).status_code, 200, '| 状态码:(%s/%s)')
        ZtyphoonList = self.result_check.comparison_check(len(url_list), 4, '| ZtyphoonList 字节长度:(%s/%s)')
        typhoonList = self.result_check.comparison_check(len(url_list["data"]["typhoonList"]), 5,
                                                         't| typhoonList 字节长度:(%s/%s)')
        resultinfo = self.result_check.comparison_check(url_list["resultinfo"], 'OK', '| resultinfo:(%s/%s)')
        servertime = self.result_check.comparison_none_check(url_list["servertime"], '| servertime:(%s)')
        resultcode = self.result_check.comparison_check(url_list["resultcode"], '0', '| resultcode:(%s/%s)')
        typhoon_list_data =  code + ZtyphoonList + typhoonList + resultinfo + servertime + resultcode
        if typhoon_list_data != '':
            self.result_check.list_data.append('台风列表接口 |' + typhoon_list_data)
        else:
            pass
        for i in range(len(url_list["data"]["typhoonList"])):
            result = '%s,%s |' % (url_list["data"]["typhoonList"][i]["nameZh"], '20' + url_list["data"]["typhoonList"][i]["code"])
            typhoonList_l = self.result_check.comparison_check(len(url_list["data"]["typhoonList"][i]), 4,result + '| typhoonList 字节长度:(%s/%s)')
            nameZh = self.result_check.comparison_check(url_list["data"]["typhoonList"][i]["nameZh"], str(data_num[-i - 1][2]), '| nameZh:(%s/%s)')
            nameEn = self.result_check.comparison_check(url_list["data"]["typhoonList"][i]["nameEn"],str(data_num[-i - 1][1]), '| nameEn:(%s/%s)')
            codes = self.result_check.comparison_in_check(url_list["data"]["typhoonList"][i]["code"],str(data_num[-i - 1][3]), '| code:(%s/%s)')
            number = self.result_check.comparison_none_check(url_list["data"]["typhoonList"][i]["number"],'| number:(%s)')
            typhoon_list_datas =  typhoonList_l + nameEn + nameZh + codes + number
            if typhoon_list_datas != '':
                self.result_check.list_data.append(
                    '%s,%s |' % (data_num[-i - 1][2], '20' + str(data_num[-i - 1][3]) + typhoon_list_datas))
            else:
                print(result+'| 检测通过')
        self.test_weather_typhoon_check()
    def test_weather_typhoon_check(self):
        import random
        global url_report
        numbers=2005
        get_url = TestAPI.get_location(self.read_ymal["minutes_typhoon_track_url"] % ('20' + str(numbers))).json()
        self.json.write_json('/aqi_data/20%s'%str(numbers),get_url)
        weather_url = self.json.read_json('/aqi_data/20%s' % str(numbers))
        sql_data = EasyMysql(self.services).query_all(self.read_ymal["minutes_typhoon_track_sql"] % ('20'+str(numbers)))
        url_report = '%s,%s |' % (sql_data[0][3], '20' + str(numbers))
        number = self.result_check.comparison_check(len(sql_data),len(weather_url["data"]["track"]), '| 数据条数:(%d/%d)')
        time_c = self.result_check.comparison_check(int(str(Data_analysis.time_disposes(sql_data[0][5])) + '000'),weather_url["data"]["changeTrender"][0]["time"],
                                                    '| 起编时间:(%s/%s)')
        total_len = self.result_check.comparison_check(len(weather_url), 4,'| 总字段长度:(%s/%s)')
        data = self.result_check.comparison_check(len(weather_url["data"]), 10,'| data 字段长度:(%s/%s)')
        resultcode = self.result_check.comparison_check(weather_url["resultcode"], '0','| resultcode:(%s/%s)')
        resultinfo = self.result_check.comparison_check(weather_url["resultinfo"], 'OK','| resultinfo:(%s/%s)')
        endTime = self.result_check.comparison_none_check(weather_url["data"]["endTime"],'| endTime:(%s)')
        source = self.result_check.comparison_none_check(weather_url["data"]["source"],'| source:(%s)')
        startTime = self.result_check.comparison_none_check(weather_url["data"]["startTime"],'| startTime:(%s)')
        sustainedTime = self.result_check.comparison_none_check(weather_url["data"]["sustainedTime"],'| sustainedTime:(%s)')
        self.typhoon_track_check(weather_url, sql_data)
        typhoon_result = number + time_c + total_len + data + resultcode + resultinfo + endTime + source + startTime + sustainedTime
        if typhoon_result != '':
            self.result_check.list_data.append('%s |' % url_report + typhoon_result)
        else:
            print(url_report +'| 检验通过')

    def typhoon_track_check(self, weather_url, sql_data):
        for a in range(len(weather_url["data"]["track"])):
            url_report_time = url_report + sql_data[a][5]
            track = self.result_check.comparison_check(len(weather_url["data"]["track"][a]), 6,'| track 字段长度:(%s/%s)')
            centralPressure = self.result_check.comparison_check(  sql_data[a][11],weather_url["data"]["track"][a]["centralPressure"],
                '| centralPressure:(%s/%s)')
            latitude = self.result_check.comparison_check(sql_data[a][8],weather_url["data"]["track"][a]["latitude"],'| latitude:(%s/%s)')
            level = self.result_check.comparison_check(sql_data[a][9],weather_url["data"]["track"][a]["level"], '| level:(%s/%s)')
            longitude = self.result_check.comparison_check(sql_data[a][7],weather_url["data"]["track"][a]["longitude"],'| longitude:(%s/%s)')
            windSpeed = self.result_check.comparison_check(sql_data[a][10],weather_url["data"]["track"][a]["windSpeed"],'| windSpeed speed:(%s/%s)')
            time_d = self.result_check.comparison_check(sql_data[a][5],self.time_transform(weather_url["data"]["track"][a]["time"]), '| time:(%s/%s)')
            typhoonId = self.result_check.comparison_check(sql_data[a][1],weather_url["data"]["typhoonId"],' | typhoonId:(%s/%s)')
            typhoonNameEn = self.result_check.comparison_check(sql_data[a][2],weather_url["data"]["typhoonNameEn"],'| typhoonNameEn:(%s/%s)')
            typhoonNameZh = self.result_check.comparison_check(sql_data[a][3],weather_url["data"]["typhoonNameZh"],'| typhoonNameZh:(%s/%s)')
            typhoon_track = track + centralPressure + latitude + level + longitude + windSpeed + time_d + typhoonId + typhoonNameEn + typhoonNameZh
            if typhoon_track != '':
                self.result_check.list_data.append('%s |' % url_report_time + typhoon_track)
            else:
                print(url_report_time + ' 检查通过')
    def time_transform(cls,data):
        import time
        timeStamp = float(int(data) / 1000)
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%Y-%m-%d %H", timeArray)
        return otherStyleTime

    def typhoon_start(self,name):
        while True:
            time.sleep(60)
            if self.num == 0:
                self.weather_typhoon_list_check()
                if self.result_check.list_data == []:
                    self.num = 0
                else:
                    self.num += 1
                    self.weather_typhoon_list_check()
                    self.result_check.all_wait_data()
                    Test_mail("[vivo]-[%s]-[API]-[台风]-[第%d次]" % (name,self.num), self.path_file).smtp_on()
                    Data_analysis.data_delete(self.path_file)
                    self.result_check.list_data.clear()
            elif self.num > 4:
                for i in range(5):
                    if self.result_check.list_data == []:
                        self.num = 0
                        break
                    else:
                        self.num += 1
                        self.result_check.list_data.append('***********************')
                        self.weather_typhoon_list_check()
                        self.result_check.all_wait_data()
                Test_mail("[vivo]-[%s]-[API]-[台风]-[第%d次]" % (name,self.num), self.path_file).smtp_on()
                Data_analysis.data_delete(self.path_file)
                self.result_check.list_data.clear()
            elif  self.num >= 1 and self.num <= 4:
                if self.result_check.list_data == []:
                    self.num = 0
                else:
                    self.num+=1
                    self.weather_typhoon_list_check()
                    self.result_check.all_wait_data()
                    Test_mail("[vivo]-[%s]-[API]-[台风]-[第%d次]" % (name,self.num) ,self.path_file).smtp_on()
                    Data_analysis.data_delete(self.path_file)
                    self.result_check.list_data.clear()
if __name__ == '__main__':
    Typhoon_Minutes('guangzhou','typhoon').typhoon_start('广州')