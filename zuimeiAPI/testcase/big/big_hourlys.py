# coding=<encoding name> ： # coding=utf-8
import yaml

from util.conf_read import ConfRead
from util.timestamp_deal import hourlys_zero, hourlys_time_deal

hourly_list_1 = ConfRead.conf_get('big.conf', 'hourly_list', 'hourly_list')
hourly_re_list_1 = yaml.load(hourly_list_1, Loader=yaml.FullLoader)


def big_hourlys_case(data):
    hourlys_t1 = ''
    hourlys_t2 = ''
    hourlys_t3 = ''
    hourlys_t4 = ''


    result_OK = data['resultinfo']
    # 判断接口是否异常
    if result_OK != 'OK':
        pass

    # 城市信息是否正确
    else:
        # 小时天气 	hourlys
        # 小时天气  0 当前小时 一致
        hourly_zero = data['data']['hourlys']['hourlyweathers'][0]['date']
        if hourlys_zero(hourly_zero) == 1:
            pass
        else:
            print(f"小时天气，返回的首个小时与当前时间小时不一致！")
            # logger.info(f"小时天气，返回的首个小时与当前时间小时不一致！定位为：{accucode}")
            hourlys_t1 = f'{hourlys_time_deal(hourly_zero)}[返回的首个小时]'
            # with open(self.text_aaa + "big_hourlys.txt", mode='a+', encoding='utf-8') as f:
            #     f.write(f"[{accucode} / {cityname}] - 小时天气返回的首个小时-[{hourlys_time_deal(hourly_zero)}]\n")

        # 小时天气 72小时
        hourly_num = len(data['data']['hourlys']['hourlyweathers'])
        if hourly_num == 72:
            pass
        else:
            print(f"小时天气，72个小时，多了或者少了，接口返回有{hourly_num}个小时")
            hourlys_t2 = f'{hourly_num}[返回小时数72]'
            # logger.info(f"小时天气，72个小时，多了或者少了！定位为：{accucode}，接口返回有{hourly_num}个小时")
            # with open(self.text_aaa + "big_hourlys.txt", mode='a+', encoding='utf-8') as f:
            #     f.write(f"[{accucode} / {cityname}] - 小时天气返回-[{hourly_num}]个小时\n")

        # 小时天气 为空检查

        for hourly_i in hourly_re_list_1:
            for hourly_z in range(0, 71):
                try:
                    hourly11 = str(data['data']['hourlys']['hourlyweathers'][hourly_z][hourly_i])
                except BaseException:
                    print(
                        f"小时天气缺失参数-[{hourly_i}]-发生节点-[{hourly_z}]")
                    # logger.info(
                    #     f"小时天气，出现为空元素！定位为：{accucode}，为空的参数为{hourly_i}，出现在节点：{hourly_z}")
                    hourlys_t3 = f'{hourly_z},{hourly_i}[不存在]'
                    # with open(self.text_aaa + "big_hourlys.txt", mode='a+', encoding='utf-8') as f:
                    #     f.write(f"[{accucode} / {cityname}] - 小时天气缺失参数-[{hourly_i}]-发生节点-[{hourly_z}]\n")

                else:
                    if len(hourly11) > 0:
                        pass
                    else:
                        print(
                            f"小时天气，出现为空元素，为空的参数为{hourly_i}，出现在节点：{hourly_z}")
                        # logger.info(
                        #     f"小时天气，出现为空元素！定位为：{accucode}，为空的参数为{hourly_i}，出现在节点：{hourly_z}")
                        hourlys_t4 = f'{hourly_z},{hourly_i}[为空]'
                        # with open(self.text_aaa + "big_hourlys.txt", mode='a+', encoding='utf-8') as f:
                        #     f.write(f"[{accucode} / {cityname}] - 小时天气参数为空-[{hourly_i}]-发生节点-[{hourly_z}]\n")

    return hourlys_t1, hourlys_t2, hourlys_t3, hourlys_t4
