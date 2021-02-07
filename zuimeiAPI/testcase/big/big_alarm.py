# coding=<encoding name> ： # coding=utf-8
import yaml

from util.conf_read import ConfRead

alarm_list_1 = ConfRead.conf_get('big.conf', 'alarm_list', 'alarm_list')
alarm_re_list_1 = yaml.load(alarm_list_1, Loader=yaml.FullLoader)


def big_alarm_case(data):
    alarm_t1 = ''
    alarm_t2 = ''

    result_OK = data['resultinfo']
    # 判断接口是否异常
    if result_OK != 'OK':
        pass

    # 城市信息是否正确
    else:
        # 预警 alarm
        try:
            aaaaa = data['data']['alarm']
        except BaseException:
            alarm_t1 = '无预警'
        else:
            if len(data['data']['alarm']) > 0:
                for alarm_i in alarm_re_list_1:
                    for alarm_num in range(len(data['data']['alarm'])):
                        try:
                            alarm11 = data['data']['alarm'][alarm_num][alarm_i]
                        except BaseException:
                            print(
                                f"预警信息缺失参数-[{alarm_i}]-发生节点-[{alarm_num}]")
                            # logger.info(
                            #     f"预警信息，缺失参数，定位为：{accucode}，缺失的参数为：{alarm_i}，出现在节点：{alarm_num}")
                            alarm_t1 = f'{alarm_num},{alarm_i}[不存在]'
                            # with open(self.text_aaa + "big_alarm.txt", mode='a+', encoding='utf-8') as f:
                            #     f.write(f"[{accucode} / {cityname}] - 预警信息缺失参数-[{alarm_i}]-发生节点-[{alarm_num}]\n")
                        else:
                            if len(str(alarm11)) > 0:
                                pass
                            else:
                                print(
                                    f"预警信息，出现为空元素！为空的参数为：{alarm_i}，出现在节点：{alarm_num}")
                                # logger.info(
                                #     f"预警信息，出现为空元素！定位为：{accucode}，为空的参数为：{alarm_i}，出现在节点：{alarm_num}")
                                alarm_t2 = f'{alarm_num},{alarm_i}[为空]'
                                # with open(self.text_aaa + "big_alarm.txt", mode='a+', encoding='utf-8') as f:
                                #     f.write(f"[{accucode} / {cityname}] - 预警信息参数为空-[{alarm_i}]-发生节点-[{alarm_num}]\n")
            else:
                pass

    return alarm_t1, alarm_t2
