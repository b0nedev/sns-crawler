"""
- parser.py
 - Parser Class
  -
"""
import re
from datetime import datetime
from model.scrapdata import ScrapData, Reply
from lib.debug import print_exception_info
p = re.compile(r"(\d+[-]\d+[-]\d+)T(\d+[:]\d+[:]\d+)[.]\d+Z")


class Parser(object):
    def __init__(self):
        self.scrap = ScrapData()

    def body_parser(self, body):
        raise NotImplementedError

    def reply_parser(self, reply):
        raise NotImplementedError


class YoutubeParser(Parser):
    def __init__(self):
        super(__class__, self).__init__()

    @staticmethod
    def list_parser(list_data):
        try:
            items = list_data.get('items')
            if items:
                for item in items:
                    yield item.get('id').get('videoId')
        except Exception as e:
            print_exception_info()

    @staticmethod
    def get_ptoken(list_data):
        try:
            page_token = list_data.get('nextPageToken')
            if page_token:
                return page_token
            else:
                return ''
        except Exception as e:
            print_exception_info()

    @staticmethod
    def body_parser(body_data):
        scrap = ScrapData()
        video_url = 'https://www.youtube.com/watch?v='
        try:
            items = body_data.get('items')
            if items:
                snippet = items[0]['snippet']
                scrap.title = snippet['title']
                scrap.userid = snippet['channelId']
                scrap.username = snippet['channelTitle']
                scrap.text = snippet['description']
                scrap.url = video_url + items[0]['id']
                statistics = body_data['items'][0]['statistics']
                scrap.view = int(statistics['viewCount'])
                scrap.like = int(statistics['likeCount']) if statistics.get('likeCount') else 0
                scrap.profile = snippet['thumbnails']['default']['url']
                m_date = p.search(snippet['publishedAt'])
                date_str = m_date.group(1) + ' ' + m_date.group(2)
                scrap.publishedat = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
            return scrap
        except Exception as e:
            print_exception_info()

    @staticmethod
    def reply_parser(reply_data):
        idx = 0
        try:
            items = reply_data.get('items')
            if items:
                for item in items:
                    reply = Reply()
                    idx += 1
                    comment_snippet = item['snippet']['topLevelComment']['snippet']
                    reply.id = idx
                    reply.username = comment_snippet['authorDisplayName']
                    reply.text = comment_snippet['textDisplay']
                    if item.get('replies'):
                        reply.rreply = [x for x in YoutubeParser.rereply_parser(item['replies'])]
                    yield reply.reply
        except Exception as e:
            print_exception_info()

    @staticmethod
    def rereply_parser(rereply_data):
        idx = 0
        comments = rereply_data.get('comments')
        if comments:
            for comment in comments:
                rereply = Reply()
                idx += 1
                snippet = comment.get('snippet')
                rereply.id = idx
                rereply.username = snippet.get('authorDisplayName')
                rereply.text = snippet.get('textDisplay')
                yield rereply.reply


class InstaParser(Parser):
    def __init__(self):
        super(__class__, self).__init__()

    def body_parser(self, body):
        pass

    def reply_parser(self, reply):
        pass
