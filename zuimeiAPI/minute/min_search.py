# coding=<encoding name> ： # coding=utf-8
from common.configHTTP import RunMain
from getpathInfo import text_Path
from util.conf_read import ConfRead
from log.Log import logger

logger = logger


class MinSearch:
    def __init__(self):
        self.text_aaa = text_Path()

    # 城市编码校验城市名称
    # 城市编码 接口校验 ok or server error!
    def min_search_api(self):
        # 搜索
        erro_name = 0
        Sensitive_city_list = {'钓鱼岛': 1, '永兴岛': 1, '苏岩礁': 1}
        city_list = {'石拐区': 1, '竹安里': 1, '布鲁塞尔': 32, '北京市': 53, 'Darisiyeh': 1}
        with open(self.text_aaa + "min_search.txt", mode='a+', encoding='utf-8') as f:
            f.write(
                f'------------------------- 测 试 城 市 ----------------------------\n测试城市敏感城市为：钓鱼岛，永兴岛，苏岩礁\n测试城市普通城市为：石拐区，竹安里，布鲁塞尔，北京市，Darisiyeh\n------------------------------------------------------------------\n')
        # 敏感城市
        for key, value in Sensitive_city_list.items():
            search_api = f'http://139.159.198.98/vivoDbServer/searchcitypub?q={key}&apikey={ConfRead.conf_key()}'
            # 发送GET请求
            result = RunMain().run_main('GET', search_api)
            # 拿JSON
            data = result.json()
            a = data['citys']
            b = data['resultcode']
            if b != 0:
                if len(a) == value:
                    pass
                else:
                    erro_name += 1
                    print(f"搜索API返回数据个数与规定不不相符, 定位为：{key}")
                    # logger.info(f"搜索API返回数据个数与规定不不相符, 返回为server error，定位为：{key}")
                    with open(self.text_aaa + "min_search.txt", mode='a+', encoding='utf-8') as f:
                        f.write(f'[{key}]-server error或返回个数错误\n')

                # 判断是否为空
                city_i_list1 = ['citycode', 'localizedname', 'type', 'scenicLevel']
                for city_list_num in range(0, value):
                    for i in city_i_list1:
                        if len(data['citys'][city_list_num][i]) > 0:
                            pass
                        else:
                            erro_name += 1
                            print(f"搜索API接口有参数为空！, 定位为：{key}，为空的参数为：{i},出现的节点为：{city_list_num}")
                            # logger.info(f"搜索API接口有参数为空！, 定位为：{key}，为空的参数为：{i},出现的节点为：{city_list_num}")
                            with open(self.text_aaa + "min_search.txt", mode='a+', encoding='utf-8') as f:
                                f.write(f'[{key}] - 参数为空-[{i}]-发生节点-[{city_list_num}]\n')

                for city_list_num in range(0, value):
                    if len(data['citys'][city_list_num]['timezone']['name']) > 0:
                        pass
                    else:
                        erro_name += 1
                        print(f"搜索API接口有参数为空！, 定位为：{key}，为空的参数为：name,出现的节点为：{city_list_num}")
                        # logger.info(f"搜索API接口有参数为空！, 定位为：{key}，为空的参数为：name,出现的节点为：{city_list_num}")
                        with open(self.text_aaa + "min_search.txt", mode='a+', encoding='utf-8') as f:
                            f.write(f'[{key}] - [name]参数为空-发生节点-[{city_list_num}]\n')
                    if len(data['citys'][city_list_num]['geoposition']['longitude']) > 0:
                        if len(data['citys'][city_list_num]['geoposition']['latitude']) > 0:
                            pass
                        else:
                            erro_name += 1
                            print(f"搜索API接口有参数为空！, 定位为：{key}，为空的参数为：latitude,出现的节点为：{city_list_num}")
                            # logger.info(f"搜索API接口有参数为空！, 定位为：{key}，为空的参数为：latitude,出现的节点为：{city_list_num}")
                            with open(self.text_aaa + "min_search.txt", mode='a+', encoding='utf-8') as f:
                                f.write(f'[{key}] - [latitude]参数为空-发生节点-[{city_list_num}]\n')

                    else:
                        erro_name += 1
                        print(f"搜索API接口有参数为空！, 定位为：{key}，为空的参数为：longitude,出现的节点为：{city_list_num}")
                        # logger.info(f"搜索API接口有参数为空！, 定位为：{key}，为空的参数为：longitude,出现的节点为：{city_list_num}")
                        with open(self.text_aaa + "min_search.txt", mode='a+', encoding='utf-8') as f:
                            f.write(f'[{key}] - [latitude]参数为空-发生节点-[{city_list_num}]\n')

            else:
                erro_name += 1
                print(b)
                print(f"搜索API接口无返回！, 定位为：{key}")
                # logger.info(f"搜索API接口无返回！, 返回为server error，定位为：{key}")
                with open(self.text_aaa + "min_search.txt", mode='a+', encoding='utf-8') as f:
                    f.write(f'[{key}] - 搜索server error\n')

        # 正常城市
        for key, value in city_list.items():
            search_api = f'http://139.159.198.98/vivoDbServer/searchcitypub?q={key}&apikey={ConfRead.conf_key()}'
            # 发送GET请求
            result = RunMain().run_main('GET', search_api)
            # 拿JSON
            data = result.json()
            a = data['citys']
            b = data['resultcode']
            if b != 0:
                if len(a) == value:
                    pass
                else:
                    erro_name += 1
                    print(f"搜索API返回数据个数与规定不不相符, 定位为：{key}")
                    # logger.info(f"搜索API返回数据个数与规定不不相符, 返回为server error，定位为：{key}")
                    with open(self.text_aaa + "min_search.txt", mode='a+', encoding='utf-8') as f:
                        f.write(f'[{key}] - server error或返回个数错误\n')

                # 判断是否为空
                city_i_list1 = ['citycode', 'localizedname', 'type', 'scenicLevel']
                for city_list_num in range(0, value):
                    for i in city_i_list1:
                        if len(data['citys'][city_list_num][i]) > 0:
                            pass
                        else:
                            erro_name += 1
                            print(f"搜索API接口有参数为空！, 定位为：{key}，为空的参数为：{i},出现的节点为：{city_list_num}")
                            # logger.info(f"搜索API接口有参数为空！, 定位为：{key}，为空的参数为：{i},出现的节点为：{city_list_num}")
                            with open(self.text_aaa + "min_search.txt", mode='a+', encoding='utf-8') as f:
                                f.write(f'[{key}] - 搜索参数为空-[{i}]-发生节点-[{city_list_num}]\n')

                for city_list_num in range(0, value):
                    if len(data['citys'][city_list_num]['timezone']['name']) > 0:
                        pass
                    else:
                        erro_name += 1
                        print(f"搜索API接口有参数为空！, 定位为：{key},为空的参数为：name")
                        # logger.info(f"搜索API接口有参数为空！, 定位为：{key},为空的参数为：name")
                        with open(self.text_aaa + "min_search.txt", mode='a+', encoding='utf-8') as f:
                            f.write(f'[{key}] - 搜索[name]参数为空-发生节点-[{city_list_num}]\n')
                    if len(data['citys'][city_list_num]['geoposition']['longitude']) > 0:
                        if len(data['citys'][city_list_num]['geoposition']['latitude']) > 0:
                            pass
                        else:
                            erro_name += 1
                            print(f"搜索API接口有参数为空！, 定位为：{key},为空的参数为latitude")
                            # logger.info(f"搜索API接口有参数为空！, 定位为：{key},为空的参数为latitude")
                            with open(self.text_aaa + "min_search.txt", mode='a+', encoding='utf-8') as f:
                                f.write(f'[{key}] - 搜索[latitude]参数为空-发生节点-[{city_list_num}]\n')
                    else:
                        erro_name += 1
                        print(f"搜索API接口有参数为空！, 定位为：{key},为空的参数为longitude")
                        # logger.info(f"搜索API接口有参数为空！, 定位为：{key},为空的参数为longitude")
                        with open(self.text_aaa + "min_search.txt", mode='a+', encoding='utf-8') as f:
                            f.write(f'[{key}] - 搜索[latitude]参数为空-发生节点-[{city_list_num}]\n')

                    # if len(data['citys'][city_list_num]['administrativearea']['id']) > 0:
                    #     if len(data['citys'][city_list_num]['administrativearea']['localizedname']) > 0:
                    #         pass
                    #     else:
                    #         print(f"搜索API接口有参数为空！, 定位为：{key}为空的参数为：localizedname")
                    #         # logger.info(f"搜索API接口有参数为空！, 定位为：{key}localizedname")
                    #         with open(self.text_aaa + "search.txt", mode='a+', encoding='utf-8') as f:
                    #             f.write(f'[{key}] - 搜索[localizedname]参数为空-发生节点-[{city_list_num}]\n')
                    # else:
                    #     print(f"搜索API接口有参数为空！, 定位为：{key}。为空的参数为：id")
                    #     # logger.info(f"搜索API接口有参数为空！, 定位为：{key}。为空的参数为：id")
                    #     with open(self.text_aaa + "search.txt", mode='a+', encoding='utf-8') as f:
                    #         f.write(f'[{key}] - 搜索[id]参数为空-发生节点-[{city_list_num}]\n')

                    if len(data['citys'][city_list_num]['country']['id']) > 0:
                        if len(data['citys'][city_list_num]['country']['localizedname']) > 0:
                            pass
                        else:
                            erro_name += 1
                            print(f"搜索API接口有参数为空！, 定位为：{key}。为空的参数为：localizedname")
                            # logger.info(f"搜索API接口有参数为空！, 定位为：{key}为空的参数为：localizedname")
                            with open(self.text_aaa + "min_search.txt", mode='a+', encoding='utf-8') as f:
                                f.write(f'[{key}] - 搜索[localizedname]参数为空-发生节点-[{city_list_num}]\n')
                    else:
                        erro_name += 1
                        print(f"搜索API接口有参数为空！, 定位为：{key}。为空的参数为：id")
                        # logger.info(f"搜索API接口有参数为空！, 定位为：{key}。为空的参数为：id")
                        with open(self.text_aaa + "min_search.txt", mode='a+', encoding='utf-8') as f:
                            f.write(f'[{key}] - 搜索[id]参数为空-发生节点-[{city_list_num}]')

            else:
                erro_name += 1
                print(b)
                print(f"搜索API接口无返回！, 定位为：{key}")
                # logger.info(f"搜索API接口无返回！, 返回为server error，定位为：{key}")
                with open(self.text_aaa + "min_search.txt", mode='a+', encoding='utf-8') as f:
                    f.write(f'[{key}] - 搜索server error\n')

        if erro_name >= 1:
            with open(self.text_aaa + "min_search_erro_citynum.txt", mode='a+', encoding='utf-8') as f:
                f.write(
                    f"{erro_name}" + "\n")
            return 1
        else:
            return 2


if __name__ == '__main__':
    pass

