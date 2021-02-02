# coding=<encoding name> ： # coding=utf-8
import os


# 获取当前项目路径
class Path_data:

    @classmethod
    def get_path(cls):
        print = os.path.split(os.path.realpath(__file__))[0]
        return print


