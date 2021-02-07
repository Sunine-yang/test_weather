#-*-coding:GBK -*-
import os
import time,datetime

from path_data import Path_data


class Data_analysis:

    @classmethod
    def data_extract(self,data):

        result=str(data).split(' ')
        return result[-1]

    @classmethod
    def data_parse(cls,data):
        result1=data.split('℃')
        result2=(result1[0]).split('°/')
        return int(result2[0]),int(result2[1])
    @classmethod
    def data_dispose(cls,data):
        result=data.replace(',','')
        return result
    @classmethod
    def data_time(cls,data):
        pass
    @classmethod
    def data_disposes(cls,data):
        result=data.split(':')
        return result[-1]


    @classmethod
    def data_tree_disposes(cls,data):
        result=data.split('浇')
        result1=result[1].split('次')
        return eval(result1[0])

    @classmethod
    def data_take_out_lin(cls,data):
        result=data.replace(' ','-')
        result1=result.lower()
        return result1

    @classmethod
    def time_disposes(cls,data):
        t1 = time.strptime(data, '%Y-%m-%d %H')
        # 将日期字符串转换为元组
        result=time.mktime(t1)
        return int(result)
    @classmethod
    def time_disposes_int(cls,data):
        t1 = time.strptime(data, '%Y%m%d%H%M')
        # 将日期字符串转换为元组
        result=time.mktime(t1)
        return int(result)

    @classmethod
    def time_transform(cls,data):
        import time
        timeStamp = float(data / 1000)
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%Y-%m-%d %H", timeArray)
        return otherStyleTime

    @classmethod
    def data_delete(cls,document):
        Path_data.get_path()
        path = os.listdir(Path_data.get_path()+"/test_data/test_log_report")
        for i in range(len(path)):
            if '%s.txt'%document == path[i]:
                os.unlink(Path_data.get_path()+"/test_data/test_log_report/%s.txt" % document)
                break
            else:
                pass
    @classmethod
    def document_check(cls, document):
        Path_data.get_path()
        path = os.listdir(Path_data.get_path() + "/test_data/test_log_report")
        for i in range(len(path)):
            if  str(path[i])== '%s.txt'%document:
                return True
    @classmethod
    def data_switch(cls,data):
        if int(data)==9999:
            return 0
        elif int(data) == 0:
            return 9999
        else:
            return data
    @classmethod
    def data_switch_fx(cls,data):
        if data=='9999':
            return '0'
        elif data == '0':
            return '9999'
        else:
            return data

    @classmethod
    def hour_time_handle(cls,data=eval(str(int(time.time())) + '000')):
        timeStamp = float(data / 1000)
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%H", timeArray)
        return int(otherStyleTime)

    @classmethod
    def days_time_handle(cls,data=eval(str(int(time.time())) + '000')):
        timeStamp = float(data / 1000)
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%d", timeArray)
        return otherStyleTime

    @classmethod
    def month_days_check(self):
        data=eval(str(int(time.time()))+'000')
        mooth = {'01': '31','03': '31', '04': '30', '05': '31', '06': '30', '07': '31', '08': '31',
                 '09': '30', '10': '31', '11': '30', '12': '31'}
        timeStamp = float(data / 1000)
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%y", timeArray)
        moonth_s=time.strftime("%m", timeArray)
        if int(otherStyleTime)/4==0:
            mooth.update({"02":"29"})
            return mooth[moonth_s]
        else:
            mooth.update({"02":"28"})
            return mooth[moonth_s]

    @classmethod
    def time_data1(cls,data):
        data_sj = time.strptime(data, "%Y-%m-%d %H:%M:%S")  # 定义格式
        time_int = eval(str(int(time.mktime(data_sj)))+'000')
        return time_int

    @classmethod
    def time_data2(cls,data):  # 传入参数
        data_sj = time.localtime(int(data))
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", data_sj)  # 时间戳转换正常时间
        return time_str

    @classmethod
    def aqi_time(cls):
        time_data=int(str(int(time.time()))+'000')-604957000
        return time_data
if __name__ == '__main__':
  Data_analysis.aqi_time()


