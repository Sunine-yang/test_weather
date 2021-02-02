#-*-coding:GBK -*-
import time
from lib.test_api import TestAPI
from tools.read_yaml import ReadYaml
import json
from path_data import Path_data
from tools.easy_mysql import EasyMysql
class Url_data:

    read_yaml=ReadYaml.read_yaml()

    def read_data(self,data):
        with open(Path_data.get_path()+'/test_data/%s'%(data),'r',encoding='utf8') as f:
            result=f.read()
            return eval(result)
    def get_data(self,data,name):
        a=0
        list_data=[]
        get_url = TestAPI.get_location(self.read_yaml["typhoon"]["baseURL"] % data).text
        url_data = get_url.strip("typhoon_jsons_view_%s("%data)
        url_data1 = url_data.strip(");")
        result = json.loads(url_data1)["typhoon"][8]
        for i in range(len(result)):
            if a ==0:
                if result[i][3]=="TD":
                    pass
                elif result[i][3] != "TD":
                    a=1
                    list_data.append(result[i])
            elif a==1:
                list_data.append(result[i])
        self.write_data(Path_data.get_path()+'/test_data/aqi_data/%s.txt' % name, str(list_data))
    def get_number_list(self):
        get_url = TestAPI.get_location(self.read_yaml["typhoon"]["baseURL_list"]).text
        url_data = get_url.strip("typhoon_jsons_list_default(")
        url_data1 = url_data.strip(");")
        result=json.loads(url_data1)["typhoonList"]
        for i in range(len(result)):
            for j in range(len(result)-i-1):
                if result[j][3]==None:
                    pass
                elif int(result[j][3])>int(result[j+1][3]):
                    result[j],result[j+1]=result[j+1],result[j]
        result.pop(0)
        self.write_data(Path_data.get_path()+'/test_data/typhoon_list.txt',str(result))

    def write_data(self,path,data):
        with open(path, 'w+', encoding='utf8') as f:
            f.write(data)
            f.close()
    def write_data_query(self,name,data):
        with open(Path_data.get_path()+'/test_data/test_log_report/%s.txt'%name, 'a+', encoding='utf8') as f:
            f.write(data)
            f.write('\n')
            f.close()


    def write_weather_typhoon_data(self,data):
        try:
            if TestAPI.get_location(self.read_yaml["typhoon"]["weather_typhoon"]%('20'+str(data))).status_code ==200:
                get_url = TestAPI.get_location(self.read_yaml["typhoon"]["weather_typhoon"]%('20'+str(data))).json()
                with open(Path_data.get_path()+'/test_data/aqi_data/%s.json'%('20'+str(data)), 'w+') as f:
                    json.dump(get_url,f)
                    f.close()
            else:
                data = "write_weather_typhoon_data: Return status code not is 200"
                Url_data().write_data_query('typhoon_track', data)
        except Exception as e:
            Url_data().write_data_query('typhoon_track', 'write_weather_typhoon_data is '+str(e))
    def read_weather_typhoon_data(self,data):
        with open(Path_data.get_path()+'/test_data/aqi_data/%s.json'%('20'+str(data)), 'r') as load_f:
            load_dict = json.load(load_f)
            return load_dict

    def wait_aqi_json(self,service):
        get_url=TestAPI.get_location(self.read_yaml["requests"][service]).json()
        with open(Path_data.get_path() + '/test_data/aqi_data/aqi.json' , 'w+') as f:
            json.dump(get_url, f)
            f.close()

    def read_aqi_json(self):
        with open(Path_data.get_path()+'/test_data/aqi_data/aqi.json', 'r') as load_f:
            load_dict = json.load(load_f)
            return load_dict

    def wait_aqi_sql_data(self,requests,city_code,data):
        sql_data=EasyMysql.query_all(self.read_yaml[requests][city_code])
        with open(Path_data.get_path()+'/test_data/sql_data/%s.txt'%data,'w+',encoding='utf8') as f:
            f.write(str(sql_data))
            f.close()

    def read_sql_data(self,data):
        with open(Path_data.get_path()+'/test_data/sql_data/%s.txt'%data,'r',encoding='utf8') as f:
            result=f.read()
            return eval(result)

    def wait_big_sql_data(self,services,city_code,num1,num2):
        sql_data=EasyMysql.query_all(self.read_yaml[services][city_code]%(num1,num2))
        with open(Path_data.get_path()+'/test_data/sql_data/%s.txt'%str(num2),'w+',encoding='utf8') as f:
            f.write(str(sql_data))
            f.close()




if __name__ == '__main__':
    Url_data().wait_aqi_sql_data()
    print(Url_data().read_sql_data()[0])

