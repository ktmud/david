# -*- coding: utf-8 -*-
from flask import Blueprint, request, abort, redirect
from david.lib.template import st
from .model import Event

bp = Blueprint('event', __name__)


def list_data(pagi):
    return dict(r=0,
            total=pagi.total,
            has_next=pagi.has_next,
            items=[x.serialize() for x in pagi.items])

@bp.route('/event/')
@bp.route('/event/p<int:page>')
def list(page=1):
    perpage = 40
    pagi = Event.query.order_by(Event.create_at.desc()).paginate(page, perpage)
    data = list_data(pagi)
    return st('/modules/event/index.html', **locals())

