#-*-coding:GBK -*-
import os


class Path_data:

    @classmethod
    def get_path(cls):
        print = os.path.split(os.path.realpath(__file__))[0]
        return print


