#-*-coding:GBK -*-
import logging

from path_data import Path_data


class Logger:

    logger = None
    @classmethod
    def get_ctime_str(cls):
        """
            ���ع涨��ʽ��ʱ���ַ���
        :param : ��
        :return: ʱ���ַ���
        """
        import time
        return time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
    @classmethod
    def report_logger(cls):
        """
                    ���ع涨��ʽ����־����������
                :return: ��־����������
                """
        if cls.logger is None:
            # �õ�����������
            cls.logger = logging.getLogger()
            # �����logger��֧�ֵ���־����
            cls.logger.setLevel(level=logging.INFO)
            # ����logger���ļ������涨���ļ�����
            handler = logging.FileHandler(Path_data.get_path()+'/logs/' +cls.get_ctime_str()+ '.log', encoding='utf8')
            # ������Ϣ�ĸ�ʽ
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            cls.logger.addHandler(handler)


        return cls.logger


