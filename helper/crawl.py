"""
- crawl.py
 - Crawl Class
  -
"""
import requests
from model.scrapdata import ScrapMongo
from lib.dateparse import datetime_to_date, date_timedelta
from lib.debug import print_exception_info


def get_res(url, headers=None, proxy=None):
    try:
        res = requests.get(url, headers=headers, proxies=proxy)
        if res.status_code == 200:
            return res
    except Exception as e:
        print_exception_info()


def get_json(res):
    try:
        json_data = res.json()
        return json_data
    except Exception as e:
        print_exception_info()


def get_data(url, headers=None, proxy=None):
    try:
        res = get_res(url, headers, proxy)
        if res:
            raw_data = get_json(res)
            return raw_data
    except Exception as e:
        print_exception_info()

base_urls = {
    'youtube': 'https://www.youtube.com/watch?v=',
    'instagram': ''
}

class Crawl(object):
    def __init__(self, platform, search):
        self.platform = platform
        self.search = search
        self.start_date = datetime_to_date(self.search['start_date'])
        self.end_date = datetime_to_date(self.search['end_date'])

    def tag_crawl(self, scrap_data):
        print('tag crawl')
        try:
            smongo = ScrapMongo()
            scrap_id = smongo.get_last_id()
            std_date = self.end_date
            while std_date >= self.start_date:
                vid_list = scrap_data['list'](std_date)
                for vid in vid_list:
                    print(base_urls[self.platform] + vid)
                    scrap_id += 1
                    body = scrap_data['body'](vid)
                    if body:
                        scrap = body
                        scrap.id = scrap_id
                        scrap.reply = scrap_data['reply'](vid)
                    smongo.scrap = scrap.scrap
                    smongo.insert_scrap_dict()
                std_date = date_timedelta(std_date, days=-1)
            smongo.close()
        except Exception as e:
            print_exception_info()

    def user_crawl(self):
        pass