#-*-coding:GBK -*-
from analysis.test_location_data import Test_Loction_data
from tools.read_yaml import ReadYaml
from lib.test_api import TestAPI
from analysis.comparison_results import Result_check
from tools.test_html import Test_mail
from analysis.data_analysis import Data_analysis

class Test_Location:
    def __init__(self,service):
        self.result_check=Result_check('Fixed_latitude_longitude')
        self.url=ReadYaml.read_yaml()['requests_two'][service]
    def get_location(self):
        global sql_info
        print('location  start...........................')
        Test_Loction_data.with_data()
        txt_data = Test_Loction_data.read_data()
        for i in eval(txt_data[0]):
            try:
                url_data = self.url % (eval(i[7]), eval(i[8]))
                code=self.result_check.comparison_check(TestAPI.get_location(url_data).status_code,200,'| 状态码:(%s/%s)')
                url_get_data = eval(TestAPI.get_location(url_data).text)
                sql_info = '%s,%s,%s,%s |' % (i[2],i[3], i[7], i[8])
                result_e=self.except_check(url_get_data)
                city=self.result_check.comparison_none_check(url_get_data,'| city:(%s)')
                countryCode=self.result_check.comparison_none_check(url_get_data["city"]["countryCode"],'| countryCode:(%s)')
                englishCountryName=self.result_check.comparison_none_check(url_get_data["city"]["englishCountryName"],'| englishCountryName:(%s)')
                englishCityName=self.result_check.comparison_none_check(url_get_data["city"]["englishCityName"],'| englishCityName:(%s)')
                administrativearea=self.result_check.comparison_none_check(url_get_data["city"]["administrativearea"],'| administrativearea:(%s)')
                city_len=self.result_check.comparison_check(len(url_get_data["city"]),11,'| city 字节长度:(%s/%s)')

                supplementalAdminAreas=self.result_check.comparison_is_none_check(url_get_data["city"]["supplementalAdminAreas"],'| supplementalAdminAreas:(%s)')
                Cityname=self.result_check.comparison_check(url_get_data["city"]["name"],i[3],'| CityCame:(%s/%s)')
                countryname=self.result_check.comparison_check(url_get_data["city"]["countryname"],i[5],'| countryname:(%s/%s)')
                citycode=self.result_check.comparison_check(url_get_data["city"]["citycode"],i[2],'| citycode:(%s/%s)')
                timezone=self.result_check.comparison_check(url_get_data["city"]["timezone"],i[6],'| timezone:(%s&%s)')

                resultcode=self.result_check.comparison_check(url_get_data["resultcode"],'0','| resultcode:(%s/%s)')
                print(1)
                esultinfo=self.result_check.comparison_check(url_get_data["resultinfo"],'success.','| esultinfo:(%s/%s)')
                print(2)
                englishCityNamen=self.result_check.comparison_none_check(url_get_data["city"]["englishCityName"],'| englishCityName:(%s)')
                # self.location_check(url_get_data["city"]["administrativearea"]["level"],i[16])
                print(Data_analysis.data_take_out_lin(url_get_data["city"]["englishCityName"]))
                location_result = city + countryCode + englishCountryName + administrativearea + city_len + supplementalAdminAreas + Cityname + countryname + \
                                  citycode + timezone + resultcode + esultinfo + result_e+englishCityName+englishCityNamen+code
                if location_result != '':
                    self.result_check.list_data.append(sql_info + location_result)
                else:
                    pass

            except Exception as e:
                print(e)
                if e=="name 'null' is not defined":
                    pass

                else:
                    self.result_check.list_data.append(sql_info+'| %s 不存在'%e)





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
    def location_start(self,name):
        self.get_location()
        self.result_check.wait_data_log('定位经纬度 错误数：%d' % (len(self.result_check.list_data)))
        self.result_check.all_wait_data()
        if Data_analysis.document_check('Fixed_latitude_longitude') == None:
            pass
        else:
            Test_mail("[vivo]-[%s]-[数据]-[定位经纬度]-[%d]" % (name,(len(self.result_check.list_data))), 'Fixed_latitude_longitude').smtp_on()
            Data_analysis.data_delete('Fixed_latitude_longitude')
        self.result_check.list_data.clear()



if __name__ == '__main__':
    Test_Location('baseURL').location_start('广州')