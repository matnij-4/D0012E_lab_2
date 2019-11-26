# -*- coding: utf-8 -*-
""" De element vi sätter in i hashtabelet. Key och data genereras som random värden av oss, hashed_key och function_key
    sätts till h(key).
"""
class key:
    def __init__(self, key, data):
        self.hashed_key = 0
        self.function_key = 0
        self.key = key
        self.data = data