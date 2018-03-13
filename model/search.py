"""
search.py
- search model
- id: keyword_id(to keyword number)
- keyword: search word
- start_date: start date of search
- end_date: end date of search
"""
from datetime import datetime
from pymongo import MongoClient
from lib.debug import print_exception_info

class Search(object):
    def __init__(self):
        self.__search = dict()
        self.__search['_id'] = 0
        self.__search['keyword'] = None
        self.__search['start_date'] = None
        self.__search['end_date'] = None

    @property
    def search(self):
        return self._Search__search

    @search.setter
    def search(self, search):
        if self.search.keys() == search.keys():
            self._Search__search = search
        else:
            print('Type err(required Search class type) at search')
            raise TypeError

    @property
    def id(self):
        return self.search['_id']

    @id.setter
    def id(self, id):
        if type(id) != int:
            print('Type err(required int type) at id')
            raise TypeError
        self.search['_id'] = id

    @property
    def keyword(self):
        return self.search['keyword']

    @keyword.setter
    def keyword(self, keyword):
        if type(keyword) != str:
            print('Type err(required str type) at keyword')
            raise TypeError
        self.search['keyword'] = keyword

    @property
    def start_date(self):
        return self.search['start_date']

    @start_date.setter
    def start_date(self, start_date):
        if type(start_date) != datetime:
            print('Type err(required datetime type) at start_date')
            raise TypeError
        self.search['start_date'] = start_date

    @property
    def end_date(self):
        return self.search['end_date']

    @end_date.setter
    def end_date(self, end_date):
        if type(end_date) != datetime:
            print('Type err(required datetime type) at end_date')
            raise TypeError
        self.search['end_date'] = end_date


class SearchMongo(Search):
    def __init__(self):
        super(__class__, self).__init__()
        self.mongo = SearchMongo.connect()

    @staticmethod
    def connect():
        try:
            mongo = MongoClient('localhost', 27017)
            return mongo
        except Exception as e:
            print_exception_info(e)

    def close(self):
        self.mongo.close()

    def get_search_dict(self, key_id):
        try:
            search_dict = self.mongo.crawler.search.find_one({'_id': key_id})
            return search_dict
        except Exception as e:
            print_exception_info(e)

    def insert_search_dict(self):
        try:
            self.mongo.crawler.search.insert_one(self.search)
        except Exception as e:
            print_exception_info(e)