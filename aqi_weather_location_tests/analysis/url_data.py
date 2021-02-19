#-*-coding:GBK -*-
import time,json
from lib.test_api import TestAPI
from tools.read_yaml import ReadYaml
from tools.write_data_txt import Write_Data_txt
class Url_data:
    def __init__(self,sercice):

        self.txt=Write_Data_txt
        self.sercice=sercice
        self.read_yaml = ReadYaml.read_yaml(self.sercice)[self.sercice]
    def get_data(self,data):
        a=0
        list_data=[]
        get_url = TestAPI.get_location(self.read_yaml["atmosphere_track"] % data).text
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
        get_url_2020 = TestAPI.get_location(self.read_yaml["atmosphere_list"]%2020).text
        url_data = get_url_2020.strip('typhoon_jsons_list_%s('%2020)
        get_data = url_data.strip(");")
        get_url_2021 = TestAPI.get_location(self.read_yaml["atmosphere_list"]%2021).text
        url_data1 = get_url_2021.strip('typhoon_jsons_list_%s('%2021)
        get_data1 = url_data1.strip(");")
        list_data=json.loads(get_data)["typhoonList"]
        for i in range(len(json.loads(get_data1)["typhoonList"])):
            list_data.append(json.loads(get_data1)["typhoonList"][i])

        for i in range(len(list_data)):
            for j in range(len(list_data)-i-1):
                if list_data[j][3]==None:
                    pass
                elif int(list_data[j][3])>int(list_data[j+1][3]):
                    list_data[j],list_data[j+1]=list_data[j+1],list_data[j]
        list_data.pop(0)
        self.txt.write_data('aqi_data/typhoon_list','w+',str(list_data))











if __name__ == '__main__':
    Url_data('guangzhou').get_number_list()


