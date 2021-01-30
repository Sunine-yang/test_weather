# coding=<encoding name> ： # coding=utf-8
import yaml

from util.conf_read import ConfRead
from util.timestamp_deal import ts_deal, hourlys_time_deal

condition_list = ConfRead.conf_get('big.conf', 'condition_list', 'condition_list')
condition_re_list = yaml.load(condition_list, Loader=yaml.FullLoader)


def big_condition_case(data):
    big_condition_t1 = ''
    big_condition_t2 = ''
    big_condition_t3 = ''
    big_condition_t4 = ''
    result_OK = data['resultinfo']
    # 判断接口是否异常
    if result_OK != 'OK':
        pass
    # 城市信息是否正确
    else:
        # 实况天气
        if len(data['data']['condition']) == 28:
            pass
        else:
            print(f"实况天气，参数数量不对，参数应该为28个，现在参数为：{len(data['data']['condition'])}")
            # logger.info(f"实况天气，参数数量不对，参数应该为28个，现在参数为：{len(data['data']['condition'])}。定位为：{accucode}")
            big_condition_t1 = f"返回参数个数应为28-[{len(data['data']['condition'])}]"
            # with open(self.text_aaa + "big_condition.txt", mode='a+', encoding='utf-8') as f:
            #     f.write(f"[{accucode} / {cityname}] - \n")

        for i in condition_re_list:
            try:
                condition_oh = str(data['data']['condition'][i])
            except BaseException:
                print(f"实况天气，参数缺失，缺失的参数为{i}")
                # logger.info(f"实况天气，参数缺失，定位为：{accucode}，缺失的参数为{i}")
                big_condition_t2 = f'{i}[不存在]'
                # with open(self.text_aaa + "big_condition.txt", mode='a+', encoding='utf-8') as f:
                #     f.write(f"[{accucode} / {cityname}] - 缺失参数-[{i}]\n")
            else:
                if len(condition_oh) > 0:
                    pass
                else:
                    print(f"实况天气，出现为空元素！为空的参数为{i}")
                    # logger.info(f"实况天气，出现为空元素！定位为：{accucode}，为空的参数为{i}")
                    big_condition_t3 = f'{i}[为空]'
                    # with open(self.text_aaa + "big_condition.txt", mode='a+', encoding='utf-8') as f:
                    #     f.write(f"[{accucode} / {cityname}] - 实况天气-[{i}]-参数为空\n")

        # updatetime 时间戳校验
        # 时间戳
        timestamp = data['data']['condition']['updatetime']
        c = ts_deal(timestamp)
        if c < 1:
            pass
        else:
            print(f"实况天气，时间戳大于现在时间一小时！")
            # logger.info(f"实况天气，时间戳大于现在时间一小时！定位为：{accucode}")
            big_condition_t4 = f'日期-{hourlys_time_deal(timestamp)}-[大于现在时间一小时]'
            # with open(self.text_aaa + "big_condition.txt", mode='a+', encoding='utf-8') as f:
            #     f.write(f"[{accucode} / {cityname}] - 实况天气日期-[{hourlys_time_deal(timestamp)}]-大于现在时间一小时\n")

    return big_condition_t1, big_condition_t2, big_condition_t3, big_condition_t4
