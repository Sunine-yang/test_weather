#-*-coding:GBK -*-
import os,sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import time
from lib.test_api import TestAPI
from analysis.url_data import Url_data
from tools.easy_mysql import EasyMysql
from tools.read_yaml import ReadYaml
from analysis.comparison_results import Result_check
from analysis.data_analysis import Data_analysis
from tools.test_html import Test_mail
class Test_Typhoon:
    def __init__(self,service):
        self.result_check=Result_check('typhoon_list_track')
        self.read_ymal=ReadYaml.read_yaml()[service]
    def weather_typhoon_list_check(self):

        global result
        try:
            data_num = Url_data().read_data('typhoon_list.txt')
            url_list = TestAPI.get_location(self.read_ymal["weather_typhoon_list"]).json()
            typhoon_list=['data','typhoonList','resultinfo',"servertime"]
            key_query=self.key_check(typhoon_list,str(url_list))
            code=self.result_check.comparison_check(TestAPI.get_location(self.read_ymal["weather_typhoon_list"]).status_code,200,'| 状态码:(%s/%s)')
            ZtyphoonList=self.result_check.comparison_check(len(url_list),4,'| ZtyphoonList 字节长度:(%s/%s)')
            typhoonList=self.result_check.comparison_check(len(url_list["data"]["typhoonList"]),5,'t| typhoonList 字节长度:(%s/%s)')
            resultinfo=self.result_check.comparison_check(url_list["resultinfo"],'OK','| resultinfo:(%s/%s)')
            servertime=self.result_check.comparison_none_check(url_list["servertime"],'| servertime:(%s)')
            resultcode=self.result_check.comparison_check(url_list["resultcode"],'0','| resultcode:(%s/%s)')
            typhoon_list_data=key_query+code+ZtyphoonList+typhoonList+resultinfo+servertime+resultcode
            if typhoon_list_data != '':
                self.result_check.list_data.append('台风列表接口 |'+ typhoon_list_data)
            else:
                pass
            for i in range(len(url_list["data"]["typhoonList"])):
                result='%s,%s |'%(url_list["data"]["typhoonList"][i]["nameZh"],'20'+url_list["data"]["typhoonList"][i]["code"])
                typhoon_lists = ['nameZh', 'nameEn', 'code', "number"]
                key_info=self.key_check(typhoon_lists, str(url_list["data"]["typhoonList"][i]))
                typhoonList_l=self.result_check.comparison_check(len(url_list["data"]["typhoonList"][i]),4,result+'| typhoonList 字节长度:(%s/%s)')
                nameZh=self.result_check.comparison_check(url_list["data"]["typhoonList"][i]["nameZh"],str(data_num[-i-1][2]),'| nameZh:(%s/%s)')
                nameEn=self.result_check.comparison_check(url_list["data"]["typhoonList"][i]["nameEn"],str(data_num[-i-1][1]),'| nameEn:(%s/%s)')
                codes=self.result_check.comparison_in_check(url_list["data"]["typhoonList"][i]["code"],str(data_num[-i-1][3]),'| code:(%s/%s)')
                number=self.result_check.comparison_none_check(url_list["data"]["typhoonList"][i]["number"],'| number:(%s)')
                typhoon_list_datas=key_info+typhoonList_l+nameEn+nameZh+codes+number
                if typhoon_list_datas != '':
                    self.result_check.list_data.append('%s,%s |'%(data_num[-i-1][2],'20'+str(data_num[-i-1][3]) + typhoon_list_datas))
                else:
                    print('正确')
        except Exception as e:
            self.result_check.list_data.append(result + '| %s 不存在' % e)
            self.result_check.logger.warning(e)
