#-*-coding:GBK -*-

from path_data import Path_data


class Write_Data_txt:

    @classmethod
    def write_data(cls,*data):
        with open(Path_data.get_path()+'/test_data/%s.txt'%data[0],data[1],encoding='utf8') as f :
            f.write(data[2])
            f.close()

    @classmethod
    def read_data(cls,*data):
        with open(Path_data.get_path()+'/test_data/%s.txt'%data[0],'r',encoding='utf8') as f:
            result=f.read()
            return result

    @classmethod
    def read_data_readline(cls,*data):
        with open(Path_data.get_path() + '/test_data/%s.txt' % data[0], 'r', encoding='utf8') as f:
            result = f.readline()
            return eval(result)

if __name__ == '__main__':
    datas=Write_Data_txt.read_data_readline('sql_data/20000')
    print(datas)