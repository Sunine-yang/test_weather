#-*-coding:GBK -*-
import yaml
from path_data import Path_data


class ReadYaml:


    @classmethod
    def read_yaml(cls,data):
        filepath=Path_data.get_path() + '/config/%s.yaml' % data
        with open(filepath, encoding='utf8') as f:
            content = f.read()
            result=yaml.load(content)
        return result

if __name__ == '__main__':
    print(ReadYaml.read_yaml('guangzhou'))
