# -*- coding: utf-8 -*-
import re
from werkzeug.routing import BaseConverter


class NoDotConverter(BaseConverter):
    def __init__(self, url_map):
        super(NoDotConverter, self).__init__(url_map)
        self.regex = re.compile(r'[^\.]+')
