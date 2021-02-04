

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