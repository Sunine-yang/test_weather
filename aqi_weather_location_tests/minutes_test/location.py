#-*-coding:GBK -*-
import os
import sys
import time
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from analysis.comparison_results import Result_check
from analysis.data_analysis import Data_analysis
from lib.test_api import TestAPI
from tools.easy_mysql import EasyMysql
from tools.read_yaml import ReadYaml
from tools.test_html import Test_mail
from tools.logger import Logger
class Location_Minutes:
    def __init__(self,service,path_file):
        self.services = service
        self.path_file = path_file
        self.result_check = Result_check(self.path_file)
        self.yaml=ReadYaml.read_yaml(self.services)[self.services]
        self.num=0
        self.logger=Logger.report_logger()
    def get_location(self):

        global sql_info
        print('location  start...........................')
        txt_data=EasyMysql(self.services).query_all(self.yaml["minutes_location_sql"])[0]
        try:
            url_data = self.yaml['minutes_location_url'] % (float(txt_data[7]), float(txt_data[8]))
            status_code=self.result_check.comparison_check(TestAPI.get_location(url_data).status_code, 200,'状态码:(%s/%s)')
            url_get_data = TestAPI.get_location(url_data).json()
            sql_info = '%s,%s,%s,%s |' % (txt_data[2], txt_data[3], txt_data[7], txt_data[8])
            city = self.result_check.comparison_none_check(url_get_data, '| city:(%s)')
            countryCode = self.result_check.comparison_none_check(url_get_data["city"]["countryCode"],
                                                                  '| countryCode:(%s)')
            parentcity = self.result_check.comparison_none_check(url_get_data["city"]["parentcity"],
                                                                 '| parentcity:(%s)')
            englishCountryName = self.result_check.comparison_none_check(url_get_data["city"]["englishCountryName"],
                                                                         '| englishCountryName:(%s)')
            englishCityName = self.result_check.comparison_none_check(url_get_data["city"]["englishCityName"],
                                                                      '| englishCityName:(%s)')
            administrativearea = self.result_check.comparison_none_check(url_get_data["city"]["administrativearea"],
                                                                         '| administrativearea:(%s)')
            city_len = self.result_check.comparison_check(len(url_get_data["city"]), 11, '| city 字节长度:(%s/%s)')
            supplementalAdminAreas = self.result_check.comparison_is_none_check(
                url_get_data["city"]["supplementalAdminAreas"], '| supplementalAdminAreas:(%s)')
            Cityname = self.result_check.comparison_check( txt_data[3],url_get_data["city"]["name"],
                                                          '| CityCame:(%s/%s)')
            countryname = self.result_check.comparison_check( txt_data[5],url_get_data["city"]["countryname"],
                                                             '| countryname:(%s/%s)')
            citycode = self.result_check.comparison_check(txt_data[2],url_get_data["city"]["citycode"],
                                                          '| citycode:(%s/%s)')
            timezone = self.result_check.comparison_check(txt_data[6],url_get_data["city"]["timezone"],
                                                          '| timezone:(%s&%s)')
            provincename = self.result_check.comparison_check(txt_data[4],url_get_data["city"]["provincename"],
                                                              '| provincename:(%s&%s)')
            resultcode = self.result_check.comparison_check(url_get_data["resultcode"], '0', '| resultcode:(%s/%s)')
            esultinfo = self.result_check.comparison_check(url_get_data["resultinfo"], 'success.',
                                                           '| esultinfo:(%s/%s)')
            englishCityNamen = self.result_check.comparison_none_check(Data_analysis.data_take_out_lin(url_get_data["city"]["englishCityName"]), '| englishCityName:(%s)')
            # self.location_check(url_get_data["city"]["administrativearea"]["level"],i[16])
            location_result = city + countryCode + englishCountryName + administrativearea + city_len + supplementalAdminAreas + Cityname + countryname + \
                              citycode + timezone + resultcode + esultinfo + englishCityName + englishCityNamen+status_code+parentcity+provincename
            if location_result != '':
                self.result_check.list_data.append(sql_info + location_result)
            else:
                print(sql_info +'检验通过')

        except Exception as e:
            self.logger.error('Location_Minutes:'+str(e))
            self.result_check.list_data.append(sql_info +"| %s 不存在"%str(e))


    def location_start(self,name):
        while True:
            try:
                self.get_location()
                if self.num == 0:
                    if self.result_check.list_data == []:
                        self.num=0
                    else:
                        self.num+=1
                        self.result_check.all_wait_data()
                        Test_mail("[vivo]-[%s]-[API]-[定位经纬度]-[第%d次]" %(name,self.num) ).smtp_on(self.path_file)
                elif self.num > 4:
                    for i in range(5):
                        if self.result_check.list_data == []:
                            self.num = 0
                            break
                        else:
                            self.num += 1
                            self.result_check.list_data.append('***********************')
                            self.get_location()
                            self.result_check.all_wait_data()
                        time.sleep(60)
                    Test_mail("[vivo]-[%s]-[API]-[定位经纬度]-[第%d次]" %(name,self.num) ).smtp_on(self.path_file)
                elif self.num >= 1 and self.num <= 4:
                    if self.result_check.list_data == []:
                        self.num=0
                    else:
                        self.num += 1
                        self.result_check.all_wait_data()
                        Test_mail("[vivo]-[%s]-[API]-[定位经纬度]-[第%d次]" %(name,self.num) ).smtp_on(self.path_file)
                Data_analysis.data_delete(self.path_file)
                self.result_check.list_data.clear()
                time.sleep(60)
                print('定位经纬度 第%s 执行成功' % self.num)
            except Exception as e:
                print('定位经纬度 第%s 执行失败' % self.num)
                Test_mail("[vivo]-[%s]-[API]-[定位经纬度]-[第%d次]" % (name, self.num)).error_mail(str(e))

if __name__ == '__main__':
    Location_Minutes('guangzhou','guangzhou_location').location_start('广州')