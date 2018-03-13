"""
- youtube.py
 - youtube cralwer
"""
from helper.crawl import Crawl, get_data
from helper.url import YoutubeUrl
from model.search import SearchMongo
from model.crawler import CrawlerMongo
from model.scrapdata import ScrapData
from lib.debug import print_exception_info
from lib.dateparse import get_youtube_datetime
from helper.parser import YoutubeParser


class Youtube(object):

    def __init__(self, crw_id, mode):
        self.crw_id = crw_id
        self.mode = mode
        self.search = self.get_search()
        self.youtube = YoutubeUrl()
        self.youtube_key = 'AIzaSyBTFax4x5CfPd04huEoSOrM2OTIldyHyyk'

    def get_keyword_id(self):
        try:
            cmongo = CrawlerMongo()
            crawl = cmongo.get_crawler_dict(self.crw_id)
            cmongo.close()
            if crawl:
                return crawl['key_id']
            else:
                return 0
        except Exception as e:
            print_exception_info()

    def get_search(self):
        try:
            key_id = self.get_keyword_id()
            smongo = SearchMongo()
            search = smongo.get_search_dict(key_id)
            smongo.close()
            return search if search else None
        except Exception as e:
            print_exception_info()

    def get_list(self, std_date):
        page_token = ''
        published_after, published_before = get_youtube_datetime(std_date)
        while True:
            list_url = self.youtube.get_list_url(self.search['keyword'], published_after, published_before, self.youtube_key, page_token)
            list_data = get_data(list_url)
            if list_data:
                video_ids = YoutubeParser.list_parser(list_data)
                for video_id in video_ids:
                    yield video_id
                page_token = YoutubeParser.get_ptoken(list_data)
                if page_token is None or not list_data.get('items'):
                    print('url list end')
                    break
            else:
                print('list data is None')

    def get_body(self, video_id):
        body_url = self.youtube.get_body_url(video_id, self.youtube_key)
        body_data = get_data(body_url)
        if body_data:
            scrap = YoutubeParser.body_parser(body_data)
            return scrap
        else:
            return None

    def get_reply(self, video_id):
        page_token = ''
        while True:
            reply_url = self.youtube.get_reply_url(video_id, self.youtube_key, page_token)
            reply_data = get_data(reply_url)
            if reply_data:
                reply = [x for x in YoutubeParser.reply_parser(reply_data)]
                return reply
            else:
                return []
            page_token = YoutubeParser.get_ptoken(reply_data)
            if page_token is None or not list_data.get('items'):
                print('reply end')
                break

    def run(self):
        crawl = Crawl('youtube', self.search)
        func_list = {'list': youtube.get_list, 'body': youtube.get_body, 'reply': youtube.get_reply}
        if self.mode == 'tag':
            crawl.tag_crawl(func_list)
        elif self.mode == 'user':
            crawl.user_crawl(func_list)
        else:
            print('invalid mode!')


if __name__ == "__main__":
    youtube = Youtube(1, 'tag')
    youtube.run()