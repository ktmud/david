# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8') # use utf-8 by default

from flask import Flask

from .ext import init_app
from . import config

app = Flask(__name__,
        # remap to distributed static files
        static_url_path='/static',
        static_folder='static/dist'
      )
app.config.from_object(config)

init_app(app)
