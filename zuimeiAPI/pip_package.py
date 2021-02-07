import os

from getpathInfo import get_Path

path = get_Path()
with open(path + '\\requirements.txt', 'r', ) as f:
    con = f.readlines()


try:
    for i in con:
        os.system("pip install " + i.replace('\n', ''))
        print('pip ok')
except BaseException:
    print('pip erro')

