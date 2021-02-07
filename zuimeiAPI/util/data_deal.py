# coding=<encoding name> ： # coding=utf-8
from util.conf_read import ConfRead
from util.testSQL import TestSQL


class DateDeal:
    def __init__(self):
        self.sql = TestSQL()

    def china_date(self):
        data = self.sql.do_sql(ConfRead.conf_get('sql.conf', 'big', 'china_sql'))
        accucode = []  # 城市编码
        cityname = []  # 城市名
        geolong = []  # 经度
        geolat = []  # 纬度

        for i in data:
            accucode.append(i[0])
            cityname.append(i[1])
            geolong.append(i[2])
            geolat.append(i[3])

        # print(accucode)
        # print(cityname)
        # print(geolong)
        # print(geolat)
        return accucode, cityname, geolong, geolat

    def china_dic_code_name(self):
        data = self.sql.do_sql(ConfRead.conf_get('sql.conf', 'big', 'china_sql'))
        dic = {}
        for i in data:
            # 键值对， 城市编码：城市名
            dic[i[0]] = i[1]
        return dic

    def china_dic_geo_name(self):
        data = self.sql.do_sql(ConfRead.conf_get('sql.conf', 'big', 'china_sql'))
        dic = {}
        for i in data:
            # 键值对， 经纬度：城市名
            dic[i[2] + '-' + i[3]] = i[1]
        return dic

    def china_dic_citycode(self):
        citycode = self.sql.do_sql(ConfRead.conf_get('sql.conf', 'big', 'china_city'))
        dic = {}
        for i in citycode:
            # 键值对， 城市码（accucode）：城市编码
            dic[i[0]] = i[0]
        return dic

    def china_dic_province(self):
        city_data = self.sql.do_sql(ConfRead.conf_get('sql.conf', 'big', 'china_city'))
        dic = {}
        for i in city_data:
            # 键值对， 城市码（accucode）：省市区
            dic[i[3]] = i[1]
        return dic

    def china_dic_timeZone(self):
        city_data = self.sql.do_sql(ConfRead.conf_get('sql.conf', 'big', 'china_city'))
        dic = {}
        for i in city_data:
            # 键值对， 城市码（accucode）：时区
            dic[i[3]] = i[2]
        return dic

    def china_dic_geo_code(self):
        geo_code = self.sql.do_sql(ConfRead.conf_get('sql.conf', 'big', 'china_city'))
        dic = {}
        for i in geo_code:
            # 键值对，经度-纬度 ： citycode
            dic[str(i[4])+str(i[5])] = i[0]
        return dic

    def china_dic_geo_province(self):
        city_province = self.sql.do_sql(ConfRead.conf_get('sql.conf', 'big', 'china_city'))
        dic = {}
        for i in city_province:
            # 键值对，经度-纬度 ： 省
            dic[str(i[4])+str(i[5])] = i[1]
        return dic

    def china_dic_geo_zone(self):
        city_province = self.sql.do_sql(ConfRead.conf_get('sql.conf', 'big', 'china_city'))
        dic = {}
        for i in city_province:
            # 键值对，经度-纬度 ： 时区
            dic[str(i[4]) + str(i[5])] = i[2]
        return dic

    def days_time_aqi_list(self):
        city_province = self.sql.do_sql(ConfRead.conf_get('sql.conf', 'big', 'no_days_time_aqi'))
        accucode_list = []
        for i in city_province:
            accucode_list.append(i[2])
        return accucode_list

    def days_time_aqi_long_list(self):
        city_province = self.sql.do_sql(ConfRead.conf_get('sql.conf', 'big', 'no_days_time_aqi'))
        long_list = []
        for i in city_province:
            long_list.append(i[7])
        return long_list

    def days_time_aqi_lat_list(self):
        city_province = self.sql.do_sql(ConfRead.conf_get('sql.conf', 'big', 'no_days_time_aqi'))
        lat_list = []
        for i in city_province:
            lat_list.append(i[8])
        return lat_list


if __name__ == '__main__':
    a = DateDeal()
    b = a.days_time_aqi_list()
    print(b)

