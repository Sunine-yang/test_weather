#-*-coding:GBK -*-
import json

from path_data import Path_data

class Write_Read_Json:

    @classmethod
    def write_json(cls,*data):
        with open(Path_data.get_path() + '/test_data/%s.json'%data[0] , 'w+') as f:
            json.dump(data[1], f)
            f.close()

    @classmethod
    def read_json(cls,*data):
        with open(Path_data.get_path() + '/test_data/%s.json'%data[0] , 'r') as f:
            load_dict = json.load(f, strict=False)
            return load_dict





