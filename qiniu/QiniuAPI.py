#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests

from qiniu import Auth
from qiniu import BucketManager
from qiniu import CdnManager


class QiniuApi:
	"""
	pip install qiniu
	"""	
    def __init__(self):
        self.access_key = ''
        self.secret_key = ''
        self._auth = self.__auth()
        self._bucket = BucketManager(self._auth)
        self._cdn = CdnManager(self._auth)

    def __auth(self):
        q = Auth(access_key=self.access_key, secret_key=self.secret_key)
        return q

    def file_stat(self, bucket_name, img_name):
        ret, info = self._bucket.stat(bucket_name, img_name)
        return ret, info

    def download_file(self, base_url):
        private_url = self._auth.private_download_url(base_url, expires=600)
        r = requests.get(private_url)
        if r.status_code == 200:
            return r.content
        return

    def delete_file(self, bucket_name, img_name):
        ret, info = self._bucket.delete(bucket_name, img_name)
        return ret, info

    def refresh_urls(self, url_list):
        refresh_url_result = self._cdn.refresh_urls(url_list)
        return refresh_url_result


if __name__ == '__main__':
    qiniu_obj = QiniuAPI()
    print(qiniu_obj.file_stat(bucket_name='test', img_name='test.jpg'))
