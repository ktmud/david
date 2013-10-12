# -*- coding: utf-8 -*-
from flask import url_for, current_app
from david.lib.mixins.props import PropsMixin, PropsItem
from david.core.article import Article, add_cat
from david.ext.views.static import lazy_static_url

C_PHOTOS = 201
C_MAGAZINE = 202

class Photos(Article):
    cat_id = C_PHOTOS
    cat_name = 'photos'

    def serialize(self, fields=[]):
        pics = self.pics_info()
        ret = dict(id=self.id, title=self.title,
                url=self.url(),
                abstract=self.abstract(),
                thumb_url = self.thumb_url,
                median_url = self.picture_url('median'),
                pics=pics)
        return ret

    @property
    def thumb_url(self):
        return self.picture_url('sqr120')

    def url(self):
        return url_for('gallery.show', mod=self.cat_name, ident=self.slug);

    def pics_info(self):
        pics = [dict(title=x.title, desc=x.desc, large_url=x.url('large'),
                     thumb_url=x.thumb_url)
                for x in self.attachment_pics()]
        return pics


class Magazine(Photos):
    cat_id = C_MAGAZINE
    cat_name = 'magazine'

    _DEFAULT_PIC = lazy_static_url('img/blank.gif')

    @property
    def thumb_url(self):
        return self.picture_url('cover')

    def url(self):
        return '%smagazine/#%s' % (current_app.config['SITE_ROOT'], self.id)

add_cat(C_PHOTOS, Photos)
add_cat(C_MAGAZINE, Magazine)
