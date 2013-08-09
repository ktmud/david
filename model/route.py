# coding: utf-8
from flask import request

class Route:

    def __init__(path, module):
        self.path = path
        self.module = module

    @classmethod
    def get(path):
        return ''

    def dispatch():
        return __import__(module, 'view')(request)
