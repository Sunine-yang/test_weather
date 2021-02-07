# coding=<encoding name> ： # coding=utf-8
import time

from common.configHTTP import RunMain
from getpathInfo import text_Path
from testcase.dailys.ninety_empty import ninety_empty_case
from testcase.dailys.ninety_erro import ninety_erro_case
from util.conf_read import ConfRead
from util.data_deal import DateDeal

from util.timestamp_deal import ninety_start_end


class Ninety:
    def __init__(self, path=text_Path(), url_data='139.159.198.98'):
        self.text_aaa = path
        self.url = url_data

    def dailys_api(self, accucode, cityname):
        erro_city_num = 0
        start, end = ninety_start_end()
        ninety_api = f'http://{self.url}/pubDataServer/getweatherdailys?apikey={ConfRead.conf_key()}&start={start}&end={end}&citycode={accucode}'
        result, timeout = RunMain().run_main('GET', ninety_api)
        if timeout == 2:
            erro_city_num += 1
            with open(self.text_aaa + "ninety_erro.txt", mode='a+', encoding='utf-8') as f:
                f.write(
                    f"[{accucode} / {cityname}] - " + '响应超时' + "\n")
        # 拿JSON
        data = result.json()
        print(ninety_api)
        # 90日 为空
        em1, em2, em3, em4, em5, em6 = ninety_empty_case(data)

        if em1 != '' or em2 != '' or em3 != '' or em4 != '' or em5 != '' or em6 != '':
            erro_city_num += 1
            str_em = ''
            if em1 != '':
                str_em = em1
            if em2 != '':
                str_em = str_em + ',' + em2
            if em3 != '':
                str_em = str_em + ',' + em3
            if em4 != '':
                str_em = str_em + ',' + em4
            if em5 != '':
                str_em = str_em + ',' + em5
            if em6 != '':
                str_em = str_em + ',' + em6

            with open(self.text_aaa + "ninety_empty.txt", mode='a+', encoding='utf-8') as f:
                f.write(
                    f"[{accucode} / {cityname}] - " + str_em + "\n")
        else:
            pass

        # 90日 错误
        e1, e2, e3, e4, e5 = ninety_erro_case(data, timeout, result.status_code, data)

        if e1 != '' or e2 != '' or e3 != '' or e4 != '' or e5 != '':
            erro_city_num += 1
            erro_num = ''
            if e1 != '':
                erro_num = e1
            if e2 != '':
                erro_num = erro_num + e2
            if e3 != '':
                erro_num = erro_num + e3
            if e4 != '':
                erro_num = erro_num + e4
            if e5 != '':
                erro_num = erro_num + e5

            with open(self.text_aaa + "ninety_erro.txt", mode='a+', encoding='utf-8') as f:
                f.write(
                    f"[{accucode} / {cityname}] - " + erro_num + "\n")
        else:
            pass

        if erro_city_num >= 1:
            with open(self.text_aaa + "nine_erro_citynum.txt", mode='a+', encoding='utf-8') as f:
                f.write(
                    f"{erro_city_num}" + "\n")


if __name__ == '__main__':
    from util.fast import do_fast

    a = Ninety()
    # 拿数据
    datedeal = DateDeal()
    # 拿 城市编码 ，城市名称， 经度， 纬度
    accucode, cityname, geolong, geolat = datedeal.china_date()
    # print(accucode)
    start_time = time.time()
    # do_fast(a.dailys_api, accucode, cityname)
    a.dailys_api('59474', '桂阳县')
    end_time = time.time()
    print(f'大颗粒接口中国城市执行完毕，耗时：{end_time - start_time}')
    # a.dailys_api(9999998)