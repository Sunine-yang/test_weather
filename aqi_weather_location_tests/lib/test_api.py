#-*-coding:GBK -*-
import datetime

import requests
from tools.read_yaml import ReadYaml
from tools.logger import Logger
class TestAPI:
    logger=Logger.report_logger()
    session = requests.session()

    @classmethod
    def post(cls, data,requests,baseURL):
        baseURL = ReadYaml.read_yaml()[requests][baseURL]
        try:
            url = baseURL + data['uri']
            headers = data['headers']
            data = data['data']
            resp = cls.session.post(url=url, headers=headers, data=data)
            return resp
        except:
            raise

    @classmethod
    def get(cls,requests,baseURL):
        baseURL = ReadYaml.read_yaml()[requests][baseURL]
        try:
            url = baseURL
            start = datetime.datetime.now()
            cls.logger.info('发送请求')
            resp = cls.session.get(url=url)
            resp.close()
            cls.logger.info('请求发生成功')
            end=datetime.datetime.now()
            time_reault = end - start
            cls.logger.info('请求耗时 %s' % (time_reault))
            return resp
        except:
            raise


    @classmethod
    def get_location(cls,baseURL):
        try:
            url = baseURL
            start = datetime.datetime.now()
            cls.logger.info('发送请求')
            resp = cls.session.get(url=url)
            resp.close()
            cls.logger.info('请求发生成功')
            end = datetime.datetime.now()
            time_reault = end - start
            cls.logger.info('请求耗时 %s' % (time_reault))
            return resp
        except:
            cls.get_location()

    @classmethod
    def get_location_tf(cls,baseURL):
        try:
            url = baseURL
            start = datetime.datetime.now()
            cls.logger.info('发送请求')
            resp = cls.session.get(url=url)
            result=resp.text
            cls.logger.info('请求发生成功')
            end = datetime.datetime.now()
            time_reault = end - start
            cls.logger.warning('请求耗时 %s' % (time_reault))
            return result
        except:
            raise



