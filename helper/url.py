"""
- url.py

"""
import json
import urllib


def get_url_json():
    content = list()
    try:
        with open("url_info.json") as file:
            for line in file:
                content.append(line)
        return json.loads(''.join(content))
    except Exception as e:
        print(e)


class YoutubeUrl(object):
    def __init__(self):
        self.config = get_url_json()

    def get_list_url(self, query, start_str, end_str, key, page_token='', max_results=50):
        params = {
            'part': 'snippet',
            'q': query,
            'order': 'date',
            'type': 'video',
            'publishedAfter': start_str,
            'publishedBefore': end_str,
            'maxResults': max_results,
            'key': key,
            'pageToken': page_token
        }
        url_tuple = (self.config['protocol'], self.config['youtube']['top_url'],
                     self.config['youtube']['search_url'], '', urllib.parse.urlencode(params), '')
        return urllib.parse.urlunparse(url_tuple)

    def get_body_url(self, video_id, key):
        params = {
            'part': 'snippet,statistics',
            'id': video_id,
            'key': key
        }
        url_tuple = (self.config['protocol'], self.config['youtube']['top_url'],
                     self.config['youtube']['body_url'], '', urllib.parse.urlencode(params), '')
        return urllib.parse.urlunparse(url_tuple)

    def get_reply_url(self, video_id, key, page_token='', order='relevance', max_results=100):
        params = {
            'part': 'snippet,replies',
            'videoId': video_id,
            'order': order,
            'maxResults': max_results,
            'key': key,
            'pageToken': page_token
        }
        url_tuple = (self.config['protocol'], self.config['youtube']['top_url'],
                     self.config['youtube']['reply_url'], '', urllib.parse.urlencode(params), '')
        return urllib.parse.urlunparse(url_tuple)

    def get_plist_url(self, ch_id, key):
        params = {
            'part': 'snippet',
            'channelId': ch_id,
            'key': key
        }
        url_tuple = (self.config['protocol'], self.config['youtube']['top_url'],
                     self.config['youtube']['plist_url'], '', urllib.parse.urlencode(params), '')
        return urllib.parse.urlunparse(url_tuple)

    def get_pitem_url(self, plist_id, key, max_results=50):
        params = {
            'part': 'snippet',
            'playlistId': plist_id,
            'maxResults': max_results,
            'key': key
        }
        url_tuple = (self.config['protocol'], self.config['youtube']['top_url'],
                     self.config['youtube']['pitem_url'], '', urllib.parse.urlencode(params), '')
        return urllib.parse.urlunparse(url_tuple)

    def get_channel_url(self, u_name, key):
        params = {
            'part': 'snippet',
            'forUsername': u_name,
            'key': key
        }
        url_tuple = (self.config['protocol'], self.config['youtube']['top_url'],
                     self.config['youtube']['channel_url'], '', urllib.parse.urlencode(params), '')
        return urllib.parse.urlunparse(url_tuple)

class InstaUrl(object):
    def __init__(self):
        self.config = get_url_json()

    def get_list_url(self):
        pass

    def get_body_url(self):
        pass

    def get_reply_url(self):
        pass

class TwitterUrl(object):
    def __init__(self):
        self.config = get_url_json()

    def get_list_url(self):
        pass

    def get_body_url(self):
        pass

    def get_reply_url(self):
        pass
