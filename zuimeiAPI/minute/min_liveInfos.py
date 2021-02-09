# coding=<encoding name> ： # coding=utf-8
import time

import yaml
import datetime
from common.configHTTP import RunMain
from getpathInfo import text_Path
from util.conf_read import ConfRead
from util.timestamp_deal import aqi_today




class MinLiveInfos:
    def __init__(self, path=text_Path(), url_data='139.159.198.98'):
        self.text_aaa = path
        self.url = url_data
    def min_liveInfos_api(self, accucode, cityname):
        erro_num = 0
        live_api = f'http://{self.url}/pubDataServer/getweatherpub?apikey={ConfRead.conf_key()}&language=zh_CNchl=&codeType=1&dataType=index'
        params = {'citycode': accucode}
        # 发送GET请求
        result, timeout_num = RunMain().run_main('GET', live_api, params)
        data = result.json()
        # a = data['resultinfo']
        print(accucode)
        print(live_api)
        data_resultinfo = data['resultinfo']
        if timeout_num == 2:
            erro_num += 1
            with open(self.text_aaa + "min_big_liveinfos.txt", mode='a+', encoding='utf-8') as f:
                f.write(f'[{accucode} / {cityname}] - 响应超时\n')
        if data_resultinfo == 'server error!':
            erro_num += 1
            print(f'生活指数 接口异常，定位：{accucode}')
            # logger.info(print(f'生活指数 接口异常，定位：{accucode}'))
            with open(self.text_aaa + "min_big_liveinfos.txt", mode='a+', encoding='utf-8') as f:
                f.write(f'[{accucode} / {cityname}] - 接口异常 - [{result.status_code}] - [{data}]\n')
        else:
            # 23个生活指数
            try:
                live_len = len(data['data']['additionalLiveInfos'])
            except BaseException:
                erro_num += 1
                print(f'生活指数缺失additionalLiveInfos，定位：{accucode}')
                # logger.info(f'生活指数缺失additionalLiveInfos，定位：{accucode}')
                with open(self.text_aaa + "min_big_liveinfos.txt", mode='a+', encoding='utf-8') as f:
                    f.write(f'[{accucode} / {cityname}] - additionalLiveInfos[不存在]\n')
            else:
                if live_len == 23:
                    pass
                else:
                    erro_num += 1
                    print(f"生活指数,返回为数量或多或少，定位为：{accucode}")
                    # logger.info(f"生活指数,返回为数量或多或少，定位为：{accucode}")
                    with open(self.text_aaa + "min_big_liveinfos.txt", mode='a+', encoding='utf-8') as f:
                        f.write(f'[{accucode} / {cityname}] - {live_len}[应为23]\n')

            # 判断时间

            if aqi_today() == 1:
                for i in range(0, 23):
                    num = 0
                    for j in range(0, 4):
                        try:
                            time = data['data']['additionalLiveInfos'][i]['levelList'][j]['day']
                        except BaseException:
                            live_re_1 = data['data']['additionalLiveInfos'][i]['name']
                            live_date_1 = data['data']['additionalLiveInfos'][i]['levelList'][j]['day']
                            erro_num += 1
                            print(f"生活指数,日期有参数缺失问题，定位为：{accucode},节点为：{i}，{j}")
                            # logger.info(f"生活指数,日期有参数缺失问题，定位为：{accucode},节点为：{i}，{j}")
                            with open(self.text_aaa + "min_big_liveinfos.txt", mode='a+', encoding='utf-8') as f:
                                f.write(f'[{accucode} / {cityname}] - {live_re_1},{live_date_1}[日期的参数不存在]\n')

                        else:
                            now = datetime.datetime.now()
                            day1 = now + datetime.timedelta(days=num)
                            day1_re = day1.strftime("%Y-%m-%d")
                            if time == day1_re:
                                num += 1
                            else:
                                erro_num += 1
                                num += 1
                                live_re_1 = data['data']['additionalLiveInfos'][i]['name']
                                live_date_1 = data['data']['additionalLiveInfos'][i]['levelList'][j]['day']
                                print(f"生活指数-日期错误-节点-[{i},{j}]-定位-[{accucode}]")
                                # logger.info(f"生活指数,日期有问题，定位为：{accucode},节点为：{i}，{j}")
                                with open(self.text_aaa + "min_big_liveinfos.txt", mode='a+', encoding='utf-8') as f:
                                    f.write(f'[{accucode} / {cityname}] - {live_re_1},{live_date_1}[日期不符合规范]\n')

            else:
                for x in range(0, 23):
                    num = -1
                    for y in range(0, 4):
                        try:
                            time = data['data']['additionalLiveInfos'][x]['levelList'][y]['day']
                        except BaseException:
                            erro_num += 1
                            live_re_1 = data['data']['additionalLiveInfos'][x]['name']
                            live_date_1 = data['data']['additionalLiveInfos'][x]['levelList'][y]['day']
                            print(f"生活指数,日期有参数缺失问题，定位为：{accucode},节点为：{x}，{y}")
                            # logger.info(f"生活指数,日期有参数缺失问题，定位为：{accucode},节点为：{x}，{y}")
                            with open(self.text_aaa + "min_big_liveinfos.txt", mode='a+', encoding='utf-8') as f:
                                f.write(f'[{accucode} / {cityname}] - {live_re_1},{live_date_1}[日期的参数不存在]\n')
                        else:
                            now = datetime.datetime.now()
                            day1 = now + datetime.timedelta(days=num)
                            day1_re = day1.strftime("%Y-%m-%d")
                            if time == day1_re:
                                num += 1
                            else:
                                live_re_1 = data['data']['additionalLiveInfos'][x]['name']
                                live_date_1 = data['data']['additionalLiveInfos'][x]['levelList'][y]['day']
                                num += 1
                                erro_num += 1
                                print(f"生活指数,日期有问题，定位为：{accucode},节点为：{x}，{y}")
                                # logger.info(f"生活指数,日期有问题，定位为：{accucode},节点为：{x}，{y}")
                                with open(self.text_aaa + "min_big_liveinfos.txt", mode='a+', encoding='utf-8') as f:
                                    f.write(f'[{accucode} / {cityname}] - {live_re_1},{live_date_1}[日期不符合规范]\n')

            # 判断参数不为空
            live_list = ConfRead.conf_get('live.conf', 'live_list', 'live_list')
            live_re_list = yaml.load(live_list, Loader=yaml.FullLoader)

            for live_y in range(0, 23):
                for xxx in range(0, 4):
                    for live_i in live_re_list:
                        try:
                            live11 = str(data['data']['additionalLiveInfos'][live_y]['levelList'][xxx][live_i])
                        except BaseException:
                            erro_num += 1
                            print(
                                f"生活指数，缺失参数，定位为：{accucode}，缺失的参数为{live_i}，出现的条目为：{live_y}，出现的天数为：{xxx}")
                            # logger.info(
                            #     f"生活指数，缺失参数，定位为：{accucode}，缺失的参数为{live_i},出现的条目为：{live_y}，出现的天数为：{xxx}")
                            with open(self.text_aaa + "min_big_liveinfos.txt", mode='a+', encoding='utf-8') as f:
                                f.write(f'[{accucode} / {cityname}] - {live_y},{xxx},{live_i}[不存在]\n')
                        else:
                            if len(live11) > 0:
                                pass
                            else:
                                erro_num += 1
                                print(
                                    f"生活指数，出现为空元素！定位为：{accucode}，为空的参数为{live_i}，出现的条目为：{live_y}，出现的天数为：{xxx}")
                                # logger.info(
                                #     f"生活指数，出现为空元素！定位为：{accucode}，为空的参数为{live_i},出现的条目为：{live_y}，出现的天数为：{xxx}")
                                with open(self.text_aaa + "min_big_liveinfos.txt", mode='a+', encoding='utf-8') as f:
                                    f.write(f'[{accucode} / {cityname}] - {live_y},{xxx},{live_i}[为空]\n')

        if erro_num >= 1:
            with open(self.text_aaa + "min_live_erro_citynum.txt", mode='a+', encoding='utf-8') as f:
                f.write(
                    f"{erro_num}" + "\n")
            return 1
        else:
            return 2


if __name__ == '__main__':
    pass
