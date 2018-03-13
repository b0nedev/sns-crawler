"""
- youtubekey.py
 - id: youtube api key id
 - key_code: youtube api key
 - crw_id: current assigned crawler id
 - status: youtube api key status(normal/dailyexceed/quotaexceed)
 - sts_chk_at: youtube api key status check time
"""

from datetime import datetime
from pymongo import MongoClient

class YoutubeKey(object):
    def __init__(self):
        self.__youtubekey = dict()
        self.__youtubekey['_id'] = 0
        self.__youtubekey['key_code'] = None
        self.__youtubekey['crw_id'] = 0
        self.__youtubekey['status'] = None
        self.__youtubekey['sts_chk_at'] = None

    @property
    def youtubekey(self):
        return self._YoutubeKey__youtubekey

    @youtubekey.setter
    def youtubekey(self, youtubekey):
        if self.youtubekey.keys() == youtubekey.keys():
            self._YoutubeKey__youtubekey = youtubekey
        else:
            print('required youtubekey class type at youtube')
            raise TypeError

    @property
    def id(self):
        return self.youtubekey['_id']

    @id.setter
    def id(self, id):
        if type(id) != int:
            print('Type err(required int type) at id')
            raise TypeError
        self.youtubekey['_id'] = id

    @property
    def key_code(self):
        return self.youtubekey['key_code']

    @key_code.setter
    def key_code(self, key_code):
        if type(key_code) != str:
            print('Type err(required str type) at key_code')
            raise TypeError
        self.youtubekey['key_code'] = key_code

    @property
    def crw_id(self):
        return self.youtubekey['crw_id']

    @crw_id.setter
    def crw_id(self, crw_id):
        if type(crw_id) != int:
            print('Type err(required int type) at crw_id')
            raise TypeError
        self.youtubekey['crw_id'] = crw_id

    @property
    def status(self):
        return self.youtubekey['status']

    @status.setter
    def status(self, status):
        if type(status) != str:
            print('Type err(required str type) at status')
            raise TypeError
        self.youtubekey['status'] = status

    @property
    def sts_chk_at(self):
        return self.youtubekey['sts_chk_at']

    @sts_chk_at.setter
    def sts_chk_at(self, sts_chk_at):
        if type(sts_chk_at) != datetime:
            print('Type err(required datetime type) at sts_chk_at')
            raise TypeError
        self.youtubekey['sts_chk_at'] = sts_chk_at