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

#accessToken = "1HT52J6F4EVZP8DRGKASOCXIMQLUB7W0"    # dev测试token 【测试】机器人测试企业2
#secretKey = "SX83UIFW7ZBCK1JR960PHMYG45LQVOAT"  # dev测试secret 【测试】机器人测试企业2
# # #
#accessToken = "3254NFZ8KQ7E0SCXRGULDTWHA1V9YOMP"    # dev测试token 【测试】KA融合版测试企业xwh
#secretKey = "53MV9XTB0ES6WFHI48271JPDYNZOUKQA"  # dev测试secret 【测试】KA融合版测试企业xwh
# accessToken = "9TGXF7NWK51EYDL03VQA846J2MUHPCRS"    # uat测试token
# secretKey = "W7KG2NQFLJ14TEISR9HADVC63ZPXBY85"  # uat测试secret
accessToken = "GW9HPDVYR6ESJ2I45XN7FQCLAK30ZT18"    # uat测试茶里token
secretKey = "2AD7415C6KUYN08VZJRQTIS3HEW9PMFL"  # uat测试茶里secret
#accessToken = "SYD7UMBNFXLKR8W30EI5CGJQZV2TO6A9"  # test测试token【测试】开放平台测试
#secretKey = "RQ8DJZKA3O5PLMN0HX7FIUBVYGST642W"  # test测试secret【测试】开放平台测试
#accessToken = "6XYM4HIO19QNKGP28WS7L5J3FUZERDVB"  # test测试token【测试】特斯联内嵌页测试
#secretKey = "HWLC34MAYOPNRX9U5SBEVQIK8D6GZTJ2"  # test测试secret【测试】特斯联内嵌页测试
# accessToken = "IPJVH9KLZ2UOSD8ENYQ1A3XCTWMF7460"    # 生产token
# secretKey = "USBJ52N46RCYLKW8EH0IMFOD9QAP3X1G"  # 生产secret
#host = "http://paas-dev.tangees.com"
#host = "http://paas-test.tangees.com"  #test测试主机
host = "http://paas-uat.tangees.com"   # UAT测试主机
# host = "https://paas.tungee.com"   # 生产主机
params = {
    "accessToken": accessToken,
    "timestamp": datetime.strftime(datetime.utcnow(), '%Y-%m-%dT%H:%M:%S')
}


def signature(secret_key):
    # params = {
    #     "accessToken": accessToken,
    #     "timestamp": datetime.strftime(datetime.utcnow(), '%Y-%m-%dT%H:%M:%S')
    # }
    keys = sorted(list(params.keys()))
    params_str = ''
    for key in keys:
        params_str += str(params[key])
    params_str += secret_key
    print(params_str)
    return md5(params_str.encode('utf-8')).hexdigest()


# 获取客户公海列表：
def pools_with_role():
    # params = {
    #     "accessToken": accessToken,
    #     "timestamp": datetime.strftime(datetime.utcnow(), '%Y-%m-%dT%H:%M:%S')
    # }
    url = "%s/api/open-api/crm/pools-with-role" % host
    params['signature'] = signature(secretKey)
    print(params)

    resp = requests.get(url, params=params)
    print(resp.status_code)
    # print(resp.content)
    print(resp.json())
    #print(resp.json()['data']['customer_pools'])

#获取客户字段信息
def company_user_profile():
    url = "%s/api/open-api/crm/company-user-profile" % host
    params['signature'] = signature(secretKey)
    print(params)

    resp = requests.get(url, params=params)
    print(resp.status_code)
    # print(resp.content)
    print(resp.json())
    #print(resp.json()['data']['customer_pools'])

#获取客户列表
def customers_list():
    url = "%s/api/open-api/crm/customers-list" % host
    params['begin'] = '0'
    params['end'] = '10'
    #params['company_user_id'] = '60f942e09604db466a38f058'
    #params['company_user_id'] = "60f942e09604db466a38f058"
    #params['company_collaborator_user_id'] = '60f942e09604db466a38f058'
    #params['pool_id'] ='Null'
    #params['search_field_id'] = 'company_name'
    #params['search_field_value'] = '广州'
    #params['source_ids'] = 'mobile_robot'
    #params['sort_field_id'] = 'last_follow_up_time'
    #params['sort_type'] = '0'
    #params['department_id'] = '601b9a109604db3511a60180'
    #params['follow_up_ids'] ='done'
    #params['business_tag_ids'] = '621485e11bfdb51bd358765f'
    params['business_tag_match_type'] = 'and'
    params['no_business_tags'] = '1'
    params['signature'] = signature(secretKey)
    print(params)

    resp = requests.get(url, params=params)
    print(resp.status_code)
    # print(resp.content)
    print(resp.json())
    #print(resp.json()['data']['customer_pools'])

