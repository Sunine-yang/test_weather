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


class Test_Location:
    def __init__(self,services):
        self.services = services
        self.result_check=Result_check('Fixed_latitude_longitude')
        self.read_yaml=ReadYaml.read_yaml(self.services)[self.services]
        self.txt=Write_Data_txt

    def get_location(self):
        global sql_info
        print('location  start...........................')
        result1 = EasyMysql(self.services).query_all(self.read_yaml['location_sql'])
        self.txt.write_data('sql_data/location','w+',str(result1))
        txt_data = eval(self.txt.read_data('sql_data/location'))
        for i in range(len(txt_data)):
            try:
                url_data = self.read_yaml["location_url"] % (eval(txt_data[i][7]), eval(txt_data[i][8]))
                code=self.result_check.comparison_check(TestAPI.get_location(url_data).status_code,200,'| ״̬��:(%s/%s)')
                url_get_data = eval(TestAPI.get_location(url_data).text)
                sql_info = '%s,%s,%s,%s |' % (txt_data[i][2],txt_data[i][3], txt_data[i][7], txt_data[i][8])
                city=self.result_check.comparison_none_check(url_get_data,'| city:(%s)')
                countryCode=self.result_check.comparison_none_check(url_get_data["city"]["countryCode"],'| countryCode:(%s)')
                englishCountryName=self.result_check.comparison_none_check(url_get_data["city"]["englishCountryName"],'| englishCountryName:(%s)')
                englishCityName=self.result_check.comparison_none_check(url_get_data["city"]["englishCityName"],'| englishCityName:(%s)')
                administrativearea=self.result_check.comparison_none_check(url_get_data["city"]["administrativearea"],'| administrativearea:(%s)')
                city_len=self.result_check.comparison_check(len(url_get_data["city"]),11,'| city �ֽڳ���:(%s/%s)')
                supplementalAdminAreas=self.result_check.comparison_is_none_check(url_get_data["city"]["supplementalAdminAreas"],'| supplementalAdminAreas:(%s)')
                Cityname=self.result_check.comparison_check(url_get_data["city"]["name"],txt_data[i][3],'| CityCame:(%s/%s)')
                countryname=self.result_check.comparison_check(url_get_data["city"]["countryname"],txt_data[i][5],'| countryname:(%s/%s)')
                citycode=self.result_check.comparison_check(url_get_data["city"]["citycode"],txt_data[i][2],'| citycode:(%s/%s)')
                timezone=self.result_check.comparison_check(url_get_data["city"]["timezone"],txt_data[i][6],'| timezone:(%s&%s)')
                resultcode=self.result_check.comparison_check(url_get_data["resultcode"],'0','| resultcode:(%s/%s)')
                esultinfo=self.result_check.comparison_check(url_get_data["resultinfo"],'success.','| esultinfo:(%s/%s)')
                englishCityNamen=self.result_check.comparison_none_check(url_get_data["city"]["englishCityName"],'| englishCityName:(%s)')
                location_result = city + countryCode + englishCountryName + administrativearea + city_len + supplementalAdminAreas + Cityname + countryname + \
                                  citycode + timezone + resultcode + esultinfo+englishCityName+englishCityNamen+code
                if location_result != '':
                    self.result_check.list_data.append(sql_info + location_result)
                else:
                    print(sql_info+'| ����ͨ��')
            except Exception as e:
                self.result_check.list_data.append('%s,%s,%s,%s |' % (txt_data[i][2],txt_data[i][3], txt_data[i][7], txt_data[i][8])+'| %s ������'%str(e))


    def location_start(self,name):
        self.get_location()
        self.result_check.wait_data_log('��λ��γ�� ��������%d' % (len(self.result_check.list_data)))
        self.result_check.all_wait_data()
        if Data_analysis.document_check('Fixed_latitude_longitude') == None:
            pass
        else:
            Test_mail("[vivo]-[%s]-[����]-[��λ��γ��]-[%d]" % (name,(len(self.result_check.list_data))), 'Fixed_latitude_longitude').smtp_on()
            Data_analysis.data_delete('Fixed_latitude_longitude')
        self.result_check.list_data.clear()



if __name__ == '__main__':
    Test_Location('guangzhou').location_start('����')