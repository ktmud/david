# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify
from david.lib.template import st
from david.ext.attachment import 

from .model import QiniuAttachment

bp = Blueprint('qiniu', __name__)

@bp.route('/api/qiniu/upload', methods=['GET', 'POST'])
def qiniu_upload():
    if request.method = 'POST' and request.files:
        ret = []
        for k, fp in request.files:
            item = QiniuAttachment.add(filename)
            ret.append(item.info())
        return jsonify(ret)


@bp.route('/api/qiniu/callback', methods=['GET', 'POST'])
def qiniu_callback():
    pass
