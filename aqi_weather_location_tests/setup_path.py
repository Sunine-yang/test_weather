#-*-coding:GBK -*-
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from path_data import Path_data
class Setup_Istall:
    @classmethod
    def set_up_install(cls):
        libs=open(Path_data.get_path()+'/requirements.txt',"r+").read()
        libs=libs.split("\n")
        print("此次安装的第三方库有：{}".format(libs))
        try:
            for lib in range(len(libs)):
                os.system("pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple " + libs[lib])
            print("Successful")
        except:
            print("Failed Somehow")