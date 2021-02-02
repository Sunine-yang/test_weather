#-*-coding:GBK -*-

from analysis.comparison_results import Result_check
from analysis.data_analysis import Data_analysis
from lib.test_api import TestAPI
from tools.easy_mysql import EasyMysql
from tools.read_yaml import ReadYaml
from tools.test_html import Test_mail



class Location_Minutes:
    def __init__(self):
        self.result_check = Result_check('location')
        self.url=ReadYaml.read_yaml()
    def get_location(self):

        print('location  start...........................')
        i=EasyMysql.query_all(self.url["minute_test"]["location"])[0]
        try:
            url_data = self.url['requests_two']['baseURL'] % (eval(i[7]), eval(i[8]))
            status_code=self.result_check.comparison_check(TestAPI.get_location(url_data).status_code, 200,'状态码:(%s/%s)')
            url_get_data = eval(TestAPI.get_location(url_data).text)
            sql_info = '%s,%s,%s,%s |' % (i[2], i[3], i[7], i[8])
            result_e = self.except_check(url_get_data)
            city = self.result_check.comparison_none_check(url_get_data, '| city:(%s)')
            countryCode = self.result_check.comparison_none_check(url_get_data["city"]["countryCode"],
                                                                  '| countryCode:(%s)')
            englishCountryName = self.result_check.comparison_none_check(url_get_data["city"]["englishCountryName"],
                                                                         '| englishCountryName:(%s)')
            englishCityName = self.result_check.comparison_none_check(url_get_data["city"]["englishCityName"],
                                                                      '| englishCityName:(%s)')
            administrativearea = self.result_check.comparison_none_check(url_get_data["city"]["administrativearea"],
                                                                         '| administrativearea:(%s)')
            city_len = self.result_check.comparison_check(len(url_get_data["city"]), 11, '| city 字节长度:(%s/%s)')
            supplementalAdminAreas = self.result_check.comparison_is_none_check(
                url_get_data["city"]["supplementalAdminAreas"], '| supplementalAdminAreas:(%s)')
            Cityname = self.result_check.comparison_check(url_get_data["city"]["name"], i[3], '| CityCame:(%s/%s)')
            countryname = self.result_check.comparison_check(url_get_data["city"]["countryname"], i[5],
                                                             '| countryname:(%s/%s)')
            citycode = self.result_check.comparison_check(url_get_data["city"]["citycode"], i[2], '| citycode:(%s/%s)')
            timezone = self.result_check.comparison_check(url_get_data["city"]["timezone"], i[6], '| timezone:(%s&%s)')
            resultcode = self.result_check.comparison_check(url_get_data["resultcode"], '0', '| resultcode:(%s/%s)')
            esultinfo = self.result_check.comparison_check(url_get_data["resultinfo"], 'success.',
                                                           '| esultinfo:(%s/%s)')
            englishCityNamen = self.result_check.comparison_none_check(
                Data_analysis.data_take_out_lin(url_get_data["city"]["englishCityName"]), '| englishCityName:(%s)')
            # self.location_check(url_get_data["city"]["administrativearea"]["level"],i[16])
            location_result = city + countryCode + englishCountryName + administrativearea + city_len + supplementalAdminAreas + Cityname + countryname + \
                              citycode + timezone + resultcode + esultinfo + result_e + englishCityName + englishCityNamen+status_code
            if location_result != '':
                self.result_check.list_data.append(sql_info + location_result)
            else:
                print(sql_info +'检验通过')

        except Exception as e:
            self.result_check.list_data.append("| %s 不存在"%str(e))

    def except_check(self,url_data):
        list_key_data = ['countryCode', 'englishCountryName', 'englishCityName', 'administrativearea', 'city',
                         'supplementalAdminAreas', 'name', 'countryname', 'timezone', 'citycode', 'resultcode',
                         'englishCityName', 'level']
        result_data=[]
        for i in range(len(list_key_data)):
            if list_key_data[i] not in str(url_data):
                result = '| %s 不存在' % list_key_data[i]
                result_data.append(result)
            else:
                pass
        if result_data==[]:
            return ''
        else:
            data=str(result_data).replace("[",' ')
            data1=data.replace("]",'')
            data2 = data1.replace(",", "| ")
            return eval(data2)
    def list_check(self):
        if self.result_check.list_data==[]:
            return True
        else:
            return False
    def location_start(self):
        global a
        a = 0
        self.get_location()
        if a == 0:
            if self.result_check.list_data == []:
                a=0
            else:
                a+=1
                self.result_check.all_wait_data()
                Test_mail("[vivo]-[广州]-[API]-[定位]-[第%d次]" % a, 'location').smtp_on()
                Data_analysis.data_delete('location')
                self.result_check.list_data.clear()
        elif a > 4:
            for i in range(5):
                if self.result_check.list_data == []:
                    a = 0
                    break
                else:
                    a += 1
                    self.result_check.list_data.append('***********************')
                    self.get_location()
                    self.result_check.all_wait_data()
            Test_mail("[vivo]-[广州]-[API]-[定位经纬度]-[第%d次]" % a, 'location').smtp_on()
            Data_analysis.data_delete('location')
            self.result_check.list_data.clear()
        elif a >= 1 and a <= 4:
            if self.result_check.list_data == []:
                a=0
            else:
                a += 1
                self.result_check.all_wait_data()
                Test_mail("[vivo]-[广州]-[API]-[定位经纬度]-[第%d次]"%a , 'location').smtp_on()
                Data_analysis.data_delete('location')
                self.result_check.list_data.clear()



if __name__ == '__main__':
    Location_Minutes().location_start()