# -*- coding: utf-8 -*-
import qiniu

from david.ext.filestore import FileStore 
from david.config import QINIU_AK, QINIU_SK, QINIU_BUCKET, QINIU_ROOT
from david.config import SITE_ROOT

from david.core.attachment import Attachment



qiniu.conf.ACCESS_KEY = QINIU_AK
qiniu.conf.SECRET_KEY = QINIU_SK


class QiniuPutPolicy(qiniu.rs.PutPolicy)
    callbackUrl = SITE_ROOT + '/api/qiniu/callback'
    callbackBody = 'owner_type=$(x:owner_type)&owner_id=$(x:owner_id)&key=$(etag)&size=$(fsize)&uid=$(endUser)'



class QiniuClient(qiniu.rs.Client):
    pass


class QiniuStore(FileStore):

    def __init__(self, bucket):
        self._bucket = bucket
        self._policy = QiniuPutPolicy(bucket)
        self._client = QiniuClient()

    def save(self, storage, name=None):
        key = self.get_file_key(storage, name)
        uptoken = self._policy.token()
        qiniu.io.put(uptoken, key, storage.stream)

    def exists(self, key):
        ret, err = self._client.stat(self._bucket, key)

    def url(self, key):
        return QINIU_ROOT + key

    def path(self, key):
        return key


class QiniuAttachment(Attachment):
    manager = QiniuStore(QINIU_BUCKET)
