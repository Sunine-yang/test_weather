# -*- coding: utf-8 -*-
import os
from tools.logger import Logger
from path_data import Path_data
class Result_check:
    def __init__(self,name):
        self.logger=Logger.report_logger()
        self.test_data_name=name
        self.list_data=[]
    def comparison_check(self,*data):
        try:
            if data[0]==data[1]:
                return ''
            else:
                return data[-1]%(data[1],data[0])

        except Exception as e:
            self.logger.warning(e)

    def comparison_in_check(self,*data):

        try:
            if data[0] in data[1] or data[1] in data[0]:
                return ''
            else:

                return data[-1]%(data[0])

        except Exception as e:
            self.logger.warning(e)

    def comparison_not_in_check(self, *data):
        try:
            if data[0] not in data[1]:
                return data[-1]%data[0]
            else:
                return ''
        except Exception as e:
            self.logger.warning(e)

    def comparison_none_check(self,*data):
        try:
            if data[0] != '' or data[0] != {} or data[0] != [] or data[0] =="":
                return ''
            else:
                return data[-1]%('null')
        except Exception as e:
            self.logger.warning(e)
    def comparison_is_none_check(self,*data):
        try:
            if  data[0] == '' or data[0] == {} or data[0] == [] or data[0] =="":
                return ''
            elif data[0] != None:
                return ''
            else:
                return data[-1]%('null')
        except Exception as e:
            self.logger.warning(e)

    def check_data(self,data):
        try:
            if data[0] != '' or data[0] != {} or data[0] != []:
                return data
            else:
                return data[-1]%'null'

        except Exception as e:
            self.logger.warning(e)

    def days_check(self,*data):
        try:
            if data[0]=='31' or  data[0]=='28' or  data[0]=='30' or data[0]=='29':
                pass
            else:
                return data[-1]
        except:
            pass

    def time_check(self,*data):
        try:
            if int(data[0])==int(data[1]) or int(data[0]-1)==int(data[1]):
                return ''

            else:
                return data[-1]%(data[0],data[1])
        except Exception as e:
            print(e)

    def all_wait_data(self):

        try:
            new_lst = []
            for k in self.list_data:
                if k not in new_lst:
                    new_lst.append(k)
            for i in range(len(new_lst)):
                self.wait_data_log(new_lst[i])
        except:
            pass
    def all_wait_txt_data(self):
        for i in range(len(self.list_data)):
            self.wait_data_log(self.list_data[i])



    def wait_data_log(self,data):
        with open(Path_data.get_path()+'/test_data/test_log_report/%s.txt'%self.test_data_name, 'a+', encoding='utf8') as f:
            f.write(data)
            f.write('\n')
            f.close()


