# -*- coding: utf-8 -*-
from flask import Blueprint, request
from david.lib.template import st
from .model import Artist

bp = Blueprint('artist', __name__)

@bp.route('/artist/<uid>')
def artist_intro(uid):
    artist = Artist.get(uid)
