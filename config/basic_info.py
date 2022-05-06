"""
Description of this file
author:
copyright:
date created: 2021-05-01
python version: 3.8

基本信息配置：
accessToken：开放平台自建CRM-连接认证-连接信息中Client_Id
secretKey：开放平台自建CRM-连接认证-连接信息中Client_Secret
params:请求参数
"""
from datetime import datetime


'''本文件是用于公共参数配置（数据驱动理念架构）'''
# 主机地址：
# host = "http://paas-dev.tangees.com"    # dev测试主机
host = "http://paas-uat.tangees.com"   # UAT测试主机

# accessToken = "DW6HF5ZB829VCYGA14Q73RESTJOKUPIL"    # dev测试token 【测试】开放平台测试
# secretKey = "AFYTHE0MIRS7ZOPXN3LW6UK9D4V8J1C2"  # dev测试secret 【测试】开放平台测试

# accessToken = "YUXJRB5SKGAD9LVP78WHE0FICM32Q146"  # dev测试token 机器人企业2
# secretKey = "1KIN5C7QZJA8HSEORBLPV2T6Y3XW4MFD"  # dev测试secret  机器人企业2
#

accessToken = "9TGXF7NWK51EYDL03VQA846J2MUHPCRS"    # UAT测试token  【测试】开放平台测试
secretKey = "W7KG2NQFLJ14TEISR9HADVC63ZPXBY85"  # UAT测试secret 【测试】开放平台测试
params = {
            "accessToken": accessToken,
            # "timestamp": "2020-09-24T13:28:37",
            "timestamp": datetime.strftime(datetime.utcnow(), '%Y-%m-%dT%H:%M:%S')
        }


# url = "/api/open-api/demo1"
# url = "/api/open-api/enterprise/business"
# url = "/api/open-api/enterprise"


headers={"Host": "paas-dev.tangees.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip, deflate, br",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)" 
                      "Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68",
        "Cache-Control": "no-cache"}

# 测试环境的请求头
# {"Host": "api.pre.juejinchain.cn",
#         "Connection": "Keep-Alive",
#         "Accept-Encoding": "gzip",
#         "User-Agent": "okhttp/3.12.1",
#         "Cache-Control": "no-cache"}
#

# 正式环境的请求头
# {"Host": "api.juejinchain.com",
#         "Connection": "Keep-Alive",
#         "Accept-Encoding": "gzip",
#         "User-Agent": "okhttp/3.12.1",
#         "Cache-Control": "no-cache"}


# 邮箱通用参数
# 用来发送的邮箱账号和准许令牌密码
# sender='673421543@qq.com'
# psw="pkgaebmqnpcdbfei"
# 接收的邮箱账号
# receiver='2209715367@qq.com'
