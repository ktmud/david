# -*- coding: utf-8 -*-
import logging
import qiniu.conf
import qiniu.rs
import qiniu.io
import qiniu.resumable_io as rio
import sys

from david.ext.filestore import FileStore 
from config import QINIU_AK, QINIU_SK, QINIU_BUCKET, QINIU_ROOT
from config import SITE_ROOT

from david.core.attachment import Attachment, add_subclass

logger = logging.getLogger(__name__)


class QiniuUploadFail(Exception):
    pass

class QiniuStatFail(Exception):
    pass


qiniu.conf.ACCESS_KEY = QINIU_AK
qiniu.conf.SECRET_KEY = QINIU_SK


class QiniuPutPolicy(qiniu.rs.PutPolicy):
    #callbackUrl = SITE_ROOT + '/api/qiniu/callback'
    callbackBody = 'owner_type=$(x:owner_type)&owner_id=$(x:owner_id)&key=$(etag)&size=$(fsize)&uid=$(endUser)'



class QiniuClient(qiniu.rs.Client):
    pass


class QiniuStore(FileStore):

    def __init__(self, bucket, delimiter='-'):
        self._bucket = bucket
        self._delimiter = delimiter
        self._policy = QiniuPutPolicy(bucket)
        self._client = QiniuClient()
        self.target = None

    def save(self, storage, name=None):
        key = self.get_file_key(storage, name)
        uptoken = self._policy.token()
        logger.debug('uploading: %s', key)
        ret, err = qiniu.io.put(uptoken, key, storage.stream)
        if err:
            logger.error('%s - "%s", %s', self._bucket, key, err)
            raise QiniuUploadFail('%s: %s' % (key, err))
        else:
            logger.debug('uploaded: %s', ret)
        return ret['key']

    def remove(self, key):
        ret, err = self._client.delete(self._bucket, key)
        logger.debug('remove %s: %s, %s', key, ret, err)
        return ret

    def exists(self, key):
        return False

    def url(self, key, category='default', user=None):
        return QINIU_ROOT + key + (self._delimiter + category if category else '')

    def path(self, key):
        return key

    def stat(self, key):
        ret, err = self._client.stat(bucket_name, key)
        if err:
            logger.error('%s - "%s", %s', self._bucket, key, err)
            raise QiniuStoreA('%s: %s' % (key, err))
        return ret


class QiniuAttachment(Attachment):
    manager = QiniuStore(QINIU_BUCKET)


add_subclass(QiniuAttachment)
