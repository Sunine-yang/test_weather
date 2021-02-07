# -*- coding:utf-8 -*-
import yaml

from util.conf_read import ConfRead
from util.timestamp_deal import ninety_erro_day

ninety_list1 = ConfRead.conf_get('big.conf', 'ninty_list', 'ninty_list')
ninety_re_list1 = yaml.load(ninety_list1, Loader=yaml.FullLoader)

ninety_list1_day = ConfRead.conf_get('big.conf', 'ninty_list', 'ninty_list_day_night')
ninety_re_list1_day = yaml.load(ninety_list1_day, Loader=yaml.FullLoader)

ninety_list1_night = ConfRead.conf_get('big.conf', 'ninty_list', 'ninty_list_day_night')
ninety_re_list1_night = yaml.load(ninety_list1_night, Loader=yaml.FullLoader)


def ninety_empty_case(data):
    empty_t1 = ''
    empty_t2 = ''
    empty_t3 = ''
    empty_t4 = ''
    empty_t5 = ''
    empty_t6 = ''

    try:
        data_status = data['status']
    except BaseException:
        data_status = 200
    if data_status == 500:
        pass
    else:
        # 判断 是否为空
        # 1
        flag1 = True
        for days_i in range(0, 91):
            for ninety_name in ninety_re_list1:
                try:
                    ninety11 = str(data['dailys']['dailyweathers'][days_i][ninety_name])
                except BaseException:
                    print(f"90天，缺失参数！缺失的参数为{ninety_name},出现的天数为：{ninety_erro_day(days_i)}")
                    # logger.info(f"90天，缺失参数！定位为：{accucode}，缺失的参数为{ninety_name},出现的天数为：{days_i}")
                    empty_t1 = f'{ninety_erro_day(days_i)},{ninety_name}[不存在]'
                    # with open(self.text_aaa + "ninety_empty.txt", mode='a+', encoding='utf-8') as f:
                    #     f.write(f'[{accucode} / {cityname}] - 缺失参数-[{ninety_name}]-日期-[{ninety_erro_day(days_i)}]\n')
                    flag1 = False
                else:
                    # print(ninety11)
                    if len(ninety11) > 0:
                        pass
                    else:
                        print(f"90天，出现为空元素！为空的参数为{ninety_name},出现的天数为：{days_i}")
                        # logger.info(f"90天，出现为空元素！定位为：{accucode}，为空的参数为{ninety_name}，出现的天数为：{days_i}")
                        empty_t2 = f'{ninety_erro_day(days_i)},{ninety_name}[为空]'
                        # with open(self.text_aaa + "ninety_empty.txt", mode='a+', encoding='utf-8') as f:
                        #     f.write(
                        #         f'[{accucode} / {cityname}] - 参数为空-[{ninety_name}]-日期-[{ninety_erro_day(days_i)}]\n')
                        flag1 = False
            if flag1 == False:
                break

        # 白天
        flag2 = True

        for days_j in range(0, 91):
            for ninety_day_name in ninety_re_list1_day:
                try:
                    ninety22 = str(data['dailys']['dailyweathers'][days_j]['conditionDay'][ninety_day_name])
                except BaseException:
                    print(f"90天，参数缺失！缺失的参数为{ninety_day_name},出现的天数为：{days_j}")
                    # logger.info(f"90天，参数缺失！定位为：{accucode}，缺失的参数为{ninety_day_name},出现的天数为：{days_j}")
                    empty_t3 = f'{ninety_erro_day(days_j)},{ninety_day_name}[不存在]'
                    # with open(self.text_aaa + "ninety_empty.txt", mode='a+', encoding='utf-8') as f: f.write( f'[{
                    # accucode} / {cityname}] - 白天缺失参数-[{ninety_day_name}]-日期-[{ninety_erro_day(days_j)}]\n')
                    flag2 = False

                else:
                    if len(ninety22) > 0:
                        pass
                    else:
                        print(f"90天，出现为空元素！为空的参数为{ninety_day_name},出现的天数为：{days_j}")
                        # logger.info(f"90天，出现为空元素！定位为：{accucode}，为空的参数为{ninety_day_name},出现的天数为：{days_j}")
                        empty_t4 = f'{ninety_erro_day(days_j)},{ninety_day_name}[为空]'
                        # with open(self.text_aaa + "ninety_empty.txt", mode='a+', encoding='utf-8') as f: f.write(
                        # f'[{accucode} / {cityname}] - 白天参数为空-[{ninety_day_name}]-日期-[{ninety_erro_day(days_j)}]\n')
                        flag2 = False
            if flag2 == False:
                break

        # 晚上
        flag3 = True

        for days_x in range(0, 91):
            for ninety_day_name in ninety_re_list1_night:
                try:
                    ninety33 = str(data['dailys']['dailyweathers'][days_x]['conditionNight'][ninety_day_name])
                except BaseException:
                    print(f"90天，参数缺失，缺失的参数为{ninety_day_name},出现的天数为：{days_x}")
                    # logger.info(f"90天，参数缺失，定位为：{accucode}，缺失的参数为{ninety_day_name},出现的天数为：{days_x}")
                    empty_t5 = f'{ninety_erro_day(days_x)},{ninety_day_name}[不存在]'
                    # with open(self.text_aaa + "ninety_empty.txt", mode='a+', encoding='utf-8') as f: f.write( f'[{
                    # accucode} / {cityname}] - 晚上缺失参数-[{ninety_day_name}]-日期-[{ninety_erro_day(days_x)}]\n')
                    flag3 = False

                else:
                    if len(ninety33) > 0:
                        pass
                    else:
                        print(f"90天，出现为空元素！为空的参数为{ninety_day_name},出现的天数为：{days_x}")
                        # logger.info(f"90天，出现为空元素！定位为：{accucode}，为空的参数为{ninety_day_name},出现的天数为：{days_x}")
                        empty_t6 = f'{ninety_erro_day(days_x)},{ninety_day_name}[为空]'
                        # with open(self.text_aaa + "ninety_empty.txt", mode='a+', encoding='utf-8') as f: f.write(
                        # f'[{accucode} / {cityname}] - 晚上参数为空-[{ninety_day_name}]-日期-[{ninety_erro_day(days_x)}]\n')
                        flag3 = False
            if flag3 == False:
                break

    return empty_t1, empty_t2, empty_t3, empty_t4, empty_t5, empty_t6

if __name__ == '__main__':
    pass

