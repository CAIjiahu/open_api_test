#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    open_api.py
    ~~~~~~~~~~~~~~~~~~~~~~~

    Description of this file

    :author: will
    :copyright: (c) 2020, Tungee
    :date created: 2020-09-21
    :python version: 3.6

"""
import time
from datetime import datetime
from hashlib import md5

import requests

accessToken = "YUXJRB5SKGAD9LVP78WHE0FICM32Q146"    # dev测试token 【测试】开放平台测试
secretKey = "1KIN5C7QZJA8HSEORBLPV2T6Y3XW4MFD"  # dev测试secret 【测试】开放平台测试
# # #
# accessToken = "9TGXF7NWK51EYDL03VQA846J2MUHPCRS"    # uat测试token
# secretKey = "W7KG2NQFLJ14TEISR9HADVC63ZPXBY85"  # uat测试secret
# accessToken = "YUXJRB5SKGAD9LVP78WHE0FICM32Q146"  # dev测试token
# secretKey = "1KIN5C7QZJA8HSEORBLPV2T6Y3XW4MFD"  # dev测试secret
# accessToken = "IPJVH9KLZ2UOSD8ENYQ1A3XCTWMF7460"    # 生产token
# secretKey = "USBJ52N46RCYLKW8EH0IMFOD9QAP3X1G"  # 生产secret
host = "http://paas-dev.tangees.com"
# host = "http://paas-uat.tangees.com"   # UAT测试主机
# host = "https://paas.tungee.com"   # 生产主机
params = {
    'nterprise_id':"NNoipejfdiweniu3",
    "accessToken": accessToken,
    "timestamp": datetime.strftime(datetime.utcnow(), '%Y-%m-%dT%H:%M:%S'),
    "user":'888f3jopjfop3w88888'
}


def signature(secret_key):
    keys = sorted(list(params.keys()))
    print(keys)
    params_str = ''
    for key in keys:
        params_str += str(params[key])
    params_str += secret_key
    print(params_str)
    return md5(params_str.encode('utf-8')).hexdigest()
print(params)




# 获取企业的相关联系方式：
def call_detail():
    url = "%s/api/open-api/enterprise/v2/contact" % host  #通过企业的enterprise_id获取（新接口）
    # params["task_id"] = "37622fce30453dea"
    # params["task_id"] = "37622fcfdec5380"
    # params["task_id"] = "37622fcfdec5380f1"
    # params["task_id"] = "6087a76be28548009d4713f6,6006370f976a3929da30b32e"
    # params["task_id"] = "深圳市腾讯计算机系统有限公司深圳市腾讯计算机系统有限公司深圳市腾讯计算机系统有限公司深圳市腾讯计算机系统有限" \
    #                           "公司深圳市腾讯计算机系统有限公司深圳市腾讯计算机系统有限公司深圳市腾讯计算机系统有限公司深圳市腾讯计算机系统" \
    #                           "有限公司深圳市腾讯计算机系统有限公司深圳市腾讯计算机系统有限公司深圳市腾讯计算机系统有限公司深圳市腾讯计算机系统有限公司"
    # params["task_id"] = "57887e6cf933756357887e6cf933756357887e6cf933756357887e6cf933756357887e6cf933756357887e6cf9337563" \
    #           "57887e6cf933756357887e6cf933756357887e6cf933756357887e6cf933756357887e6cf933756357887e6cf9337563" \
    #           "57887e6cf933756357887e6cf933756357887e6cf933756357887e6cf933756357887e6cf933756357887e6cf9337563"
    # params["task_id"] = "深圳市腾讯计算机系统有限公司"
    # params["task_id"] = "6006370f976a3929da30b32e"
    # params["task_id"] = "#$#%%^^%&&^%^&%^%"
    # params["task_id"] = "null"
    # params["task_id"] = "' or '1'<> '2 "
    # params["task_id"] = None
    # params["task_id"] = ""
    # params['task_id'] = "6087a76be28548009d4713f6"    # 99条记录
    # params['task_id'] = "6087a51ae28548009d4713b4"   # 10条记录
    # params['task_id'] = "5f0c3182976a3954af14e836"  # 60c2dc3d976a390bdac06de9
    # params["task_id"] = "5f0e5ab1976a39639b340f90"
    # params['enterprise_id'] = "37622fe9314536df"  #广州探迹科技有限公司
    # params['enterprise_id'] = None
    # params['enterprise_id'] = "' or '1'<> '2 "
    params['enterprise_id'] = "37622fe9314536df"
    # params['enterprise_id'] = None
    #params['begin'] = '0'
    #params["end"] = '200'

    params['signature'] = signature(secretKey)
    print(params)

    resp = requests.get(url, params=params)
    print(resp.status_code)
    # print(resp.content)
    print(resp.json())


if __name__ == "__main__":
    call_detail()
