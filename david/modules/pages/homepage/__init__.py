# -*- coding: utf-8 -*-
from david.ext.babel import lazy_gettext as _
from david.ext.admin import DBKeyAdminView
from david.lib.template import st

from .model import DB_HOMEPAGE_ARTICLES
from .model import get_homepage_articles

from ..view import bp


@bp.route('/')
def home():
    articles, captions = get_homepage_articles()
    articles = [x.extended_self() for x in articles]
    carousel_items = [dict(img=x.picture_url('large'), link=x.url(),
                                caption=captions[i])
                      for i,x in enumerate(articles) if x]
    return st('modules/pages/home.html', **locals())



homepage_admin = DBKeyAdminView(name=_('Home Page'), endpoint='homepage')
homepage_admin.db_keys = (DB_HOMEPAGE_ARTICLES, )
homepage_admin.key_labels = {
    DB_HOMEPAGE_ARTICLES: _('Home page articles')
}
homepage_admin.help_text = {
    DB_HOMEPAGE_ARTICLES: _('article ids or article url, one item per line')
}
