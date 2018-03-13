"""
- dateparse.py
 - date, datetime parsing and converting
"""
from datetime import datetime, date, time
from datetime import timedelta, timezone
import pytz


def min_of_datetime(date_time):
    day = date_time.date()
    datetime_str = datetime.combine(day, time.min).strftime('%Y-%m-%d %H:%M:%S')
    return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')


def max_of_datetime(date_time):
    day = date_time.date()
    datetime_str = datetime.combine(day, time.max).strftime('%Y-%m-%d %H:%M:%S')
    return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')


def datetime_to_date(date_time):
    return date_time.date()


def date_to_datetime(date_, format='%Y-%m-%d %H:%M:%S'):
    datetime_str = datetime.combine(date_, time.min).strftime(format)
    return datetime.strptime(datetime_str, format)


def get_youtube_datetime(date_):
    published_after = datetime.combine(date_, time.min).strftime('%Y-%m-%dT%H:%M:%SZ')
    published_before = datetime.combine(date_,time.max).strftime('%Y-%m-%dT%H:%M:%SZ')
    return published_after, published_before


def date_timedelta(date_, days=0, hours=0, minutes=0, seconds=0):
    date_time = date_to_datetime(date_) + timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    return date_time.date()