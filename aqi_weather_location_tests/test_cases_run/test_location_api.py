#-*-coding:GBK -*-
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from tools.easy_mysql import EasyMysql
from tools.read_yaml import ReadYaml
from lib.test_api import TestAPI
from analysis.comparison_results import Result_check
from tools.test_html import Test_mail
from analysis.data_analysis import Data_analysis
from tools.write_data_txt import Write_Data_txt
from tools.logger import Logger

class Test_Location:
    def __init__(self,services):
        self.services = services
        self.path_name=services+'_Fixed_latitude_longitude'
        self.result_check=Result_check(self.path_name)
        self.read_yaml=ReadYaml.read_yaml(self.services)[self.services]
        self.txt=Write_Data_txt
        self.logger = Logger.report_logger()
    def get_location(self):
        global sql_info
        print('location  start...........................')
        result1 = EasyMysql(self.services).query_all(self.read_yaml['location_sql'])
        self.txt.write_data('sql_data/location','w+',str(result1))
        txt_data = eval(self.txt.read_data('sql_data/location'))
        for i in range(2170,len(txt_data)):
            try:
                url_data = self.read_yaml["location_url"] % (eval(txt_data[i][5]), eval(txt_data[i][6]))
                sql_info = '%s,%s,%s,%s |' % (txt_data[i][0],txt_data[i][1], txt_data[i][5], txt_data[i][6])
                url_get_data = TestAPI.get_location(url_data).json()
                if url_get_data['resultinfo']=='location error!':
                    self.result_check.list_data.append(sql_info+'| %s 返回信息错误'%url_get_data)
                else:
                    code = self.result_check.comparison_check(TestAPI.get_location(url_data).status_code, 200,'| 状态码:(%s/%s)')
                    countryCode=self.result_check.comparison_none_check(url_get_data["city"]["countryCode"],'| countryCode:(%s)')
                    parentcity=self.result_check.comparison_none_check(url_get_data["city"]["parentcity"],'| parentcity:(%s)')
                    englishCountryName=self.result_check.comparison_none_check(url_get_data["city"]["englishCountryName"],'| englishCountryName:(%s)')
                    englishCityName=self.result_check.comparison_none_check(url_get_data["city"]["englishCityName"],'| englishCityName:(%s)')
                    administrativearea=self.result_check.comparison_none_check(url_get_data["city"]["administrativearea"],'| administrativearea:(%s)')
                    city_len=self.result_check.comparison_check(len(url_get_data["city"]),11,'| city 字节长度:(%s/%s)')
                    supplementalAdminAreas=self.result_check.comparison_is_none_check(url_get_data["city"]["supplementalAdminAreas"],'| supplementalAdminAreas:(%s)')
                    Cityname=self.result_check.comparison_check(txt_data[i][1],url_get_data["city"]["name"],'| CityCame:(%s/%s)')
                    countryname=self.result_check.comparison_check(txt_data[i][3],url_get_data["city"]["countryname"],'| countryname:(%s/%s)')
                    citycode=self.result_check.comparison_check(txt_data[i][0],url_get_data["city"]["citycode"],'| citycode:(%s/%s)')
                    timezone=self.result_check.comparison_check(txt_data[i][4],url_get_data["city"]["timezone"],'| timezone:(%s&%s)')
                    provincename=self.result_check.comparison_check(txt_data[i][2],url_get_data["city"]["provincename"],'| provincename:(%s&%s)')
                    resultcode=self.result_check.comparison_check(url_get_data["resultcode"],'0','| resultcode:(%s/%s)')
                    esultinfo=self.result_check.comparison_check(url_get_data["resultinfo"],'success.','| esultinfo:(%s/%s)')
                    englishCityNamen=self.result_check.comparison_none_check(url_get_data["city"]["englishCityName"],'| englishCityName:(%s)')
                    location_result =  countryCode + englishCountryName + administrativearea + city_len + supplementalAdminAreas + Cityname + countryname + \
                                      citycode + timezone + resultcode + esultinfo+englishCityName+englishCityNamen+code+parentcity+provincename
                    if location_result != '':
                        self.result_check.list_data.append(sql_info + location_result)
                    else:
                        pass
                        print(sql_info+'| 测试通过')
            except Exception as e:
                self.logger.error('get_location:'+str(e))
                self.result_check.list_data.append('%s,%s,%s,%s |' % (txt_data[i][0],txt_data[i][1], txt_data[i][5], txt_data[i][6])+'| %s 不存在'%str(e))


    def location_start(self,name):
        self.get_location()
        self.result_check.wait_data_log('定位经纬度 错误数：%d' % (len(self.result_check.list_data)))
        self.result_check.all_wait_data()
        if Data_analysis.document_check(self.path_name) == None:
            pass
        else:
            Test_mail("[vivo]-[%s]-[数据]-[定位经纬度]-[%d]" % (name,(len(self.result_check.list_data)))).smtp_on( self.path_name)
            Data_analysis.data_delete(self.path_name)
        print(self.result_check.list_data)
        self.result_check.list_data.clear()



if __name__ == '__main__':
    Test_Location('guangzhou').location_start('广州')