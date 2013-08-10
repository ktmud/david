# coding: utf-8
from flask import Flask

from .ext import setup_logging, init_app, load_modules, register_views

import config

app = Flask(__name__)
app.config.from_object(config)

setup_logging(app)
init_app(app)
