# -*- coding: utf-8 -*-
from .ext import init_app

from flask import Flask
import config

app = Flask(__name__,
        # remap to distributed static files
        static_url_path='/static',
        static_folder='static/dist'
      )
app.config.from_object(config)

init_app(app)
