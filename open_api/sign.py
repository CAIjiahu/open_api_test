"""
Description of this file
author:
copyright:
date created: 2021-05-01
python version: 3.8

模块作用：封装各种授权方式
token+secret_key
"""
from config import basic_info
from hashlib import md5



class Signature_method:
    "该类是封装了项目所有的授权方式"
    def __init__(self, params):
        self.params = params


    def signature_method1(self, secret_key):
        keys = sorted(list(self.params.keys()))
        # print(keys)
        params_str = ''
        for key in keys:
            # print(str(params[key]))
            params_str += str(self.params[key])
        params_str += secret_key
        return md5(params_str.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    params = basic_info.params
    secret_key = basic_info.secretKey
    s = Signature_method(params).signature_method1(secret_key)

    print(s)

