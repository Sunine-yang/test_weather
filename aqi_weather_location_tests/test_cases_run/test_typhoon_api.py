#-*-coding:GBK -*-
import os,sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from lib.test_api import TestAPI
from analysis.url_data import Url_data
from tools.easy_mysql import EasyMysql
from tools.read_yaml import ReadYaml
from analysis.comparison_results import Result_check
from analysis.data_analysis import Data_analysis
from tools.test_html import Test_mail
from tools.write_read_json import Write_Read_Json
from tools.write_data_txt import Write_Data_txt
class Test_Typhoon:
    def __init__(self,services):
        self.services = services
        self.json=Write_Read_Json
        self.result_check=Result_check('typhoon_list_track')
        self.read_ymal=ReadYaml.read_yaml(self.services)[self.services]
        self.txt=Write_Data_txt
    def weather_typhoon_list_check(self):

        global result
        result= '台风列表接口 |'
        data_num=eval(self.txt.read_data('/aqi_data/typhoon_list'))
        url_list = TestAPI.get_location(self.read_ymal['typhoon_list_url']).json()
        code=self.result_check.comparison_check(TestAPI.get_location(self.read_ymal['typhoon_list_url']).status_code,200,'| 状态码:(%s/%s)')
        ZtyphoonList=self.result_check.comparison_check(len(url_list),4,'| ZtyphoonList 字节长度:(%s/%s)')
        typhoonList=self.result_check.comparison_check(len(url_list["data"]["typhoonList"]),5,'t| typhoonList 字节长度:(%s/%s)')
        resultinfo=self.result_check.comparison_check(url_list["resultinfo"],'OK','| resultinfo:(%s/%s)')
        servertime=self.result_check.comparison_none_check(url_list["servertime"],'| servertime:(%s)')
        resultcode=self.result_check.comparison_check(url_list["resultcode"],'0','| resultcode:(%s/%s)')
        typhoon_list_data=code+ZtyphoonList+typhoonList+resultinfo+servertime+resultcode
        if typhoon_list_data != '':
            self.result_check.list_data.append('台风列表接口 |'+ typhoon_list_data)
        else:
            pass
        for i in range(len(url_list["data"]["typhoonList"])):
            try:

                typhoonList_l=self.result_check.comparison_check(len(url_list["data"]["typhoonList"][i]),4,result+'| typhoonList 字节长度:(%s/%s)')
                nameZh=self.result_check.comparison_check(url_list["data"]["typhoonList"][i]["nameZh"],str(data_num[-i-1][2]),'| nameZh:(%s/%s)')
                nameEn=self.result_check.comparison_check(url_list["data"]["typhoonList"][i]["nameEn"],str(data_num[-i-1][1]),'| nameEn:(%s/%s)')
                codes=self.result_check.comparison_in_check(url_list["data"]["typhoonList"][i]["code"],str(data_num[-i-1][3]),'| code:(%s/%s)')
                number=self.result_check.comparison_none_check(url_list["data"]["typhoonList"][i]["number"],'| number:(%s)')
                typhoon_list_datas=typhoonList_l+nameEn+nameZh+codes+number
                if typhoon_list_datas != '':
                    self.result_check.list_data.append('%s,%s |'%(data_num[-i-1][2],'20'+str(data_num[-i-1][3]) + typhoon_list_datas))
                else:
                    print(result +url_list["data"]["typhoonList"][i]["nameZh"]+'| 检测正确')
            except Exception as e:
                self.result_check.list_data.append(result + '| %s 不存在' % e)



#########################################################################################################################
    def test_typhoob_list_start(self):
        print('typhoon_list  start...........................')
        Url_data(self.services).get_number_list()
        data_num=eval(self.txt.read_data('/aqi_data/typhoon_list'))
        sql_num=EasyMysql(self.services).query_all(self.read_ymal["typhoon_list_sql"])
        try:
            for i in range(len(data_num)):
                self.result_check.comparison_in_check(str(data_num[i][3]),str(sql_num[i][1]),'url_data:%s  sql_data:%s')
                self.result_check.comparison_check(data_num[i][2],sql_num[i][3],'url_data:%s  sql_data:%s')
                self.result_check.comparison_check(data_num[i][1],sql_num[i][2],'url_data:%s  sql_data:%s')
        except Exception as  e:
            self.result_check.logger.warning(str(e))


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
                    print(e)

