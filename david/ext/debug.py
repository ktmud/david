# coding: utf-8
from flask.ext.debugtoolbar import DebugToolbarExtension
from flask.ext.sqlalchemy import get_debug_queries

def setup_debug(app):
    DebugToolbarExtension(app)
