"""
scrapdata.py
 - scrapdata model
 - id: scrap data id
 - title: youtube(title), insta/twitter(username)
 - username: user nickname
 - userid: user account id
 - text: main text
 - view: view count
 - like: like count
 - subscription: subscription count
 - profile: profile image url
 - published_at: published date
 - reply: reply list
"""
from datetime import datetime
from pymongo import MongoClient
from lib.debug import print_exception_info


class ScrapData(object):
    def __init__(self):
        self.__scrap = dict()
        self.__scrap['_id'] = 0
        self.__scrap['title'] = None
        self.__scrap['username'] = None
        self.__scrap['userid'] = None
        self.__scrap['text'] = None
        self.__scrap['url'] = None
        self.__scrap['view'] = 0
        self.__scrap['like'] = 0
        self.__scrap['profile'] = None
        self.__scrap['publishedat'] = None
        self.__scrap['reply'] = []

    @property
    def scrap(self):
        return self._ScrapData__scrap

    @scrap.setter
    def scrap(self, scrap):
        if self.scrap.keys() == scrap.keys():
            self._ScrapData__scrap = scrap
        else:
            print('required ScrapData class type at scrap')
            raise TypeError

    @property
    def id(self):
        return self.scrap['_id']

    @id.setter
    def id(self, id):
        if type(id) != int:
            print('required int type at id')
            raise TypeError
        self.scrap['_id'] = id

    @property
    def title(self):
        return self.scrap['title']

    @title.setter
    def title(self, title):
        if type(title) != str:
            print('required str type at title')
            raise TypeError
        self.scrap['title'] = title

    @property
    def username(self):
        return self.scrap['username']

    @username.setter
    def username(self, username):
        if type(username) != str:
            print('required str type at username')
            raise TypeError
        self.scrap['username'] = username

    @property
    def userid(self):
        return self.scrap['userid']

    @userid.setter
    def userid(self, userid):
        if type(userid) != str:
            print('required str type at userid')
            raise TypeError
        self.scrap['userid'] = userid

    @property
    def text(self):
        return self.scrap['text']

    @text.setter
    def text(self, text):
        if type(text) != str:
            print('required str type at text')
            raise TypeError
        self.scrap['text'] = text

    @property
    def url(self):
        return self.scrap['url']

    @url.setter
    def url(self, url):
        if type(url) != str:
            print('required str type at text')
            raise TypeError
        self.scrap['url'] = url

    @property
    def view(self):
        return self.scrap['view']

    @view.setter
    def view(self, view):
        if type(view) != int:
            print('required int type at view')
            raise TypeError
        self.scrap['view'] = view

    @property
    def like(self):
        return self.scrap['view']

    @like.setter
    def like(self, like):
        if type(like) != int:
            print('required int type at like')
            raise TypeError
        self.scrap['like'] = like

    @property
    def profile(self):
        return self.scrap['profile']

    @profile.setter
    def profile(self, profile):
        if type(profile) != str:
            print('required str type at profile')
            raise TypeError
        self.scrap['profile'] = profile

    @property
    def publishedat(self):
        return self.scrap['publishedat']

    @publishedat.setter
    def publishedat(self, publishedat):
        if type(publishedat) != datetime:
            print('required datetime type at publishedat')
            raise TypeError
        self.scrap['publishedat'] = publishedat

    @property
    def reply(self):
        return self.scrap['reply']

    @reply.setter
    def reply(self, reply):
        if type(reply) != list:
            print('required list type at reply')
            raise TypeError
        self.scrap['reply'] = reply
"""
-reply.py
 - id: reply id
 - username: reply writer nickname
 - text: reply text
 - publishedat: written date
 - rreply: re-reply list
"""


class Reply(object):
    def __init__(self):
        self.__reply = dict()
        self.__reply['_id'] = 0
        self.__reply['username'] = None
        self.__reply['text'] = None
        self.__reply['publishedat'] = None
        self.__reply['rreply'] = []

    @property
    def reply(self):
        return self._Reply__reply

    @reply.setter
    def reply(self, reply):
        if self.reply.keys() == reply.keys():
            self._Reply__reply = reply
        else:
            print('required reply class type at reply')
            raise TypeError

    @property
    def id(self):
        return self.reply['_id']

    @id.setter
    def id(self, id):
        if type(id) != int:
            print('required int type at id')
            raise TypeError
        self.reply['_id'] = id

    @property
    def username(self):
        return self.username

    @username.setter
    def username(self, username):
        if type(username) != str:
            print('required str type at username')
            raise TypeError
        self.reply['username'] = username

    @property
    def text(self):
        return self.reply['text']

    @text.setter
    def text(self, text):
        if type(text) != str:
            print('required str type at text')
            raise TypeError
        self.reply['text'] = text

    @property
    def publishedat(self):
        return self.reply['publishedat']

    @publishedat.setter
    def publisehd(self, publishedat):
        if type(publishedat) != datetime:
            print('required datetime type at publishedat')
            raise TypeError
        self.reply['publishedat'] = publishedat

    @property
    def rreply(self):
        return self.reply['rreply']

    @rreply.setter
    def rreply(self, rreply):
        if type(rreply) != list:
            print('required list type at rreply')
            raise TypeError
        self.reply['rreply'] = rreply


class ScrapMongo(ScrapData):
    def __init__(self):
        super(__class__, self).__init__()
        self.mongo = self.connect()

    def connect(self):
        try:
            mongo = MongoClient('localhost', 27017)
            return mongo
        except Exception as e:
            print_exception_info()

    def close(self):
        self.mongo.close()

    def get_last_id(self):
        try:
            documents = [x for x in self.mongo.crawler.scrap_data.find()]
            if documents:
                return int(documents[-1]['_id'])
            else:
                return 0
        except Exception as e:
            print_exception_info()

    def get_scrap_dict(self, scrap_id):
        try:
            scrap_dict = self.mongo.crawler.scrap_data.find_one({'_id': scrap_id})
            return scrap_dict
        except Exception as e:
            print_exception_info()

    def delete_scrap_dict(self):
        try:
            self.mongo.crawler.scrap_data.delete_one({'url': self.url})
        except Exception as e:
            print_exception_info()

    def insert_scrap_dict(self):
        try:
            scrap_dict = self.get_scrap_dict({'url': self.url})
            if scrap_dict:
                self.delete_scrap_dict()
            self.mongo.crawler.scrap_data.insert_one(self.scrap)
        except Exception as e:
            print_exception_info()
        else:
            print('[ok]')