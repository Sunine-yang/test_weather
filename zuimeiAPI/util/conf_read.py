# coding=<encoding name> ： # coding=utf-8
import configparser
from getpathInfo import conf_Path


class ConfRead:

    @classmethod
    def conf_return(cls, confname):
        config = configparser.RawConfigParser()
        config.read(conf_Path() + confname, encoding="utf-8-sig")
        config.sections()
        return config

    @classmethod
    def conf_key(cls):
        con = cls.conf_return('APIkey.conf')
        key = con.get('APIkey', 'key')
        return key

    @classmethod
    def conf_get(cls, filename, section, name):
        con = cls.conf_return(filename)
        data = con.get(section, name)
        return data



if __name__ == '__main__':
    a = ConfRead()
    print(a.conf_key())
