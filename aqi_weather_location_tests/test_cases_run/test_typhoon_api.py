#-*-coding:GBK -*-
import os,sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from lib.test_api import TestAPI
from tools.easy_mysql import EasyMysql
from tools.read_yaml import ReadYaml
from analysis.comparison_results import Result_check
from analysis.data_analysis import Data_analysis
from tools.test_html import Test_mail
from tools.write_read_json import Write_Read_Json
from tools.write_data_txt import Write_Data_txt
from analysis.url_data import Url_data
from tools.logger import Logger
class Test_Typhoon:
    def __init__(self,services):
        self.services = services
        self.json=Write_Read_Json
        self.path_name=services+'_typhoon_list_track'
        self.result_check=Result_check(self.path_name)
        self.read_ymal=ReadYaml.read_yaml(self.services)[self.services]
        self.txt=Write_Data_txt
        self.logger=Logger.report_logger()
    def weather_typhoon_list_check(self):

        global result
        result= '̨���б�ӿ� |'
        Url_data(self.services).get_number_list()
        data_num=eval(self.txt.read_data('aqi_data/typhoon_list'))
        url_list = TestAPI.get_location(self.read_ymal['typhoon_list_url']).json()
        code=self.result_check.comparison_check(TestAPI.get_location(self.read_ymal['typhoon_list_url']).status_code,200,'| ״̬��:(%s/%s)')
        ZtyphoonList=self.result_check.comparison_check(len(url_list),4,'| ZtyphoonList �ֽڳ���:(%s/%s)')
        typhoonList=self.result_check.comparison_check(len(url_list["data"]["typhoonList"]),5,'t| typhoonList �ֽڳ���:(%s/%s)')
        resultinfo=self.result_check.comparison_check(url_list["resultinfo"],'OK','| resultinfo:(%s/%s)')
        servertime=self.result_check.comparison_none_check(url_list["servertime"],'| servertime:(%s)')
        resultcode=self.result_check.comparison_check(url_list["resultcode"],'0','| resultcode:(%s/%s)')
        typhoon_list_data=code+ZtyphoonList+typhoonList+resultinfo+servertime+resultcode
        if typhoon_list_data != '':
            self.result_check.list_data.append('̨���б�ӿ� |'+ typhoon_list_data)
        else:
            pass
        for i in range(len(url_list["data"]["typhoonList"])):
            try:

                typhoonList_l=self.result_check.comparison_check(len(url_list["data"]["typhoonList"][i]),4,result+'| typhoonList �ֽڳ���:(%s/%s)')
                nameZh=self.result_check.comparison_check(url_list["data"]["typhoonList"][i]["nameZh"],str(data_num[-i-1][2]),'| nameZh:(%s/%s)')
                nameEn=self.result_check.comparison_check(url_list["data"]["typhoonList"][i]["nameEn"],str(data_num[-i-1][1]),'| nameEn:(%s/%s)')
                codes=self.result_check.comparison_in_check(url_list["data"]["typhoonList"][i]["code"],str(data_num[-i-1][3]),'| code:(%s/%s)')
                number=self.result_check.comparison_none_check(url_list["data"]["typhoonList"][i]["number"],'| number:(%s)')
                typhoon_list_datas=typhoonList_l+nameEn+nameZh+codes+number
                if typhoon_list_datas != '':
                    self.result_check.list_data.append('%s,%s |'%(data_num[-i-1][2],'20'+str(data_num[-i-1][3]) + typhoon_list_datas))
                else:
                    print(result +url_list["data"]["typhoonList"][i]["nameZh"]+'| �����ȷ')
            except Exception as e:
                self.logger.error('weather_typhoon_list_check:'+str(e))
                self.result_check.list_data.append(result + '| %s ������' % e)

    def test_weather_typhoon_check(self):
        global url_report
        data_num=eval(self.txt.read_data('aqi_data/typhoon_list'))
        for i in range(len(data_num)):
            get_url = TestAPI.get_location(self.read_ymal['typhoon_track_url'] % ('20' + str(data_num[i][3]))).json()
            self.json.write_json('/aqi_data/20%s'%data_num[i][3],get_url)
            try:
                sql_data = EasyMysql(self.services).query_all(self.read_ymal["typhoon_bast_track_sql"] % data_num[i][1])
                weather_url=self.json.read_json('aqi_data/%s'%('20'+str(data_num[i][3])))
                url_report = '%s,%s'%(data_num[i][1],'20'+str(data_num[i][3]))
                number=self.result_check.comparison_check(len(weather_url["data"]["track"]), len(sql_data),
                                                   '| ��������:(%d/%d)')
                time_c=self.result_check.comparison_check(weather_url["data"]["changeTrender"][0]["time"],int(str(Data_analysis.time_disposes(sql_data[0][5]))+'000'),
                                                   '| ���ʱ��:(%s/%s)')
                total_len=self.result_check.comparison_check(len(weather_url),4,
                                                   '| ���ֶγ���:(%s/%s)')
                data=self.result_check.comparison_check(len(weather_url["data"]),10,
                                                   '| data �ֶγ���:(%s/%s)')
                resultcode=self.result_check.comparison_check(weather_url["resultcode"],'0',
                                                   '| resultcode:(%s/%s)')
                resultinfo=self.result_check.comparison_check(weather_url["resultinfo"],'OK',
                                                   '| resultinfo:(%s/%s)')
                endTime=self.result_check.comparison_none_check(weather_url["data"]["endTime"],
                                                    '| endTime:(%s)')
                source=self.result_check.comparison_none_check(weather_url["data"]["source"],
                                                    '| source:(%s)')
                startTime=self.result_check.comparison_none_check(weather_url["data"]["startTime"],
                                                   '| startTime:(%s)')
                sustainedTime=self.result_check.comparison_none_check(weather_url["data"]["sustainedTime"],
                                                   '| sustainedTime:(%s)')
                self.typhoon_track_check(weather_url,sql_data)
                typhoon_result=number+time_c+total_len+data+resultcode+resultinfo+endTime+source+startTime+sustainedTime
                if typhoon_result != '':
                    self.result_check.list_data.append('%s |'%url_report + typhoon_result)
                else:
                    print('%s |'%url_report+'���ͨ��')
            except Exception as e:
                self.logger.error('test_weather_typhoon_check:'+str(e))
                self.result_check.list_data.append('%s |'%url_report + '| %s ������' % e)

    def typhoon_track_check(self,weather_url,sql_data):
        global url_report_time
        for a in range(len(weather_url["data"]["track"])):
            url_report_time = url_report + sql_data[a][5]
            try:
                if weather_url["data"]["track"][a]['prediction'] == sql_data[a][6]:
                    track=self.result_check.comparison_check(len(weather_url["data"]["track"][a]), 6,'| track �ֶγ���:(%s/%s)')
                    centralPressure=self.result_check.comparison_check(sql_data[a][11],weather_url["data"]["track"][a]["centralPressure"],'| centralPressure:(%s/%s)')
                    latitude=self.result_check.comparison_check(sql_data[a][8],weather_url["data"]["track"][a]["latitude"],'| latitude:(%s/%s)')
                    level=self.result_check.comparison_check(sql_data[a][9],weather_url["data"]["track"][a]["level"], '| level:(%s/%s)')
                    longitude=self.result_check.comparison_check(sql_data[a][7],weather_url["data"]["track"][a]["longitude"],'| longitude:(%s/%s)')
                    windSpeed=self.result_check.comparison_check(sql_data[a][10],weather_url["data"]["track"][a]["windSpeed"],'| windSpeed speed:(%s/%s)')
                    time_d=self.result_check.comparison_check( int(str(Data_analysis.time_disposes(sql_data[a][5])) + '000'),weather_url["data"]["track"][a]["time"],'| time:(%s/%s)')
                    typhoonId=self.result_check.comparison_check(sql_data[a][1],weather_url["data"]["typhoonId"] ,'| typhoonId:(%s/%s)')
                    typhoonNameEn=self.result_check.comparison_check( sql_data[a][2],weather_url["data"]["typhoonNameEn"],'| typhoonNameEn:(%s/%s)')
                    typhoonNameZh=self.result_check.comparison_check(sql_data[a][3],weather_url["data"]["typhoonNameZh"] ,'| typhoonNameZh:(%s/%s)')
                    typhoon_track=track+centralPressure+latitude+level+longitude+windSpeed+time_d+typhoonId+typhoonNameEn+typhoonNameZh
                    if typhoon_track != '':
                        self.result_check.list_data.append('%s |' % url_report_time + typhoon_track)
                    else:
                        print(url_report_time+'���ͨ��')
                else:
                    self.result_check.list_data.append('%s |' % url_report_time + '| %s ȱ������'%weather_url["data"]["track"][a]['prediction'])
            except Exception as e:
                self.logger.error('typhoon_track_check:'+str(e))
                self.result_check.list_data.append(url_report_time+'| %s ������'%e)


    def weather_typhoon_start(self,name):
        print('weather_typhoon_start**********************')
        self.result_check.list_data.append("**********̨���б�*********")
        self.weather_typhoon_list_check()
        self.result_check.list_data.append("**********̨������*********")
        self.test_weather_typhoon_check()
        self.result_check.wait_data_log('̨���б�/���� ��������%d' % (len(self.result_check.list_data)-2))
        self.result_check.all_wait_data()
        if Data_analysis.document_check(self.path_name) == None:
            pass
        else:
            Test_mail("[vivo]-[%s]-[����]-[��������]-[̨���б�/����]-[%d]" % (name,(len(self.result_check.list_data)-2))).smtp_on(self.path_name)
            Data_analysis.data_delete(self.path_name)
        print(self.result_check.list_data)
        self.result_check.list_data.clear()


if __name__ == '__main__':

    Test_Typhoon('guangzhou').weather_typhoon_start('����')

