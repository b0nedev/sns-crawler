"""
- debug.py
"""
import sys


def print_exception_info():
    e_type, e_obj, tb = sys.exc_info()
    print(e_obj)
    print('{}: {} line at {}'.format(e_type.__name__, tb.tb_lineno, tb.tb_frame.f_code.co_filename.split('/')[-1]))

