# coding=<encoding name> ： # coding=utf-8
import yaml

from util.conf_read import ConfRead
from util.timestamp_deal import houraqi_time

houraqi_list = ConfRead.conf_get('big.conf', 'houraqi_list', 'houraqi_list')
houraqi_re_list = yaml.load(houraqi_list, Loader=yaml.FullLoader)


def big_hourlysAqi_case(data):
    hourlysaqi_t1 = ''
    hourlysaqi_t2 = ''
    hourlysaqi_t3 = ''
    hourlysaqi_t4 = ''
    hourlysaqi_t5 = ''
    hourlysaqi_t6 = ''

    result_OK = data['resultinfo']
    # 判断接口是否异常
    if result_OK != 'OK':
        pass

    # 城市信息是否正确
    else:
        try:
            aaaa = data['data']['hourAqi']
        except BaseException:
            hourlysaqi_t1 = '无小时空气质量'
        else:

            # 小时空气质量 hourAqi
            # 168个
            # 第一个时间，与当前时间不超过一小时
            try:
                houraqi_firsttime = data['data']['hourAqi'][0]['time']
            except BaseException:
                hourlysaqi_t1 = '无第一个时间'
                # with open(self.text_aaa + "big_houraqi.txt", mode='a+', encoding='utf-8') as f:
                #     f.write(f"[{accucode} / {cityname}] - 小时空气质量无第一个时间\n")
            else:
                # 返回1为小于60min
                houraqi_firsttime_answ = houraqi_time(houraqi_firsttime)
                if houraqi_firsttime_answ == 1:
                    pass
                else:
                    print(f"小时空气质量与当前时差大于1小时-")
                    hourlysaqi_t2 = '与当前时差大于1小时'
                    # with open(self.text_aaa + "big_houraqi.txt", mode='a+', encoding='utf-8') as f:
                    #     f.write(f"[{accucode} / {cityname}] - 小时空气质量与当前时差大于1小时\n")
            # 参数列表

            try:
                houraqi_len = data['data']['hourAqi']
            except BaseException:
                print(f"无小时空气质量")
                hourlysaqi_t3 = '无小时空气质量'
                # with open(self.text_aaa + "big_houraqi.txt", mode='a+', encoding='utf-8') as f:
                #     f.write(f"[{accucode} / {cityname}] - 无小时空气质量\n")
            else:
                # 判断是否168
                if len(houraqi_len) == 168:
                    pass
                else:
                    print(f"小时空气质量-数量-[{len(houraqi_len)}]")
                    hourlysaqi_t4 = f'{len(houraqi_len)}[应为168个参数]'
                    # with open(self.text_aaa + "big_houraqi.txt", mode='a+', encoding='utf-8') as f:
                    #     f.write(f"[{accucode} / {cityname}] - 小时空气质量-数量-[{len(houraqi_len)}]\n")

                # 遍历
                for h_num in range(0, len(houraqi_len)):
                    for h_w in houraqi_re_list:
                        try:
                            houraqi11 = data['data']['hourAqi'][h_num][h_w]
                        except BaseException:
                            print(f"小时空气质量缺失参数-[{h_w}]-发生节点-[{h_num}]")
                            hourlysaqi_t5 = f'{h_num},{h_w}[不存在]'
                            # with open(self.text_aaa + "big_houraqi.txt", mode='a+', encoding='utf-8') as f:
                            #     f.write(f"[{accucode} / {cityname}] - 小时空气质量缺失参数-[{h_w}]-发生节点-[{h_num}]\n")
                        else:
                            if len(str(houraqi11)) > 0:
                                pass
                            else:
                                print(f"小时空气质量参数为空-[{h_w}]-发生节点-[{h_num}]")
                                hourlysaqi_t6 = f'{h_num},{h_w}[为空]'
                                # with open(self.text_aaa + "big_houraqi.txt", mode='a+', encoding='utf-8') as f:
                                #     f.write(f"[{accucode} / {cityname}] - 小时空气质量参数为空-[{h_w}]-发生节点-[{h_num}]\n")
    return hourlysaqi_t1, hourlysaqi_t2, hourlysaqi_t3, hourlysaqi_t4, hourlysaqi_t5, hourlysaqi_t6
