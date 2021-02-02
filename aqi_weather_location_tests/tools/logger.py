#-*-coding:GBK -*-
import logging

from path_data import Path_data


class Logger:

    logger = None
    @classmethod
    def get_ctime_str(cls):
        """
            返回规定格式的时间字符串
        :param : 无
        :return: 时间字符串
        """
        import time
        return time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
    @classmethod
    def report_logger(cls):
        """
                    返回规定格式的日志生成器对象
                :return: 日志生成器对象
                """
        if cls.logger is None:
            # 得到生成器对象
            cls.logger = logging.getLogger()
            # 定义该logger所支持的日志级别
            cls.logger.setLevel(level=logging.INFO)
            # 创建logger的文件句柄与规定的文件关联
            handler = logging.FileHandler(Path_data.get_path()+'/logs/' +cls.get_ctime_str()+ '.log', encoding='utf8')
            # 定义信息的格式
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            cls.logger.addHandler(handler)


        return cls.logger


