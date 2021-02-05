import os
from path_data import Path_data

class Delete_fileName:

    @classmethod
    def data_delete(cls,path):
        file = os.listdir(Path_data.get_path() + "/test_data/%s"%path)
        for i in range(len(file)):
            os.unlink(Path_data.get_path() + "/test_data/%s/%s" % (path,file[i]))


if __name__ == '__main__':
    Delete_fileName.data_delete('million_data')