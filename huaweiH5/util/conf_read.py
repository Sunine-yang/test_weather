from configparser import ConfigParser
from getpathInfo import conf_Path


class ConfRead:

    @classmethod
    def conf_return(cls, confname):
        config = ConfigParser()
        config.read(conf_Path() + confname, encoding="utf-8-sig")
        config.sections()
        return config
