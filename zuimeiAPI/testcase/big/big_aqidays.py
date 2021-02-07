# coding=<encoding name> ： # coding=utf-8
import datetime

import yaml

from util.conf_read import ConfRead
from util.timestamp_deal import aqi_days_day_deal, aqi_today

aqi_list_ = ConfRead.conf_get('big.conf', 'aqi_list', 'aqi_list')
aqi_re_list = yaml.load(aqi_list_, Loader=yaml.FullLoader)


def big_aqidays_case(data):
    aqidays_t1 = ''
    aqidays_t2 = ''
    aqidays_t3 = ''
    aqidays_t4 = ''
    aqidays_t5 = ''
    aqidays_t6 = ''

    result_OK = data['resultinfo']
    # 判断接口是否异常
    if result_OK != 'OK':
        pass

    # 城市信息是否正确
    else:
        # 多天空气质量
        # 判断16天第一天时间
        # 今天

        now = datetime.datetime.now()
        # 昨天
        day1 = now + datetime.timedelta(days=-1)
        # 前天
        day2 = now + datetime.timedelta(days=-2)

        day1_re = day1.strftime("%Y-%m-%d")
        day2_re = day2.strftime("%Y-%m-%d")
        try:
            aaaaa = data['data']['aqidays']
        except BaseException:
            aqidays_t1 = '无多天空气质量'
        else:
            try:
                aqi_zore = data['data']['aqidays'][0]['date']
            except BaseException:
                print(f"多天空气质量,此城市无多天空气质量！")
                # logger.info(f"多天空气质量,此城市无多天空气质量！定位为：{accucode}")
                # with open(self.text_aaa + "big_aqidays.txt", mode='a+', encoding='utf-8') as f:
                #     f.write(f"\n多天空气质量,此城市无多天空气质量！定位为：{accucode}")
            else:
                if aqi_today() == 1:
                    if aqi_zore == day1_re:
                        pass
                    else:
                        print(
                            f"多天空气质量九点前执行-首日为-[{aqi_zore}]")
                        # logger.info(
                        #     f"多天空气质量,判断16天第一天时间，校验失败！定位为：{accucode}")
                        aqidays_t1 = f'{aqi_zore}[九点前执行的首日]'
                        # with open(self.text_aaa + "big_aqidays.txt", mode='a+', encoding='utf-8') as f:
                        #     f.write(f"[{accucode} / {cityname}] - 多天空气质量九点前执行-首日为-[{aqi_zore}]\n")
                else:
                    if aqi_zore == day1_re or aqi_zore == day2_re:
                        pass
                    else:
                        print(
                            f"多天空气质量,判断16天第一天时间，校验失败！")
                        aqidays_t2 = f'{aqi_zore}[九点后执行的首日]'
                        # logger.info(
                        #     f"多天空气质量,判断16天第一天时间，校验失败！定位为：{accucode}")
                        # with open(self.text_aaa + "big_aqidays.txt", mode='a+', encoding='utf-8') as f:
                        #     f.write(f"[{accucode} / {cityname}] - 多天空气质量九点后执行-首日为-[{aqi_zore}]\n")

            # 检查多天空气质量是否16天
            try:
                aqi_days_len = len(data['data']['aqidays'])
            except BaseException:
                print(f'此城市无多天空气质量')
                aqidays_t3 = '无多天空气质量'
                # logger.info(f'此城市无多天空气质量，定位为：{accucode}')
                # with open(self.text_aaa + "big_aqidays.txt", mode='a+', encoding='utf-8') as f:
                #     f.write(f'[{accucode} / {cityname}] - 无多天空气质量\n')
            else:
                if aqi_days_len == 16:
                    pass
                else:
                    print(
                        f"多天空气质量,天数总数不够，校验失败！")
                    # logger.info(
                    #     f"多天空气质量,天数总数不够，校验失败！定位为：{accucode}")
                    aqidays_t4 = f'{aqi_days_len}[多天空气质量天数]'
                    # with open(self.text_aaa + "big_aqidays.txt", mode='a+', encoding='utf-8') as f:
                    #     f.write(f"[{accucode} / {cityname}] - 多天空气质量天数-[{aqi_days_len}]\n")

                # 检查多天空气质量是否为空

                aqi_days_zero = '2021-11-11'
                try:
                    aqi_days_zero = data['data']['aqidays'][0]
                except BaseException:
                    pass

                for aqi_list_i in aqi_re_list:
                    for aqi_for_num in range(0, 16):
                        try:
                            aqi11 = str(data['data']['aqidays'][aqi_for_num][aqi_list_i])
                        except BaseException:
                            print(f"多天空气质量，参数缺失，缺失的参数为{aqi_list_i}，出现在节点{aqi_for_num}")
                            # logger.info(f"多天空气质量，参数缺失，定位为：{accucode}，缺失的参数为{aqi_list_i}，出现在节点{aqi_for_num}")
                            aqidays_t5 = f'{aqi_days_day_deal(aqi_days_zero, aqi_for_num)},{aqi_list_i}[不存在]'
                            # with open(self.text_aaa + "big_aqidays.txt", mode='a+', encoding='utf-8') as f: f.write(
                            # f"[{accucode} / {cityname}] - 多天空气质量缺失参数-[{aqi_list_i}]-发生日期-[{aqi_days_day_deal(
                            # aqi_days_zero, aqi_for_num)}]\n")
                        else:
                            if len(aqi11) > 0:
                                pass
                            else:
                                print(f"多天空气质量，出现为空元素，为空的参数为{aqi_list_i}，出现在节点{aqi_for_num}")
                                # logger.info(f"多天空气质量，出现为空元素！定位为：{accucode}，为空的参数为{aqi_list_i}，出现在节点{aqi_for_num}")
                                aqidays_t6 = f'{aqi_days_day_deal(aqi_days_zero, aqi_for_num)},{aqi_list_i}[为空]'
                                # with open(self.text_aaa + "big_aqidays.txt", mode='a+', encoding='utf-8') as f:
                                # f.write( f"[{accucode} / {cityname}] - 多天空气质量参数为空-[{aqi_list_i}]-发生日期-[{
                                # aqi_days_day_deal(aqi_days_zero, aqi_for_num)}]\n")

    return aqidays_t1, aqidays_t2, aqidays_t3, aqidays_t4, aqidays_t5, aqidays_t6
