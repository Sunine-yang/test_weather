#-*-coding:GBK -*-
import os,sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from analysis.url_data import Url_data
from tools.easy_mysql import EasyMysql
from tools.read_yaml import ReadYaml
from analysis.comparison_results import Result_check
from analysis.data_analysis import Data_analysis
from tools.test_html import Test_mail
from tools.write_read_json import Write_Read_Json
from tools.write_data_txt import Write_Data_txt
from tools.logger import Logger
class Test_CNTyphoon:
    def __init__(self,services):
        self.services = services
        self.json=Write_Read_Json
        self.path_name=services+'_cn_typhoon_list_track'
        self.result_check=Result_check(self.path_name)
        self.read_ymal=ReadYaml.read_yaml(self.services)[self.services]
        self.txt=Write_Data_txt
        self.logger=Logger.report_logger()
    def test_typhoob_list_start(self):
        print('typhoon_list  start...........................')
        Url_data(self.services).get_number_list()
        data_num=eval(self.txt.read_data('/aqi_data/typhoon_list'))
        sql_num=EasyMysql(self.services).query_all(self.read_ymal["typhoon_list_sql"])
        try:
            for i in range(len(data_num)):
                self.result_check.comparison_in_check(str(sql_num[i][1]),str(data_num[i][3]),'sql_data:%s  url_data:%s ')
                self.result_check.comparison_check(sql_num[i][3],data_num[i][2],'sql_data:%s  url_data:%s ')
                self.result_check.comparison_check(sql_num[i][2],data_num[i][1],'sql_data:%s  url_data:%s ')
        except Exception as  e:
            self.result_check.list_data.append('test_typhoob_list_start'+str(e))
            self.logger.error('test_typhoob_list_start'+str(e))
    def test_typhoon_track_time(self):
        global result_data
        data_num=eval(self.txt.read_data('aqi_data/typhoon_list'))
        for i in range(len(data_num)):
            Url_data(self.services).get_data(data_num[i][0])
            sql_datas=EasyMysql(self.services).query_all(self.read_ymal["typhoon_track_sql"]%data_num[i][1])
            self.txt.write_data('sql_data/%s' % data_num[i][1],'w+',str(sql_datas))

            url_data = eval(self.txt.read_data('aqi_data/%s' % data_num[i][1]))
            sql_data = eval(self.txt.read_data('sql_data/%s' % data_num[i][1]))
            result_data = '20%s,%s,%s |' % (url_data[3], url_data[2], url_data[1])
            for a in range(0, len(url_data[8])):
                tiam_data = Data_analysis.time_transform(url_data[8][a][2])
                report=self.result_check.comparison_not_in_check(tiam_data, str(sql_data) , '| %s 数据缺失' )
                if report=='':
                    pass
                else:
                    self.result_check.list_data.append(result_data+report)
                try:
                    for k in range(len(sql_data)):
                        if tiam_data ==sql_data[k][5]:
                            longitude = self.result_check.comparison_check(float(sql_data[k][7]),round(float(url_data[8][a][4]), 1),'| longitude:(%s/%s)')
                            latitude = self.result_check.comparison_check(float(sql_data[k][8]),round(float(url_data[8][a][5]), 1),'| latitude:(%s/%s)')
                            level = self.result_check.comparison_check(str(sql_data[k][9]).lower(),str(url_data[8][a][3]).lower(), '| level:(%s/%s)')
                            centre_speed = self.result_check.comparison_check(int(sql_data[k][10]),Data_analysis.data_switch(url_data[8][a][7]),'| centre_speed:(%s/%s)')
                            speed = self.result_check.comparison_check(int(sql_data[k][13]), Data_analysis.data_switch(url_data[8][a][9]),'| speed:(%s/%s)')
                            direction = self.result_check.comparison_check(str(sql_data[k][12]), str( Data_analysis.data_switch_fx(url_data[8][a][8])), '| direction:(%s/%s)')
                            centre_gas = self.result_check.comparison_check(int(sql_data[k][11]), Data_analysis.data_switch(url_data[8][a][6]),'| centre_gas:(%s/%s)')
                            typhoon_track_result = longitude + latitude + level + centre_speed + speed + direction + centre_gas
                            if typhoon_track_result != '':

                                self.result_check.list_data.append(result_data + "| %s"%tiam_data+typhoon_track_result)
                            else:
                                print(result_data +tiam_data+ ' 检验通过')
                        else:
                            pass
                except Exception as  e:
                    self.result_check.list_data.append(result_data+str(e))
                    self.logger.error('test_typhoon_track_time:'+str(e))



    def cnscene_typhoon_start(self,name):
        self.result_check.list_data.append("**********台风列表*********")
        self.test_typhoob_list_start()
        self.result_check.list_data.append("**********台风详情*********")
        self.test_typhoon_track_time()
        self.result_check.wait_data_log('台风列表/详情 错误数：%d' % (len(self.result_check.list_data) - 2))
        self.result_check.all_wait_data()
        if Data_analysis.document_check(self.path_name) == None:
            pass
        else:
            Test_mail("[vivo]-[%s]-[数据]-[中国气象]-[台风列表/详情]-[%d]" % (name, (len(self.result_check.list_data) - 2)),
                      self.path_name).smtp_on()
            Data_analysis.data_delete(self.path_name)
        print(self.result_check.list_data)
        self.result_check.list_data.clear()


if __name__ == '__main__':
    Test_CNTyphoon('guangzhou').cnscene_typhoon_start('广州')