"""
Description of this file
author:
copyright:
date created: 2021-05-01
python version: 3.8

模块作用：查找最新报告
accessToken：开放平台自建CRM-连接认证-连接信息中Client_Id
secretKey：开放平台自建CRM-连接认证-连接信息中Client_Secret
params:请求参数
"""

import os


def latest_report(report_dir):
    lists = os.listdir(report_dir)  # 用于返回指定的文件夹包含的文件或文件夹的名字的列表
    lists.sort(key=lambda fn: os.path.getmtime(report_dir + '\\' + fn))
    # print(lists)
    # 输出最新报告的路径，os.path.join(path,name)连接目录与文件名或目录
    file_name = lists[-1]
    print("the latest report is:"+file_name)
    file = os.path.join(report_dir, lists[-1])
    # print(file)
    print("the latest report dir:%s" % file)
    return file


if __name__ == '__main__':
    report_dir = r'D:\open_api_test\test_report'
    latest_report(report_dir)