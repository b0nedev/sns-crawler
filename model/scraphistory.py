"""
- ScrapHistory class
 - scrap_data model class
 - id: ordering
 - scrap_id: scrap_data number
 - key_id: keyword id
 - crw_id: crawler id
 - created_at: crawler created date
"""
from datetime import datetime
from pymongo import MongoClient
from lib.debug import print_exception_info

class ScrapHistory(object):
    def __init__(self):
        self.__shistory = dict()
        self.__shistory['_id'] = 0
        self.__shistory['scrap_id'] = 0
        self.__shistory['key_id'] = 0
        self.__shistory['crw_id'] = 0
        self.__shistory['created_at'] = None

    @property
    def shistory(self):
        return self._ScrapHistory__shistory

    @shistory.setter
    def shistory(self, shistory):
        if self.shistory.keys() == shistory.keys():
            self._ScrapHistory__shistory = shistory
        else:
            print('required ScrapHistory class type at shistory')
            raise TypeError

    @property
    def id(self):
        return self.shistory['_id']

    @id.setter
    def id(self, id):
        if type(id) != int:
            print('Type err(required int type) at id')
            raise TypeError
        self.shistory['_id'] = id

    @property
    def scrap_id(self):
        return self.shistory['scrap_id']

    @scrap_id.setter
    def scrap_id(self, scrap_id):
        if type(scrap_id) != int:
            print('Type err(required int type) at scrap_id')
            raise TypeError
        self.shistory['scrap_id'] = scrap_id

    @property
    def key_id(self):
        return self.shistory['key_id']

    @key_id.setter
    def key_id(self, key_id):
        if type(key_id) != int:
            print('Type err(required int type) at key_id')
            raise TypeError
        self.shistory['key_id'] = key_id

    @property
    def crw_id(self):
        return self.shistory['crw_id']

    @crw_id.setter
    def crw_id(self, crw_id):
        if type(crw_id) != int:
            print('Type err(required int type) at crw_id')
            raise TypeError
        self.shistory['crw_id'] = crw_id

    @property
    def created_at(self):
        return self.shistory['created_at']

    @created_at.setter
    def created_at(self, created_at):
        if type(created_at) != datetime:
            print('Type err(required datetime type) at created_at')
            raise TypeError
        self.shistory['created_at'] = created_at
"""
- ShistoryMongo class
 - scrap_data mongodb crud class
"""


class ShitoryMongo(ScrapHistory):
    def __init__(self):
        super(__class__, self).__init__()
        self.mongo = ShitoryMongo.g

    @staticmethod
    def connect():
        try:
            mongo = MongoClient('localhost', 27017)
            return mongo
        except Exception as e:
            print_exception_info()

    def close(self):
        self.mongo.close()

    def get_scrap_id(self, crw_id):
        try:
            pass
        except Exception as e:
            print_exception_info()