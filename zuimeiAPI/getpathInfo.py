# coding=<encoding name> ： # coding=utf-8
import os


# 获取当前项目路径
def get_Path():
    path = os.path.split(os.path.realpath(__file__))[0]
    # log_file = get_Path() + "\log"
    # print(log_file)
    return path


# 获取当前日志路径
def log_Path():
    path = get_Path() + "\\log\\"
    return path


# 获取当前配置文件路径
def conf_Path():
    path = get_Path() + "\\config\\"
    return path


# 获取当前数据路径
def data_Path():
    path = get_Path() + "\\data\\"
    return path

def text_Path():
    path = get_Path() + "\\text\\"
    return path

if __name__ == '__main__':  # 执行该文件，测试下是否OK
    print('测试路径是否OK,路径为：', get_Path())
    print('测试路径是否OK,log路径为：', log_Path())
    print(conf_Path())
    print(data_Path())
    # print(type(get_Path()))
