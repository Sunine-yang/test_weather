#-*-coding:GBK -*-
import json5

class ReadJson:
    @classmethod
    def read_json(cls):

        try:

            with open('../config/base_sql.conf', encoding='utf8') as f:

                cls.contents = json5.load(f)
                print(cls.contents)
            return cls.contents
        except:
            return None

