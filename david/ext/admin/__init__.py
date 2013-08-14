# coding: utf-8
from flask.ext.admin import Admin
from flask import Blueprint, abort

from .model import Roled, ModelAdmin, AdminIndex

admin = Admin(index_view=AdminIndex(name='首页'))
