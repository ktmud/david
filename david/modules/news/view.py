# coding: utf-8
from flask import Blueprint
from david.lib.template import st

bp = Blueprint('news', __name__)

@bp.route('/news/')
def home():
    return st('/modules/news/index.html')

__all__ = [bp]



