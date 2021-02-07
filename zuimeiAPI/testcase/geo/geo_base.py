# coding=<encoding name> ： # coding=utf-8
from util.data_deal import DateDeal

datedeal = DateDeal()
geo_to_name_dic = datedeal.china_dic_geo_name()
geo_code = datedeal.china_dic_geo_code()
geo_province = datedeal.china_dic_geo_province()
geo_zone = datedeal.china_dic_geo_zone()


def geo_base_case(long, lat, data):
    geo_base_t1 = ''
    geo_base_t2 = ''
    geo_base_t3 = ''
    geo_base_t4 = ''

    result_OK = data['resultinfo']
    if result_OK != 'OK':
        pass
    else:
        # 拿 城市名称
        try:
            name_result = data['data']['city']['name']
        except BaseException:
            geo_base_t1 = '无城市名称'
        else:
            print(name_result)
            online_name = geo_to_name_dic[str(long) + '-' + str(lat)]
            if online_name == name_result:
                pass
                # print(name_result)
            else:
                print(f'数据库与返回结果 城市名 不相符，定位为：经度：{long}，纬度：{lat}，服务器城市名为：{online_name},实际接口返回城市名为：{name_result}')
                # logger.info(
                #     f'数据库与返回结果 城市名 不相符，定位为：经度：{long}，纬度：{lat}，服务器城市名为：{online_name},实际接口返回城市名为：{name_result}')
                geo_base_t1 = f'cityname[{online_name},{name_result}]'
                # with open(self.text_aaa + "geo_base.txt", mode='a+', encoding='utf-8') as f:
                #     f.write(f'[{long}-{lat} / {cityname}] - 数据库城市名-[{online_name}]-接口返回城市名-[{name_result}]\n')
            # 判断返回的accucode是否正确
            citycode = data['data']['city']['citycode']
            if geo_code[str(long) + str(lat)] == citycode:
                pass
            else:
                print(
                    f"城市编码返回错误，定位为：经度：{long}，纬度：{lat},数据库城市编码citycode为：{geo_code[str(long) + str(lat)]}")
                # logger.info(
                #     f"城市编码返回错误，定位为：经度：{long}，纬度：{lat},数据库城市编码citycode为：{self.geo_code[str(long)+str(lat)]}，实际接口返回citycode为：{citycode}")
                geo_base_t2 = f'citycode[{geo_code[str(long) + str(lat)]},{citycode}]'
                # with open(self.text_aaa + "geo_base.txt", mode='a+', encoding='utf-8') as f:
                #     f.write(
                #         f"[{long}-{lat} / {cityname}] - 数据库citycode-[{}]-接口返回citycode-[{citycode}]\n")
            # 判断返回的省市县是否正确
            provincename = data['data']['city']['provincename']
            if geo_province[str(long) + str(lat)] == provincename:
                pass
            else:
                print(
                    f"错误，定位为：经度：{long}，纬度：{lat},数据库省市区为：{geo_province[str(long) + str(lat)]}，实际接口返回省市区为：{provincename}")
                geo_base_t3 = f'province[{geo_province[str(long) + str(lat)]},{provincename}]'
                # logger.info( f"错误，定位为：经度：{long}，纬度：{lat},数据库省市区为：{self.geo_province[str(long)+str(lat)]}，实际接口返回省市区为：{
                # provincename}") with open(self.text_aaa + "geo_base.txt", mode='a+', encoding='utf-8') as f: f.write(
                # f"[{long}-{lat} / {cityname}] - 数据库省市区-[{self.geo_province[str(long) + str(lat)]}]-接口返回省市区-[{
                # provincename}]\n")
            # 判断时区是否正确
            timezone = data['data']['city']['timezone']
            if geo_zone[str(long) + str(lat)] == timezone:
                pass
            else:
                print(
                    f"错误，定位为：经度：{long}，纬度：{lat},数据时区为：{geo_zone[str(long) + str(lat)]}，实际接口返回时区为：{timezone}")
                geo_base_t4 = f'timeZone[{geo_zone[str(long) + str(lat)]},{timezone}]'
                # logger.info( f"错误，定位为：经度：{long}，纬度：{lat},数据时区为：{self.geo_zone[str(long) + str(lat)]}，实际接口返回时区为：{
                # timezone}") with open(self.text_aaa + "geo_base.txt", mode='a+', encoding='utf-8') as f: f.write( f"[{
                # long}-{lat} / {cityname}] - 数据库时区-[{self.geo_zone[str(long) + str(lat)]}]-接口返回时区-[{timezone}]\n")
    return geo_base_t1, geo_base_t2, geo_base_t3, geo_base_t4
