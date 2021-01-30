# coding=<encoding name> ： # coding=utf-8
import yaml

from util.conf_read import ConfRead
from util.timestamp_deal import ts_nine, hourlys_time_deal, daily_day_deal

daily_list = ConfRead.conf_get('big.conf', 'daily_list', 'daily_list0')
daily_re_list = yaml.load(daily_list, Loader=yaml.FullLoader)

daily_list_2 = ConfRead.conf_get('big.conf', 'daily_list', 'daily_list1')
daily_re_list_2 = yaml.load(daily_list_2, Loader=yaml.FullLoader)

daily_list_3 = ConfRead.conf_get('big.conf', 'daily_list', 'daily_day_night')
daily_re_list_3 = yaml.load(daily_list_3, Loader=yaml.FullLoader)


# 多天预报
def big_dailys_case(data):
    big_dailys_t1 = ''
    big_dailys_t2 = ''
    big_dailys_t3 = ''
    big_dailys_t4 = ''
    big_dailys_t5 = ''
    big_dailys_t6 = ''
    big_dailys_t7 = ''
    big_dailys_t8 = ''
    big_dailys_t9 = ''
    big_dailys_t10 = ''

    result_OK = data['resultinfo']
    # 判断接口是否异常
    if result_OK != 'OK':
        pass

    # 城市信息是否正确
    else:
        # 多天预报
        publictime = data["data"]['dailys']['dailyweathers'][0]['publictime']
        nine_re = ts_nine(publictime)
        if nine_re == 1:
            pass
        else:
            print(f"多天预报，时间戳-[{publictime}]-逻辑错误-")
            # logger.info(f"多天预报，时间戳为昨天或者前天逻辑不对，定位为：{accucode}")
            big_dailys_t1 = f'{hourlys_time_deal(publictime)}-[九点前后时间逻辑错误]'
            # with open(self.text_aaa + "big_dailys.txt", mode='a+', encoding='utf-8') as f:
            #     f.write(f"[{accucode} / {cityname}] - 多天预报日期-[{hourlys_time_deal(publictime)}]-九点前后执行逻辑错误\n")

        if len(data['data']['dailys']['dailyweathers']) == 16:
            pass
        else:
            print(f"多天预报，返回的天数不为16天")
            # logger.info(f"多天预报，返回的天数不为16天，定位为：{accucode}")
            big_dailys_t2 = f"{len(data['data']['dailys']['dailyweathers'])}-[16天返回天数不正确]"
            # with open(self.text_aaa + "big_dailys.txt", mode='a+', encoding='utf-8') as f:
            #     f.write(
            #         f"[{accucode} / {cityname}] - 多天预报16天返回天数-[{len(data['data']['dailys']['dailyweathers'])}]\n")

        # 0-6的

        flag1 = True
        for i in daily_re_list:
            for j in range(7):
                try:
                    daily11 = str(data['data']['dailys']['dailyweathers'][j][i])
                except BaseException:
                    print(f"多天预报,参数缺失！缺失的参数为{i}，出现在节点：{j}")
                    # logger.info(f"多天预报,出现为空元素！定位为：{accucode}，为空的参数为{i},出现在节点：{j}")
                    big_dailys_t3 = f'{daily_day_deal(publictime, j)},{i}[不存在]'
                    flag1 = False
                    # with open(self.text_aaa + "big_dailys.txt", mode='a+', encoding='utf-8') as f:
                    #     f.write(
                    #         f"[{accucode} / {cityname}] - 多天预报缺失参数-[{i}]-发生日期-[{daily_day_deal(publictime, j)}]\n")
                else:
                    if len(daily11) > 0:
                        pass
                    else:
                        print(f"多天预报0-6，出现为空元素！为空的参数为{i},出现在节点：{j}")
                        # logger.info(f"多天预报0-6，出现为空元素！定位为：{accucode}，为空的参数为{i},出现在节点：{j}")
                        big_dailys_t4 = f'{daily_day_deal(publictime, j)},{i}[为空]'
                        flag1 = False
                        # with open(self.text_aaa + "big_dailys.txt", mode='a+', encoding='utf-8') as f: f.write( f"[
                        # {accucode} / {cityname}] - 多天预报参数为空-[{i}]-发生日期-[{daily_day_deal(publictime, j)}]\n")
            if flag1 == False:
                break

        # 7-15的

        flag2 = True
        for y in daily_re_list_2:
            for x in range(7, 16):
                try:
                    daily22 = str(data['data']['dailys']['dailyweathers'][x][y])
                except BaseException:
                    print(f"多天预报,参数缺失！缺失的参数为{y}，出现在节点：{x}")
                    # logger.info(f"多天预报,参数缺失！定位为：{accucode}，缺失的参数为{y}，出现在节点：{x}")
                    big_dailys_t5 = f'{daily_day_deal(publictime, x)},{y}[不存在]'
                    flag2 = False
                    # with open(self.text_aaa + "big_dailys.txt", mode='a+', encoding='utf-8') as f:
                    #     f.write(
                    #         f"[{accucode} / {cityname}] - 多天预报缺失参数-[{y}]-发生日期-[{daily_day_deal(publictime, x)}]\n")
                else:
                    if len(daily22) > 0:
                        pass
                    else:
                        print(f"多天预报7-15，出现为空元素！为空的参数为{y}，出现在节点：{x}")
                        # logger.info(f"多天预报7-15，出现为空元素！定位为：{accucode}，为空的参数为{y}，出现在节点：{x}")
                        flag2 = False
                        big_dailys_t6 = f'{daily_day_deal(publictime, x)},{y}[为空]'
                        # with open(self.text_aaa + "big_dailys.txt", mode='a+', encoding='utf-8') as f: f.write( f"[
                        # {accucode} / {cityname}] - 多天预报参数为空-[{y}]-发生日期-[{daily_day_deal(publictime, x)}]\n")
            if flag2 == False:
                break

        # condition DAY NIGHT
        flag3 = True
        for c in daily_re_list_3:
            for z in range(16):
                try:
                    daily33 = str(data['data']['dailys']['dailyweathers'][z]['conditionDay'][c])
                except BaseException:
                    print(f"多天预报conditionDay,参数缺失！缺失的参数为{c}，出现在节点：{z}")
                    # logger.info(f"多天预报conditionDay,参数缺失！定位为：{accucode}，缺失的参数为{c}，出现在节点：{z}")
                    big_dailys_t7 = f'{daily_day_deal(publictime, z)},{c}[不存在]'
                    flag3 = False
                    # with open(self.text_aaa + "big_dailys.txt", mode='a+', encoding='utf-8') as f: f.write( f"[{
                    # accucode} / {cityname}] - 多天预报conditionDay缺失参数-[{c}]-发生日期-[{daily_day_deal(publictime, z)}]\n")
                else:
                    if len(daily33) > 0:
                        pass
                    else:
                        print(
                            f"多天预报conditionDay，出现为空元素！为空的参数为{c}，出现在节点：{z}")
                        # logger.info(
                        #     f"多天预报conditionDay，出现为空元素！定位为：{accucode}，为空的参数为{c}，出现在节点：{z}")
                        big_dailys_t8 = f'{daily_day_deal(publictime, c)},{z}[为空]'
                        flag3 = False
                        # with open(self.text_aaa + "big_dailys.txt", mode='a+', encoding='utf-8') as f: f.write( f"[
                        # {accucode} / {cityname}] - 多天预报conditionDay参数为空-[{c}]-发生日期-[{daily_day_deal(publictime,
                        # z)}]\n")
            if flag3 == False:
                break

        flag4 = True
        for b in daily_re_list_3:
            for n in range(16):
                try:
                    daily44 = str(data['data']['dailys']['dailyweathers'][n]['conditionNight'][b])
                except BaseException:
                    print(
                        f"多天预报conditionNight，参数缺失，缺失的参数为{b}，出现在节点{n}")
                    big_dailys_t9 = f'{daily_day_deal(publictime, n)},{b}[不存在]'
                    # logger.info(
                    #     f"多天预报conditionNight，参数缺失！定位为：{accucode}，缺失的参数为{b}，出现在节点{n}")
                    flag4 = False
                    # with open(self.text_aaa + "big_dailys.txt", mode='a+', encoding='utf-8') as f: f.write( f"[{
                    # accucode} / {cityname}] - 多天预报conditionDay缺失参数-[{b}]-发生日期-[{daily_day_deal(publictime, n)}]\n")

                else:
                    if len(daily44) > 0:
                        pass
                    else:
                        print(
                            f"多天预报conditionNight，出现为空元素！为空的参数为{b}，出现在节点{n}")
                        # logger.info(
                        # f"多天预报conditionNight，出现为空元素！定位为：{accucode}，为空的参数为{b}，出现在节点{n}")
                        big_dailys_t10 = f'{daily_day_deal(publictime, n)},{b}[为空]'
                        flag4 = False
                        # with open(self.text_aaa + "big_dailys.txt", mode='a+', encoding='utf-8') as f: f.write( f"[
                        # {accucode} / {cityname}] - 多天预报conditionNight参数为空-[{b}]-发生日期-[{daily_day_deal(publictime,
                        # n)}]\n")

            if flag4 == False:
                break
    return big_dailys_t1, big_dailys_t2, big_dailys_t3, big_dailys_t4, big_dailys_t5, big_dailys_t6, big_dailys_t7, big_dailys_t8, big_dailys_t9, big_dailys_t10
