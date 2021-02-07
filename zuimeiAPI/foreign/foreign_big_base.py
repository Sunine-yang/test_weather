# coding=<encoding name> ： # coding=utf-8
# 城市基本信息 是否正确
from util.foreign_data_deal import ForeignDateDeal

datedeal = ForeignDateDeal()
dic_code_name, dic_citycode, dic_province, dic_timeZone = datedeal.foreign_dic_code_name()
code_to_name_dic = dic_code_name
citycode_dic = dic_citycode
province_dic = dic_province
timeZone_dic = dic_timeZone


def foreign_big_base_case(accucode, data):
    big_base_t1 = ''
    big_base_t2 = ''
    big_base_t3 = ''
    big_base_t4 = ''
    result_OK = data['resultinfo']
    # 判断接口是否异常
    if result_OK != 'OK':
        pass

    # 城市信息是否正确
    else:
        # 拿 城市名称
        try:
            name_result = data['data']['city']['name']
        except BaseException:
            big_base_t1 = '无城市名称'
        else:
            print(name_result)
            # 判断返回的城市名称是否正确
            if code_to_name_dic[str(accucode)] == name_result:
                pass
            else:
                print(f'数据库城市名-[{code_to_name_dic[accucode]}]-接口返回城市名-[{name_result}]-定位-[{accucode}]')
                # logger.info(f'错误，定位为：{accucode},数据库城市名为：{self.code_to_name_dic[accucode]}，实际接口返回城市名为：{name_result}')
                big_base_t1 = f'cityname[{code_to_name_dic[accucode]},{name_result}]'
                # with open(self.text_aaa + "big_base.txt", mode='a+', encoding='utf-8') as f:
                #     f.write(
                #         f'[{accucode} / {cityname}] - 数据库城市名-[{}]-接口返回城市名-[{}]\n')
            # 判断返回的accucode是否正确
            citycode = data['data']['city']['citycode']
            if citycode_dic[str(accucode)] == citycode:
                pass
            else:
                print(
                    f"错误，定位为：{accucode},数据库城市编码citycode为：{citycode_dic[accucode]}，实际接口返回citycode为：{citycode}")
                # logger.info(
                #     f"错误，定位为：{accucode},数据库城市编码citycode为：{self.citycode_dic[accucode]}，实际接口返回citycode为：{citycode}")
                big_base_t2 = f'cityaccucode[{citycode_dic[accucode]},{citycode}]'
                # with open(self.text_aaa + "big_base.txt", mode='a+', encoding='utf-8') as f: f.write( f'[{accucode}
                # / {cityname}] - 数据库citycode-[{self.citycode_dic[accucode]}]-接口返回citycode-[{citycode}]\n')
            # 判断返回的省市县是否正确
            provincename = data['data']['city']['provincename']
            if province_dic[str(accucode)] == provincename:
                pass
            else:
                print(
                    f"错误，定位为：{accucode},数据库省市区为：{province_dic[accucode]}，实际接口返回省市区为：{provincename}")
                # logger.info(
                #     f"错误，定位为：{accucode},数据库省市区为：{self.province_dic[accucode]}，实际接口返回省市区为：{provincename}")
                big_base_t3 = f'province[{province_dic[accucode]},{provincename}]'
                # with open(self.text_aaa + "big_base.txt", mode='a+', encoding='utf-8') as f:
                #     f.write(
                #         f'[{accucode} / {cityname}] - 数据库省市区-[{self.province_dic[accucode]}]-接口返回省市区-[{provincename}]\n')
            # 判断时区是否正确
            timezone = data['data']['city']['timezone']
            if timeZone_dic[str(accucode)] == timezone:
                pass
            else:
                print(
                    f"错误，定位为：{accucode},数据时区为：{timeZone_dic[accucode]}，实际接口返回时区为：{timezone}")
                # logger.info(
                #     f"错误，定位为：{accucode},数据时区为：{self.timeZone_dic[accucode]}，实际接口返回时区为：{timezone}")
                big_base_t4 = f'timeZone[{timeZone_dic[accucode]},{timezone}]'
                # with open(self.text_aaa + "big_base.txt", mode='a+', encoding='utf-8') as f: f.write(f'[{accucode}
                # / {cityname}] - 数据库时区-[{self.timeZone_dic[accucode]}]-接口返回时区-[{timezone}]\n')

    return big_base_t1, big_base_t2, big_base_t3, big_base_t4
