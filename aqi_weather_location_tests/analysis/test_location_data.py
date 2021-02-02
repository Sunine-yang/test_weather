#-*-coding:GBK -*-

from path_data import Path_data
from tools.easy_mysql import EasyMysql
from tools.read_yaml import ReadYaml
class Test_Loction_data:

    sql=ReadYaml.read_yaml()['requests_two']['sql']
    @classmethod
    def with_data(cls):
        result1=EasyMysql.query_all(cls.sql)
        with open(Path_data.get_path()+'/test_data/location.txt','w+',encoding='utf8') as f:
            f.write(str(result1))
            f.close()
    @classmethod
    def read_data(cls):
        with open(Path_data.get_path()+'/test_data/location.txt' , 'r', encoding='utf8') as f:
            result = f.readlines()
            return result



if __name__ == '__main__':
    print(Test_Loction_data.read_data())
