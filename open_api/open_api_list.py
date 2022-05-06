"""
Description of this file
author:
copyright:
date created: 2021-05-01
python version: 3.8

模块作用：封装开放接口
"""

import requests
from config import basic_info
from open_api.sign import Signature_method
import copy


class All_open_api:
    '''这个类封装了开放平台大部分的接口'''

    def __init__(self):
        self.host = basic_info.host
        self.headers = basic_info.headers
        self.params = basic_info.params
        self.secretKey = basic_info.secretKey

    # 获取联系方式：
    def contact(self, name):
        params = copy.deepcopy(self.params)
        url = "%s/api/open-api/enterprise/contact" % self.host
        params['name'] = name
        params['signature'] = Signature_method(params).signature_method1(self.secretKey)

        resp = requests.get(url, params=params)
        return resp.status_code, resp.json()

    # 获取拓客40个通用数据维度
    def all_dimension(self, enterprise_id):
        params = copy.deepcopy(self.params)
        url = "%s/api/open-api/enterprise/all-dimension" % self.host
        params['enterprise_id'] = enterprise_id
        params['signature'] = Signature_method(params).signature_method1(self.secretKey)

        resp = requests.get(url, params=params)
        return resp.status_code, resp.json()

    # 智能外呼通话明细数据接口
    def call_detail(self, task_id, begin, end):
        params = copy.deepcopy(self.params)
        url = "%s/api/open-api/smart-call/task/call-detail" % self.host
        params['task_id'] = task_id
        params['begin'] = begin
        params['end'] = end
        params['signature'] = Signature_method(params).signature_method1(self.secretKey)

        resp = requests.get(url, params=params)
        return resp.status_code, resp.json()


if __name__ == "__main__":
    data = "null"
    r = All_open_api().contact(data)
    print(r)





