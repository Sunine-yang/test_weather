# coding=<encoding name> ： # coding=utf-8

import time

from common.configHTTP import RunMain
from getpathInfo import text_Path
from log.Log import logger
from testcase.big.big_alarm import big_alarm_case
from testcase.big.big_aqi import big_aqi_case
from testcase.big.big_aqidays import big_aqidays_case
from testcase.big.big_condition import big_condition_case
from testcase.big.big_dailys import big_dailys_case
from testcase.big.big_erro import big_erro_case
from testcase.big.big_hourlys import big_hourlys_case
from testcase.big.big_hourlysAqi import big_hourlysAqi_case
from testcase.geo.geo_base import geo_base_case

from util.conf_read import ConfRead
from util.data_deal import DateDeal
from util.fast import do_fast

logger = logger


class Geo:
    def __init__(self):
        datedeal = DateDeal()
        # self.code_to_name_dic = datedeal.china_dic_code_name()
        # self.geo_to_name_dic = datedeal.china_dic_geo_name()
        # self.citycode_dic = datedeal.china_dic_citycode()
        # self.province_dic = datedeal.china_dic_province()
        # self.timeZone_dic = datedeal.china_dic_timeZone()
        # self.geo_code = datedeal.china_dic_geo_code()
        # self.geo_province = datedeal.china_dic_geo_province()
        # self.geo_zone = datedeal.china_dic_geo_zone()
        # self.text_aaa = text_Path()
        # self.days_time_aqi_list = datedeal.days_time_aqi_list()
        self.days_time_aqi_long_list = datedeal.days_time_aqi_long_list()
        self.days_time_aqi_lat_list = datedeal.days_time_aqi_lat_list()
        self.text_aaa = text_Path()
        self.days_time_aqi_list = datedeal.days_time_aqi_list()

    # 经纬度校验城市名称
    # 经纬度 接口校验 ok or server error!
    def geo_to_name(self, long, lat, cityname):
        erro_city_num = 0
        # 只需关注城市编码和经纬度，其他参数不需要关注

        big_api = f'http://139.159.198.98/pubDataServer/getweatherpub?apikey={ConfRead.conf_key()}&language=zh_CNchl=&codeType=1'
        params = {'lon': long, 'lat': lat}
        # 发送GET请求
        result = RunMain().run_main('GET', big_api, params)
        # 拿JSON
        data = result.json()

        # 接口是否有返回
        erro_re = big_erro_case(data)
        if erro_re != '':
            erro_city_num += 1
            with open(self.text_aaa + "geo_erro.txt", mode='a+', encoding='utf-8') as f:
                f.write(
                    f"[{long}-{lat} / {cityname}] - " + erro_re + "\n")
        else:
            pass

        # 城市信息
        base_re1, base_re2, base_re3, base_re4 = geo_base_case(long, lat, data)
        if base_re1 or base_re2 or base_re3 or base_re4 != '':
            erro_city_num += 1
            str_base = ''
            if base_re1 != '':
                str_base = base_re1
            if base_re2 != '':
                str_base = str_base + ',' + base_re2
            if base_re3 != '':
                str_base = str_base + ',' + base_re3
            if base_re4 != '':
                str_base = str_base + ',' + base_re4

            with open(self.text_aaa + "geo_base.txt", mode='a+', encoding='utf-8') as f:
                f.write(
                    f"[{long}-{lat} / {cityname}] - " + str_base + "\n")
        else:
            pass

        # 实况天气
        con_re1, con_re2, con_re3, con_re4 = big_condition_case(data)
        if con_re1 or con_re2 or con_re3 or con_re4 != '':
            erro_city_num += 1
            str_condition = ''
            if con_re1 != '':
                str_condition = con_re1
            if con_re2 != '':
                str_condition = str_condition + ',' + con_re2
            if con_re3 != '':
                str_condition = str_condition + ',' + con_re3
            if con_re4 != '':
                str_condition = str_condition + ',' + con_re4

            with open(self.text_aaa + "geo_condition.txt", mode='a+', encoding='utf-8') as f:
                f.write(
                    f"[{long}-{lat} / {cityname}] - " + str_condition + "\n")

        else:
            pass

        # 多天预报
        dailys_re1, dailys_re2, dailys_re3, dailys_re4, dailys_re5, dailys_re6, dailys_re7, dailys_re8, dailys_re9, dailys_re10 = big_dailys_case(
            data)
        if dailys_re1 or dailys_re2 or dailys_re3 or dailys_re4 or dailys_re5 or dailys_re6 or dailys_re7 or dailys_re8 or dailys_re9 or dailys_re10 != '':
            erro_city_num += 1
            str_dailys = ''
            if dailys_re1 != '':
                str_dailys = dailys_re1
            if dailys_re2 != '':
                str_dailys = str_dailys + ',' + dailys_re2
            if dailys_re3 != '':
                str_dailys = str_dailys + ',' + dailys_re3
            if dailys_re4 != '':
                str_dailys = str_dailys + ',' + dailys_re4
            if dailys_re5 != '':
                str_dailys = str_dailys + ',' + dailys_re5
            if dailys_re6 != '':
                str_dailys = str_dailys + ',' + dailys_re6
            if dailys_re7 != '':
                str_dailys = str_dailys + ',' + dailys_re7
            if dailys_re8 != '':
                str_dailys = str_dailys + ',' + dailys_re8
            if dailys_re9 != '':
                str_dailys = str_dailys + ',' + dailys_re9
            if dailys_re10 != '':
                str_dailys = str_dailys + ',' + dailys_re10

            with open(self.text_aaa + "geo_dailys.txt", mode='a+', encoding='utf-8') as f:
                f.write(
                    f"[{long}-{lat} / {cityname}] - " + str_dailys + "\n")
        else:
            pass

        # 多天空气质量
        if long not in self.days_time_aqi_long_list and lat not in self.days_time_aqi_lat_list:
            ad_re1, ad_re2, ad_re3, ad_re4, ad_re5, ad_re6 = big_aqidays_case(data)
            if ad_re1 or ad_re2 or ad_re3 or ad_re4 or ad_re5 or ad_re6 != '':
                erro_city_num += 1
                str_aqidays = ''
                if ad_re1 != '':
                    str_aqidays = con_re1
                if ad_re2 != '':
                    str_aqidays = str_aqidays + ',' + ad_re2
                if ad_re3 != '':
                    str_aqidays = str_aqidays + ',' + ad_re3
                if ad_re4 != '':
                    str_aqidays = str_aqidays + ',' + ad_re4
                if ad_re5 != '':
                    str_aqidays = str_aqidays + ',' + ad_re5
                if ad_re6 != '':
                    str_aqidays = str_aqidays + ',' + ad_re6

                with open(self.text_aaa + "geo_aqidays.txt", mode='a+', encoding='utf-8') as f:
                    f.write(
                        f"[{long}-{lat} / {cityname}] - " + str_aqidays + "\n")
            else:
                pass
        else:
            print(f'不支持多天空气质量')

        # 实时空气质量
        aqi_r1, aqi_r2, aqi_r3, aqi_r4, aqi_r5 = big_aqi_case(data)
        if aqi_r1 or aqi_r2 or aqi_r3 or aqi_r4 or aqi_r5 != '':
            erro_city_num += 1
            str_aqi = ''
            if aqi_r1 != '':
                str_aqi = aqi_r1
            if aqi_r2 != '':
                str_aqi = str_aqi + ',' + aqi_r2
            if aqi_r3 != '':
                str_aqi = str_aqi + ',' + aqi_r3
            if aqi_r4 != '':
                str_aqi = str_aqi + ',' + aqi_r4
            if aqi_r5 != '':
                str_aqi = str_aqi + ',' + aqi_r5

            with open(self.text_aaa + "geo_aqi.txt", mode='a+', encoding='utf-8') as f:
                f.write(
                    f"[{long}-{lat} / {cityname}] - " + str_aqi + "\n")
        else:
            pass

        # 预警
        alarm_re1, alarm_re2 = big_alarm_case(data)
        if alarm_re1 or alarm_re2 != '':
            erro_city_num += 1
            str_alarm = ''
            if alarm_re1 != '':
                str_alarm = alarm_re1
            if alarm_re2 != '':
                str_alarm = str_alarm + ',' + alarm_re2

            with open(self.text_aaa + "geo_alarm.txt", mode='a+', encoding='utf-8') as f:
                f.write(
                    f"[{long}-{lat} / {cityname}] - " + str_alarm + "\n")
        else:
            pass

        # 小时天气

        h_r1, h_r2, h_r3, h_r4 = big_hourlys_case(data)
        if h_r1 or h_r2 or h_r3 or h_r4 != '':
            erro_city_num += 1
            str_hourlys = ''
            if h_r1 != '':
                str_hourlys = h_r1
            if h_r2 != '':
                str_hourlys = str_hourlys + ',' + h_r2
            if h_r3 != '':
                str_hourlys = str_hourlys + ',' + h_r3
            if h_r4 != '':
                str_hourlys = str_hourlys + ',' + h_r4

            with open(self.text_aaa + "geo_hourlys.txt", mode='a+', encoding='utf-8') as f:
                f.write(
                    f"[{long}-{lat} / {cityname}] - " + str_hourlys + "\n")
        else:
            pass

        # 小时空气质量
        if long not in self.days_time_aqi_long_list and lat not in self.days_time_aqi_lat_list:
            ha1, ha2, ha3, ha4, ha5, ha6 = big_hourlysAqi_case(data)
            if ha1 or ha2 or ha3 or ha4 or ha5 or ha6 != '':
                erro_city_num += 1
                str_houraqi = ''
                if ha1 != '':
                    str_houraqi = ha1
                if ha2 != '':
                    str_houraqi = str_houraqi + ',' + ha2
                if ha3 != '':
                    str_houraqi = str_houraqi + ',' + ha3
                if ha4 != '':
                    str_houraqi = str_houraqi + ',' + ha4
                if ha5 != '':
                    str_houraqi = str_houraqi + ',' + ha5
                if ha6 != '':
                    str_houraqi = str_houraqi + ',' + ha6
                with open(self.text_aaa + "geo_houraqi.txt", mode='a+', encoding='utf-8') as f:
                    f.write(
                        f"[{long}-{lat} / {cityname}] - " + str_houraqi + "\n")
        else:
            print(f'不支持小时空气质量')

        if erro_city_num >= 1:
            with open(self.text_aaa + "geo_erro_citynum.txt", mode='a+', encoding='utf-8') as f:
                f.write(
                    f"{erro_city_num}" + "\n")

if __name__ == '__main__':
    a = Geo()
    # 拿数据
    datedeal = DateDeal()
    # 拿 城市编码 ，城市名称， 经度， 纬度
    accucode, cityname, geolong, geolat = datedeal.china_date()

    print('------------------    开始执行    -----------------------')
    start_time = time.time()
    # do_fast(a.code_to_name, accucode)
    do_fast(a.geo_to_name, geolong, geolat, cityname)
    # a.code_to_name(1921951)
    # a.geo_to_name('89.180437', '44.000497')
    end_time = time.time()
    print(f'大颗粒接口中国城市执行完毕，耗时：{end_time - start_time}')
    print('------------------    执行结束    -----------------------')
    print(f'------------------    共耗时{end_time - start_time}    -----------------------')