#########################################################################################################################
    def test_weather_typhoon_check(self):
        global url_report
        data_num=eval(self.txt.read_data('aqi_data/typhoon_list'))
        for i in range(len(data_num)):
            get_url = TestAPI.get_location(self.read_ymal['typhoon_track_url'] % ('20' + str(data_num[i][3]))).json()
            self.json.write_json('/aqi_data/20%s'%data_num[i][3],get_url)
            try:
                sql_data = EasyMysql(self.services).query_all(self.read_ymal["typhoon_track_sql"] % data_num[i][1])
                weather_url=self.json.read_json('aqi_data/%s'%('20'+str(data_num[i][3])))
                url_report = '%s,%s'%(data_num[i][1],'20'+str(data_num[i][3]))
                number=self.result_check.comparison_check(len(weather_url["data"]["track"]), len(sql_data),
                                                   '| 数据条数:(%d/%d)')
                time_c=self.result_check.comparison_check(weather_url["data"]["changeTrender"][0]["time"],int(str(Data_analysis.time_disposes(sql_data[0][5]))+'000'),
                                                   '| 起编时间:(%s/%s)')
                total_len=self.result_check.comparison_check(len(weather_url),4,
                                                   '| 总字段长度:(%s/%s)')
                data=self.result_check.comparison_check(len(weather_url["data"]),10,
                                                   '| data 字段长度:(%s/%s)')
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
                    print('%s |'%url_report+'检查通过')
            except Exception as e:
                self.result_check.list_data.append('%s |'%url_report + '| %s 不存在' % e)

    def typhoon_track_check(self,weather_url,sql_data):
        global url_report_time
        for a in range(len(weather_url["data"]["track"])):
            try:
                url_report_time=url_report+sql_data[a][5]
                track=self.result_check.comparison_check(len(weather_url["data"]["track"][a]), 6,'| track 字段长度:(%s/%s)')
                centralPressure=self.result_check.comparison_check(weather_url["data"]["track"][a]["centralPressure"],sql_data[a][11],'| centralPressure:(%s/%s)')
                latitude=self.result_check.comparison_check(weather_url["data"]["track"][a]["latitude"],sql_data[a][8],'| latitude:(%s/%s)')
                level=self.result_check.comparison_check(weather_url["data"]["track"][a]["level"],sql_data[a][9], '| level:(%s/%s)')
                longitude=self.result_check.comparison_check(weather_url["data"]["track"][a]["longitude"],sql_data[a][7],'| longitude:(%s/%s)')
                windSpeed=self.result_check.comparison_check(weather_url["data"]["track"][a]["windSpeed"],sql_data[a][10],'| windSpeed speed:(%s/%s)')
                time_d=self.result_check.comparison_check(weather_url["data"]["track"][a]["time"], int(str(Data_analysis.time_disposes(sql_data[a][5])) + '000'),'| time:(%s/%s)')
                typhoonId=self.result_check.comparison_check(weather_url["data"]["typhoonId"], sql_data[a][1],'| typhoonId:(%s/%s)')
                typhoonNameEn=self.result_check.comparison_check(weather_url["data"]["typhoonNameEn"], sql_data[a][2],'| typhoonNameEn:(%s/%s)')
                typhoonNameZh=self.result_check.comparison_check(weather_url["data"]["typhoonNameZh"], sql_data[a][3],'| typhoonNameZh:(%s/%s)')
                typhoon_track=track+centralPressure+latitude+level+longitude+windSpeed+time_d+typhoonId+typhoonNameEn+typhoonNameZh
                if typhoon_track != '':
                    self.result_check.list_data.append('%s |' % url_report_time + typhoon_track)
                else:
                    print(url_report_time+'检查通过')
            except Exception as e:
                self.result_check.list_data.append(url_report_time+'| %s 不存在'%e)

    def typhoon_start(self,name):
        self.result_check.list_data.append("**********中国气象*********")
        self.test_typhoob_list_start()

        self.test_typhoon_track_time()
        self.result_check.list_data.append("**********最美天气*********")
        self.weather_typhoon_list_check()
        self.test_weather_typhoon_check()
        self.result_check.wait_data_log('台风列表/详情 错误数：%d' % (len(self.result_check.list_data)-2))
        self.result_check.all_wait_data()
        if Data_analysis.document_check('typhoon_list_track') == None:
            pass
        else:
            Test_mail("[vivo]-[%s]-[数据]-[台风列表/详情]-[%d]" % (name,(len(self.result_check.list_data)-2)), 'typhoon_list_track').smtp_on()
            Data_analysis.data_delete('typhoon_list_track')
        self.result_check.list_data.clear()




if __name__ == '__main__':
    # Test_Typhoon("weather_typhoon_list",'weather_typhoon').typhoon_start('广州')
    Test_Typhoon('guangzhou').typhoon_start('广州')

