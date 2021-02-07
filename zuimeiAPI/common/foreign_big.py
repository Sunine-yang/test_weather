# coding=<encoding name> ： # coding=UTF-8
import time
from common.configHTTP import RunMain
from foreign.foreign_big_base import foreign_big_base_case
from foreign.foreign_big_condition import foreign_big_condition_case
from foreign.foreign_big_dailys import foreign_big_dailys_case
from foreign.foreign_big_erro import foreign_big_erro_case
from foreign.foreign_big_hourlys import foreign_big_hourlys_case
from getpathInfo import text_Path
from util.conf_read import ConfRead
from util.data_deal import DateDeal
from util.foreign_data_deal import ForeignDateDeal


class ForeignBig:
    def __init__(self, path=text_Path(), url_data='139.159.198.98'):
        datedeal = DateDeal()
        self.text_aaa = path
        self.days_time_aqi_list = datedeal.days_time_aqi_list()
        self.url = url_data

    def foreign_code_to_name(self, accucode, cityname):
        # 错误城市计数器
        erro_city_num = 0
        # 只需关注城市编码和经纬度，其他参数不需要关注
        big_api = f'http://{self.url}/pubDataServer/getweatherpub?apikey={ConfRead.conf_key()}&language=zh_CNchl=&codeType=1'
        params = {'citycode': accucode}
        # 发送GET请求
        result, time_out = RunMain().run_main('GET', big_api, params)
        # 拿JSON
        data = result.json()
        if time_out == 2:
            erro_city_num += 1
            with open(self.text_aaa + "foreign_big_erro.txt", mode='a+', encoding='UTF-8') as f:
                f.write(
                    f"[{accucode} / {cityname}] - " + '响应超时' + "\n")
        result_OK = data['resultinfo']
        print(result_OK)
        # print(result)
        # 接口是否有返回
        er1, er2 = foreign_big_erro_case(data, time_out, result.status_code, data)
        if er1 != '' or er2 != '':
            erro_da = ''
            if er1 != '':
                erro_da = er1
            if er2 != '':
                erro_da = erro_da + ',' + er2
            erro_city_num += 1
            with open(self.text_aaa + "foreign_big_erro.txt", mode='a+', encoding='UTF-8') as f:
                f.write(
                    f"[{accucode} / {cityname}] - " + erro_da + "\n")
        else:
            pass

        # 城市信息

        base_re1, base_re2, base_re3, base_re4 = foreign_big_base_case(accucode, data)
        if base_re1 != '' or base_re2 != '' or base_re3 != '' or base_re4 != '':
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
                with open(self.text_aaa + "foreign_big_base.txt", mode='a+', encoding='UTF-8') as f:
                    f.write(
                        f"[{accucode} / {cityname}] - " + str_base + "\n")
        else:
            pass

        # 实况天气
        con_re1, con_re2, con_re3, con_re4 = foreign_big_condition_case(data)
        if con_re1 != '' or con_re2 != '' or con_re3 != '' or con_re4 != '':
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
            with open(self.text_aaa + "foreign_big_condition.txt", mode='a+', encoding='UTF-8') as f:
                f.write(
                    f"[{accucode} / {cityname}] - " + str_condition + "\n")

        else:
            pass

        # 多天预报
        dailys_re1, dailys_re2, dailys_re3, dailys_re4, dailys_re5, dailys_re6, dailys_re7, dailys_re8, dailys_re9, dailys_re10, dailys_re11 = foreign_big_dailys_case(
            data)
        if dailys_re1 != '' or dailys_re2 != '' or dailys_re3 != '' or dailys_re4 != '' or dailys_re5 != '' or dailys_re6 != '' or dailys_re7 != '' or dailys_re8 != '' or dailys_re9 != '' or dailys_re10 != '' or dailys_re11 != '':
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
            if dailys_re11 != '':
                str_dailys = str_dailys + ',' + dailys_re11
            with open(self.text_aaa + "foreign_big_dailys.txt", mode='a+', encoding='UTF-8') as f:
                f.write(
                    f"[{accucode} / {cityname}] - " + str_dailys + "\n")
        else:
            pass

        # 小时天气

        h_r1, h_r2, h_r3, h_r4 = foreign_big_hourlys_case(data)
        if h_r1 != '' or h_r2 != '' or h_r3 != '' or h_r4 != '':
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

            with open(self.text_aaa + "foreign_big_hourlys.txt", mode='a+', encoding='UTF-8') as f:
                f.write(
                    f"[{accucode} / {cityname}] - " + str_hourlys + "\n")
        else:
            pass

        if erro_city_num >= 1:
            with open(self.text_aaa + "foreign_big_erro_citynum.txt", mode='a+', encoding='UTF-8') as f:
                f.write(
                    f"{erro_city_num}" + "\n")

    # def foreign_code_to_name1(self, accucode, cityname):
    #     self.foreign_code_to_name(accucode, cityname, file_num=1)
    #
    # def foreign_code_to_name2(self, accucode, cityname):
    #     self.foreign_code_to_name(accucode, cityname, file_num=2)
    #
    # def foreign_code_to_name3(self, accucode, cityname):
    #     self.foreign_code_to_name(accucode, cityname, file_num=3)
    #
    # def foreign_code_to_name4(self, accucode, cityname):
    #     self.foreign_code_to_name(accucode, cityname, file_num=4)
    #
    # def foreign_code_to_name5(self, accucode, cityname):
    #     self.foreign_code_to_name(accucode, cityname, file_num=5)


if __name__ == '__main__':
    a = ForeignBig()
    # 拿数据
    datedeal = ForeignDateDeal()
    # 拿 城市编码 ，城市名称， 经度， 纬度
    accucode, cityname, province, country, timezone, geolong, geolat = datedeal.foreign_date(' limit 0, 10000')

    print()
    print('------------------    开始执行    -----------------------')
    start_time = time.time()
    from util.fast import do_fast

    # aaaaaa = do_fast(a.foreign_code_to_name, accucode, cityname)

    a.foreign_code_to_name('3111883', '阿奥恩拉')
    # print(aaaaaa)
    # a.geo_to_name('89.180437', '44.000497')
    end_time = time.time()
    print(f'大颗粒接口国外站点执行完毕，耗时：{end_time - start_time}')
    print('------------------    执行结束    -----------------------')
    print(f'------------------    共耗时{end_time - start_time}    -----------------------')
