#-*-coding:GBK -*-
import time,json
from lib.test_api import TestAPI
from tools.read_yaml import ReadYaml
from tools.write_data_txt import Write_Data_txt
from path_data import Path_data
from tools.easy_mysql import EasyMysql
class Url_data:
    def __init__(self):
        self.read_yaml=ReadYaml.read_yaml()
        self.txt=Write_Data_txt

    def get_data(self,data):
        a=0
        list_data=[]
        get_url = TestAPI.get_location(self.read_yaml["typhoon"]["baseURL"] % data).text
        url_data = get_url.strip("typhoon_jsons_view_%s("%data)
        url_data1 = url_data.strip(");")
        result = json.loads(url_data1)["typhoon"]
        for i in range(len(result[8])):
            if a ==0:
                if result[8][i][3]=="TD":
                    pass
                elif result[8][i][3] != "TD":
                    a=1
                    list_data.append(result[8][i])
            elif a==1:
                list_data.append(result[8][i])
        result[8]=list_data
        self.txt.write_data('aqi_data/%s'%result[1],'w+',str(result))

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
        self.txt.write_data('aqi_data/typhoon_list','w+',str(result))










if __name__ == '__main__':
    Url_data().get_number_list()


