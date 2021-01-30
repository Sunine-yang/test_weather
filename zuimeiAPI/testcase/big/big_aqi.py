# coding=<encoding name> ： # coding=utf-8
import yaml

from util.conf_read import ConfRead
from util.timestamp_deal import ts_deal, hourlys_time_deal

aqi_now_conf = ConfRead.conf_get('big.conf', 'aqi_now_list', 'aqi_now_list')
aqi_now_list = yaml.load(aqi_now_conf, Loader=yaml.FullLoader)


def big_aqi_case(data):
    aqi_t1 = ''
    aqi_t2 = ''
    aqi_t3 = ''
    aqi_t4 = ''
    aqi_t5 = ''

    result_OK = data['resultinfo']
    # 判断接口是否异常
    if result_OK != 'OK':
        pass

    # 城市信息是否正确
    else:
        # 实时空气质量
        # updatetime 与当前时间 两小时判定
        aqi_now = data['data']['aqi']['updatetime']
        aqi_now_time = ts_deal(aqi_now)
        aqi_time = hourlys_time_deal(aqi_now)
        if aqi_now_time > 2:
            print(f"实时空气质量，updatetime 与当前时间 两小时判定错误!")
            # logger.info(f"实时空气质量，updatetime 与当前时间 两小时判定错误！定位为：{accucode}")
            aqi_t1 = f'{aqi_time}[时间差大于两小时]'
            # with open(self.text_aaa + "big_aqi.txt", mode='a+', encoding='utf-8') as f:
            #     f.write(f"[{accucode} / {cityname}] - 实时空气质量两小时时间差-[{aqi_now}]\n")
        else:
            pass
        # 判断不为空

        try:
            aqi_len = len(data['data']['aqi'])
        except BaseException:
            print(f'此城市没有aqi')
            # logger.info(f'此城市没有aqi，定位为：{accucode}')
            aqi_t2 = f'aqi[不存在]'
            # with open(self.text_aaa + "big_aqi.txt", mode='a+', encoding='utf-8') as f:
            #     f.write(f'[{accucode} / {cityname}] - 无参数[aqi]\n')
        else:
            if aqi_len >= 8:
                pass
            else:
                print(f"实时空气质量，应该是13个参数，实际为：{len(data['data']['aqi'])}个！")
                # logger.info(f"实时空气质量，应该是13个参数，实际为：{len(data['data']['aqi'])}个！定位为：{accucode}")
                aqi_t3 = f"{len(data['data']['aqi'])}[实时空气质量参数数量13]"
                # with open(self.text_aaa + "big_aqi.txt", mode='a+', encoding='utf-8') as f:
                #     f.write(f"[{accucode} / {cityname}] - 实时空气质量参数数量-[{len(data['data']['aqi'])}]\n")

        for aqi_now_i in aqi_now_list:
            try:
                aqi_now_data = data['data']['aqi'][aqi_now_i]
            except BaseException:
                print(f"实时空气质量，参数缺失，缺失的参数为{aqi_now_i}")
                # logger.info(f"实时空气质量，参数缺失！定位为：{accucode}，缺失的参数为{aqi_now_i}")
                aqi_t4 = f'{aqi_now_i}[不存在]'
                # with open(self.text_aaa + "big_aqi.txt", mode='a+', encoding='utf-8') as f:
                #     f.write(f"[{accucode} / {cityname}] - 实时空气质量缺失参数-[{aqi_now_i}]\n")
            else:
                if len(str(aqi_now_data)) > 0:
                    pass
                else:
                    print(f"实时空气质量，出现为空元素！为空的参数为{aqi_now_i}")
                    # logger.info(f"实时空气质量，出现为空元素！定位为：{accucode}，为空的参数为{aqi_now_i}")
                    aqi_t5 = f'{aqi_now_i}[为空]'
                    # with open(self.text_aaa + "big_aqi.txt", mode='a+', encoding='utf-8') as f:
                    #     f.write(f"[{accucode} / {cityname}] - 实时空气质量参数为空-[{aqi_now_i}]\n")
    return aqi_t1, aqi_t2, aqi_t3, aqi_t4, aqi_t5
