# coding=<encoding name> ： # coding=utf-8
import requests
from log.Log import logger
from util.conf_read import ConfRead

logger = logger


class RunMain:
    def __init__(self):
        pass

    def send_post(self, url, data):  # 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入
        result = requests.request(url=url, data=data,
                                  method="POST")  # 因为这里要封装post方法，所以这里的url和data值不能写死
        # res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return result

    def send_get(self, url, params):
        # session = requests.Session()
        result = requests.request(url=url, params=params, method="GET")
        # res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return result

    def run_main(self, method, url=None, data=None):  # 定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None
        if method == 'POST':
            result = self.send_post(url, data)
            # logger.info(str(result))
        elif method == 'GET':
            # try:
            result = self.send_get(url, data)
            # except BaseException:
            #     with open("big_wait_time.txt", mode='a+', encoding='utf-8') as f:
            #         f.write(f'[{data}] - 响应时间- 大于 2s \n')
            #     print('大于2s')
            # else:
            #     time = result.elapsed.total_seconds()
            #     print(f'发送请求到服务端响应,时间为：{time}')
            # logger.info(str(result))
        else:
            print("method值错误！！！")
            logger.info("method值错误！！！")
        return result


if __name__ == '__main__':  # 通过写死参数，来验证我们写的请求是否正确
    url = f'http://139.159.198.98/pubDataServer/getweatherpub?apikey={ConfRead.conf_key()}&citycode=1921951&language=zh_CNchl=&codeType=1'
    url1 = 'http://www.google.com.hk'
    url2 = 'http://139.159.198.98/pubDataServer/getweatherdailys?apikey=0710d94cebb4248a38edef859d11ab35&start=20210128&end=20210429&citycode=9999996'
    result = RunMain().run_main('GET', url2)
    print(result)
    a = result
    print(a)
    print()
    data = result.json()
    print(data)
    # time0 = data["data"]['dailys']['dailyweathers'][0]['publictime']
    # print(time0)
    # print(type(time0))

