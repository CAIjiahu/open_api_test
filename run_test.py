"""
Description of this file
author:
copyright:
date created: 2021-05-01
python version: 3.8

模块作用：执行测试用例，生成测试报告，并将最新的测试报告邮件发送到指定邮箱
report_dir：报告存放目录
test_dir：用例目录
"""

import unittest
from function.latest_report import latest_report
from function.send_email import send_email
from function.test_log import *
from BSTestRunner import BSTestRunner


report_dir = './test_report'
test_dir = './api_test_case'
log = Log()

log.info("Start to run test case...")
discovery = unittest.defaultTestLoader.discover(test_dir, pattern="api_test_case1.py")
# discover 方法筛选出来的用例，循环添加到测试套件中

now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_dir + '/' + now + 'result.html'

log.info("Start to write report")
# 运行前记得把BSTestRunner.py 120行‘unicode’ 换成‘str’
with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title="Test Report", description="localhost login test")
    runner.run(discovery)
f.close()

log.info("find latest report...")
# 查看最新的测试报告
latest_report = latest_report(report_dir)

log.info("Send function report...")
# 邮件发送报告
send_email(latest_report)

log.info("The End!")