"""
crawler.py
 - crawler model
 - id : crawler id
 - key_id : keyword id
 - p_id: process id
 - server: server ip and account(accunt@ip)
 - state: crawler state(created/running/stoped/termiated)
 - platform: youtube/instagram/twitter
 - mode: tag/user
"""
from lib.debug import print_exception_info
from pymongo import MongoClient


class Crawler(object):
    def __init__(self):
        self.__crawler = dict()
        self.__crawler['_id'] = 0
        self.__crawler['key_id'] = 0
        self.__crawler['p_id'] = 0
        self.__crawler['server'] = None
        self.__crawler['state'] = 'created'
        self.__crawler['platform'] = None
        self.__crawler['mode'] = None

    @property
    def crawler(self):
        return self._Crawler__crawler

    @crawler.setter
    def crawler(self, crawler):
        if self.crawler.keys() == crawler.keys():
            self._Crawler__crawler = crawler
        else:
            print('required Crawler class type at crawler')
            raise TypeError

    @crawler.setter
    def crawler(self, crawler):
        print()

    @property
    def id(self):
        return self.crawler['_id']

    @id.setter
    def id(self, id):
        if type(id) != int:
            print('required int type at id')
            raise TypeError
        self.crawler['_id'] = id

    @property
    def key_id(self):
        return self.crawler['key_id']

    @key_id.setter
    def key_id(self, key_id):
        if type(key_id) != int:
            print('required int type at key_id')
            raise TypeError
        self.crawler['key_id'] = key_id

    @property
    def p_id(self):
        return self.crawler['p_id']

    @p_id.setter
    def p_id(self, p_id):
        if type(p_id) != int:
            print('required int type at p_id')
            raise TypeError
        self.crawler['p_id'] = p_id

    @property
    def server(self):
        return self.crawler['server']

    @server.setter
    def server(self, server):
        if type(server) != str:
            print('required str type at server')
            raise TypeError
        self.crawler['server'] = server

    @property
    def state(self):
        return self.crawler['state']

    @state.setter
    def state(self, state):
        if type(state) != str:
            print('required str type at state')
            raise TypeError
        self.crawler['state'] = state

    @property
    def platform(self):
        return self.crawler['platform']

    @platform.setter
    def platform(self, platform):
        if type(platform) != str:
            print('required str type at platform')
            raise TypeError
        self.crawler['platform'] = platform

    @property
    def mode(self):
        return self.mode

    @mode.setter
    def mode(self, mode):
        if type(mode) != str:
            print('required str type at mode')
            raise TypeError
        self.crawler['mode'] = mode


class CrawlerMongo(Crawler):
    def __init__(self):
        super(__class__, self).__init__()
        self.mongo = CrawlerMongo.connect()

    @staticmethod
    def connect():
        try:
            mongo = MongoClient('localhost', 27017)
            return mongo
        except Exception as e:
            print_exception_info()

    def close(self):
        try:
            self.mongo.close()
        except Exception as e:
            print_exception_info()

    def get_crawler_dict(self, crw_id):
        try:
            cralwer_dict = self.mongo.crawler.crawler.find_one({'_id': crw_id})
            return cralwer_dict
        except Exception as e:
            print_exception_info()

    def insert_crawler_dict(self):
        try:
            self.mongo.crawler.crawler.insert_one(self.crawler)
        except Exception as e:
            print_exception_info()