#获取客户信息
def detail_info():
    url = "%s/api/open-api/crm/customer/detail-info" % host
    params['customer_id'] = '61e01f18e1522142df17f718'

    params['signature'] = signature(secretKey)
    print(params)

    resp = requests.get(url, params=params)
    print(resp.status_code)
    # print(resp.content)
    print(resp.json())
    #print(resp.json()['data']['customer_pools'])

#获取部门列表
def get_department_tree():
    url = "%s/api/open-api/account/get-department-tree" % host


    params['signature'] = signature(secretKey)
    print(params)

    resp = requests.get(url, params=params)
    print(resp.status_code)
    # print(resp.content)
    print(resp.json())
    #print(resp.json()['data']['customer_pools'])

#获取部门员工
def company_users():
    url = "%s/api/open-api/account/company-users" % host

    params['start'] = '0'
    params['end']  = '10'
    params['department_id'] ="61e7df61c21ab2049c959235"


    params['signature'] = signature(secretKey)
    print(params)

    resp = requests.get(url, params=params)
    print(resp.status_code)
    # print(resp.content)
    print(resp.json())
    #print(resp.json()['data']['customer_pools'])

#企业通用维度
def all_dimension():
    url = "%s/api/open-api/enterprise/all-dimension" % host

    params['enterprise_id'] = '37622fe9314536df'#广州探迹科技有限公司



    params['signature'] = signature(secretKey)
    print(params)

    resp = requests.get(url, params=params)
    print(resp.status_code)
    # print(resp.content)
    print(resp.json())
    #print(resp.json()['data']['customer_pools'])

#企业联系方式
def contact():
    url = "%s/api/open-api/enterprise/v2/contact" % host

    params['enterprise_id'] = '37622fe9314536df'  #广州探迹科技有限公司


    params['signature'] = signature(secretKey)
    print(params)

    resp = requests.get(url, params=params)
    print(resp.status_code)
    # print(resp.content)
    print(resp.json())
    #print(resp.json()['data']['customer_pools'])

#企业模糊搜索
def search():
    url = "%s/api/open-api/enterprises/search" % host
    params['start'] = '0'
    params['end'] = '10'
    params['keywords'] = '探迹'
    #params['sort'] = '1'
    params['filter'] = '{}'

    params['signature'] = signature(secretKey)
    print(params)

    resp = requests.get(url, params=params)
    print(resp.status_code)
    # print(resp.content)
    print(resp.json())
    #print(resp.json()['data']['customer_pools'])

#获取定制公海列表
def tag_lead_pools():
    url = "%s/api/open-api/sales-ka/tag-lead-pools" % host

    params['signature'] = signature(secretKey)
    print(params)

    resp = requests.get(url, params=params)
    print(resp.status_code)
    # print(resp.content)
    print(resp.json())
    #print(resp.json()['data']['customer_pools'])

#获取定制公海企业列表
def advance_search():
    url = "%s/api/open-api/sales-ka/advance-search" % host
    params['tag_id'] = '620f6cc185b2e959a977bcd6'
    params['begin'] = '0'
    params['end'] = '10'
    #params['rate'] = '1'

    params['signature'] = signature(secretKey)
    print(params)

    resp = requests.post(url, data=params)
    print(resp.status_code)
    # print(resp.content)
    print(resp.json())
    #print(resp.json()['data']['customer_pools'])

#获取企业定制维度信息
def key_info():
    url = "%s/api/open-api/sales-ka/key-info" % host
    params['entity_id'] = '37622fe6c405369c'
    #params['entity_type'] = 'enterprise'
    params['lead_pool_id'] = '620f3e8785b2e959a977b5b0'

    params['signature'] = signature(secretKey)
    print(params)

    resp = requests.get(url, params=params)
    print(resp.status_code)
    # print(resp.content)
    print(resp.json())
    #print(resp.json()['data']['customer_pools'])



if __name__ == "__main__":
    #pools_with_role()
    #company_user_profile()
    customers_list()
    #detail_info()
    #get_department_tree()
    #company_users()
    #all_dimension()
    #contact()
    #search()
    #tag_lead_pools()
    #advance_search()
    #key_info()
