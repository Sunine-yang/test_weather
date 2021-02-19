import os
from path_data import Path_data

class Setup_Istall:
    @classmethod
    def set_up_install(cls):
        libs=open(Path_data.get_path()+'/requirements.txt',"r+").read()
        libs=libs.split("\n")
        print("此次安装的第三方库有：{}".format(libs))
        try:
            for lib in range(len(libs)):
                print(libs)
                os.system("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple " + libs[lib]) #这里我用的是遍历索引的方式，当然也可以直接遍历列表元素！
            print("Successful")
        except:
            print("Failed Somehow")