#########################################################################################################################
    def test_typhoob_list_start(self):
        print('typhoon_list  start...........................')
        Url_data().get_number_list()
        data_num=Url_data().read_data('typhoon_list.txt')
        sql_num=EasyMysql.query_all(self.read_ymal["sql_typhoon_list"])
        try:
            for i in range(len(data_num)):
                self.result_check.comparison_in_check(str(data_num[i][3]),str(sql_num[i][1]),'url_data:%s  sql_data:%s')
                self.result_check.comparison_check(data_num[i][2],sql_num[i][3],'url_data:%s  sql_data:%s')
                self.result_check.comparison_check(data_num[i][1],sql_num[i][2],'url_data:%s  sql_data:%s')
        except Exception as  e:
            self.result_check.logger.warning(str(e))


    def test_typhoon_track_time(self):
        data_num = Url_data().read_data('typhoon_list.txt')
        for i in range(0,len(data_num)):
            Url_data().get_data(data_num[i][0], data_num[i][1])
            time.sleep(5)
            url_data1 = Url_data().read_data('aqi_data/%s.txt' % data_num[i][1])
            self.test_typhoon_track(url_data1,data_num[i][1],'20'+str(data_num[i][3]))

    def test_typhoon_track(self,url_data,name,number):

        global result_data
        for a in range(0,len(url_data)):
            tiam_data=Data_analysis.time_transform(url_data[a][2])
            sql_data = EasyMysql.query_all(self.read_ymal["sql_typhoon_track_time"] % (name,tiam_data))
            try:
                if sql_data==():
                    self.result_check.list_data.append('数据库未找到台风数据:|%s,%s,%s 数据' % (number,
                        name, tiam_data))
                else:
                    result_data = '%s,%s,%s |' % (sql_data[0][1], sql_data[0][2], sql_data[0][5])
                    longitude=self.result_check.comparison_check(float(sql_data[0][7]),round(float(url_data[a][4]),1),
                                                        '| longitude:(%s/%s)')
                    latitude=self.result_check.comparison_check(float(sql_data[0][8]),round(float(url_data[a][5]),1),
                                                        '| latitude:(%s/%s)')
                    level=self.result_check.comparison_check(str(sql_data[0][9]).lower(),str(url_data[a][3]).lower(),
                                                        '| level:(%s/%s)')
                    centre_speed=self.result_check.comparison_check(int(sql_data[0][10]),Data_analysis.data_switch(url_data[a][7]),
                                                        '| centre_speed:(%s/%s)')
                    speed=self.result_check.comparison_check(int(sql_data[0][13]),Data_analysis.data_switch(url_data[a][9]),
                                                       '| speed:(%s/%s)')
                    direction=self.result_check.comparison_check(str(sql_data[0][12]), str(Data_analysis.data_switch_fx(url_data[a][8])),
                                                       '| direction:(%s/%s)')
                    centre_gas=self.result_check.comparison_check(int(sql_data[0][11]),Data_analysis.data_switch(url_data[a][6]) ,
                                                       '| centre_gas:(%s/%s)')
                    typhoon_track_result = longitude + latitude + level + str(centre_speed) + str(speed) + str(direction) + str(centre_gas)
                    if typhoon_track_result != '':
                        self.result_check.list_data.append(result_data + typhoon_track_result)
                    else:
                        print(result_data +'检验通过')
            except Exception as e:
                print(e)
                if str(e)=='tuple index out of range':
                    pass
                else:
                    self.result_check.list_data.append('%s |' % result_data + '| %s 不存在' % e)
                    self.result_check.logger.warning(e)


#########################################################################################################################
    def test_weather_typhoon_check(self):
        global url_report
        data_num = Url_data().read_data('typhoon_list.txt')
        for i in range(len(data_num)):
            Url_data().write_weather_typhoon_data(data_num[i][3])
            try:
                sql_data = EasyMysql.query_all(self.read_ymal["sql_typhoon_track"] % data_num[i][1])
                weather_url=Url_data().read_weather_typhoon_data(data_num[i][3])
                url_report = '%s,%s'%(data_num[i][1],'20'+str(data_num[i][3]))
                list_key_datas = ['data', 'track', 'changeTrender', 'endTime', 'source', 'startTime',
                                 'sustainedTime']
                key_query=self.key_check(list_key_datas,str(weather_url))
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
                typhoon_result=number+time_c+total_len+data+resultcode+resultinfo+endTime+source+startTime+sustainedTime+key_query
                if typhoon_result != '':
                    self.result_check.list_data.append('%s |'%url_report + typhoon_result)
                else:
                    print('%s |'%url_report+'检查通过')
            except Exception as e:
                self.result_check.list_data.append('%s |'%url_report + '| %s 不存在' % e)

    def typhoon_track_check(self,weather_url,sql_data):
        for a in range(len(weather_url["data"]["track"])):
            url_report_time=url_report+sql_data[a][5]
            list_key_data = [ 'track', 'changeTrender', 'time','centralPressure','latitude', 'level', 'longitude',
                              'typhoonNameZh', "typhoonNameEn", "typhoonId","windSpeed","longitude"]
            key_track=self.key_check(list_key_data,str(weather_url["data"]))
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
            typhoon_track=track+centralPressure+latitude+level+longitude+windSpeed+time_d+typhoonId+typhoonNameEn+typhoonNameZh+key_track
            if typhoon_track != '':
                self.result_check.list_data.append('%s |' % url_report_time + typhoon_track)
            else:
                print(url_report_time+'检查通过')




    def key_check(self,list_data,data):
        result_data = []
        for i in range(len(list_data)):
            if list_data[i] in data:
                pass
            else:
                result = '%s 不存在' % list_data[i]
                result_data.append(result)
        if result_data == []:
            return ''
        else:
            data = str(result_data).replace("[", ' ')
            data1 = data.replace("]", '')
            data2 = data1.replace(",", " | ")
            return data2


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
    Test_Typhoon("typhoon").typhoon_start('广州')