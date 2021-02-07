# coding=<encoding name> ： # coding=utf-8

from common.configHTTP import RunMain
from getpathInfo import text_Path
from testcase.big.big_alarm import big_alarm_case
from testcase.big.big_aqi import big_aqi_case
from testcase.big.big_aqidays import big_aqidays_case
from testcase.big.big_base import big_base_case
from testcase.big.big_condition import big_condition_case
from testcase.big.big_dailys import big_dailys_case
from testcase.big.big_erro import big_erro_case
from testcase.big.big_hourlys import big_hourlys_case
from testcase.big.big_hourlysAqi import big_hourlysAqi_case
from util.conf_read import ConfRead
from util.data_deal import DateDeal


class MinBig:
    def __init__(self, path=text_Path(), url_data='139.159.198.98'):
        datedeal = DateDeal()
        self.text_aaa = path
        self.days_time_aqi_list = datedeal.days_time_aqi_list()
        self.url = url_data

    def min_code_to_name(self, accucode, cityname):
        # 只需关注城市编码和经纬度，其他参数不需要关注
        erro_num = 0
        big_api = f'http://{self.url}/pubDataServer/getweatherpub?apikey={ConfRead.conf_key()}&language=zh_CNchl=&codeType=1'
        params = {'citycode': accucode}
        # 发送GET请求
        result, time_out = RunMain().run_main('GET', big_api, params)
        # 拿JSON
        data = result.json()
        if time_out == 2:
            erro_num += 1
            with open(self.text_aaa + "min_big_erro.txt", mode='w+', encoding='utf-8') as f:
                f.write(
                    f"[{accucode} / {cityname}] - " + '响应超时' + "\n")
        # 接口是否有返回
        er1, er2 = big_erro_case(data, time_out, result.status_code, data)
        if er1 != '' or er2 != '':
            erro_num += 1
            erro_da = ''
            if er1 != '':
                erro_da = er1
            if er2 != '':
                erro_da = erro_da + ',' + er2
            with open(self.text_aaa + "min_big_erro.txt", mode='w+', encoding='utf-8') as f:
                f.write(
                    f"[{accucode} / {cityname}] - " + erro_da + "\n")
        else:
            pass

        # 城市信息
        base_re1, base_re2, base_re3, base_re4 = big_base_case(accucode, data)
        if base_re1 != '' or base_re2 != '' or base_re3 != '' or base_re4 != '':
            erro_num += 1
            str_base = ''
            if base_re1 != '':
                str_base = base_re1
            if base_re2 != '':
                str_base = str_base + ',' + base_re2
            if base_re3 != '':
                str_base = str_base + ',' + base_re3
            if base_re4 != '':
                str_base = str_base + ',' + base_re4
            with open(self.text_aaa + "min_big_base.txt", mode='w+', encoding='utf-8') as f:
                f.write(
                    f"[{accucode} / {cityname}] - " + str_base + "\n")
        else:
            pass

        # 实况天气
        con_re1, con_re2, con_re3, con_re4 = big_condition_case(data)
        if con_re1 != '' or con_re2 != '' or con_re3 != '' or con_re4 != '':
            erro_num += 1
            str_condition = ''
            if con_re1 != '':
                str_condition = con_re1
            if con_re2 != '':
                str_condition = str_condition + ',' + con_re2
            if con_re3 != '':
                str_condition = str_condition + ',' + con_re3
            if con_re4 != '':
                str_condition = str_condition + ',' + con_re4
            with open(self.text_aaa + "min_big_condition.txt", mode='w+', encoding='utf-8') as f:
                f.write(
                    f"[{accucode} / {cityname}] - " + str_condition + "\n")

        else:
            pass

        # 多天预报
        dailys_re1, dailys_re2, dailys_re3, dailys_re4, dailys_re5, dailys_re6, dailys_re7, dailys_re8, dailys_re9, dailys_re10, dailys_re11 = big_dailys_case(
            data)
        if dailys_re1 != '' or dailys_re2 != '' or dailys_re3 != '' or dailys_re4 != '' or dailys_re5 != '' or dailys_re6 != '' or dailys_re7 != '' or dailys_re8 != '' or dailys_re9 != '' or dailys_re10 != '' or dailys_re11 != '':
            erro_num += 1
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
            if dailys_re11 != '':
                str_dailys = str_dailys + ',' + dailys_re11
            with open(self.text_aaa + "min_big_dailys.txt", mode='w+', encoding='utf-8') as f:
                f.write(
                    f"[{accucode} / {cityname}] - " + str_dailys + "\n")
        else:
            pass

        # 多天空气质量
        if accucode not in self.days_time_aqi_list:
            ad_re1, ad_re2, ad_re3, ad_re4, ad_re5, ad_re6 = big_aqidays_case(data)
            if ad_re1 != '' or ad_re2 != '' or ad_re3 != '' or ad_re4 != '' or ad_re5 != '' or ad_re6 != '':
                erro_num += 1
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
                with open(self.text_aaa + "min_big_aqidays.txt", mode='w+', encoding='utf-8') as f:
                    f.write(
                        f"[{accucode} / {cityname}] - " + str_aqidays + "\n")
            else:
                pass
        else:
            print(f'{accucode}不支持多天空气质量')

        # 实时空气质量
        aqi_r1, aqi_r2, aqi_r3, aqi_r4, aqi_r5, aqi_r6 = big_aqi_case(data)
        if aqi_r1 != '' or aqi_r2 != '' or aqi_r3 != '' or aqi_r4 != '' or aqi_r5 != '' or aqi_r6 != '':
            erro_num += 1
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
            if aqi_r6 != '':
                str_aqi = str_aqi + ',' + aqi_r6

            with open(self.text_aaa + "min_big_aqi.txt", mode='w+', encoding='utf-8') as f:
                f.write(
                    f"[{accucode} / {cityname}] - " + str_aqi + "\n")
        else:
            pass

        # 预警
        alarm_re1, alarm_re2 = big_alarm_case(data)
        if alarm_re1 != '' or alarm_re2 != '':
            erro_num += 1
            str_alarm = ''
            if alarm_re1 != '':
                str_alarm = alarm_re1
            if alarm_re2 != '':
                str_alarm = str_alarm + ',' + alarm_re2
            with open(self.text_aaa + "min_big_alarm.txt", mode='w+', encoding='utf-8') as f:
                f.write(
                    f"[{accucode} / {cityname}] - " + str_alarm + "\n")
        else:
            pass

        # 小时天气

        h_r1, h_r2, h_r3, h_r4 = big_hourlys_case(data)
        if h_r1 != '' or h_r2 != '' or h_r3 != '' or h_r4 != '':
            erro_num += 1
            str_hourlys = ''
            if h_r1 != '':
                str_hourlys = h_r1
            if h_r2 != '':
                str_hourlys = str_hourlys + ',' + h_r2
            if h_r3 != '':
                str_hourlys = str_hourlys + ',' + h_r3
            if h_r4 != '':
                str_hourlys = str_hourlys + ',' + h_r4
            with open(self.text_aaa + "min_big_hourlys.txt", mode='w+', encoding='utf-8') as f:
                f.write(
                    f"[{accucode} / {cityname}] - " + str_hourlys + "\n")
        else:
            pass

        # 小时空气质量
        if accucode not in self.days_time_aqi_list:
            ha1, ha2, ha3, ha4, ha5, ha6 = big_hourlysAqi_case(data)
            if ha1 != '' or ha2 != '' or ha3 != '' or ha4 != '' or ha5 != '' or ha6 != '':
                erro_num += 1
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
                with open(self.text_aaa + "min_big_houraqi.txt", mode='w+', encoding='utf-8') as f:
                    f.write(
                        f"[{accucode} / {cityname}] - " + str_houraqi + "\n")
        else:
            print(f'{accucode}不支持小时空气质量')

        if erro_num >= 1:
            with open(self.text_aaa + "min_big_erro_citynum.txt", mode='a+', encoding='utf-8') as f:
                f.write(
                    f"{erro_num}" + "\n")
            return 1
        else:
            return 2


if __name__ == '__main__':
    a = MinBig()
    b = a.min_code_to_name('58689', '蠡县')
    print(b)
