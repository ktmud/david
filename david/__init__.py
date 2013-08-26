# coding: utf-8
VERSION = (0, 0, 1)

__version__ = ".".join(map(str, VERSION))
__status__ = "Development"
__description__ = "Flask CMS with MYSQL"
__author__ = "Jesse Yang"
__credits__ = ['quokka']
__email__ = "kissmud@gmail.com"
__license__ = "MIT License"
__copyright__ = "Copyright 2013, Jesse Yang"

import sys
reload(sys)
sys.setdefaultencoding('utf-8') # use utf-8 str by default

from flask import Flask

from .ext import init_app
import config

app = Flask(__name__,
        # remap to distributed static files
        static_url_path='/static',
        static_folder='static/dist'
      )
app.config.from_object(config)

init_app(app)
