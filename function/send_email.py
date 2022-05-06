"""
Description of this file
author:
copyright:
date created: 2021-05-01
python version: 3.8

模块作用：发送邮件
"""

import os
import smtplib   # emil send module
from email.mime.text import MIMEText  # definite emil content
from email.mime.multipart import MIMEMultipart  # user for emil attachment sending


def send_email(latest_report):
    # f = open(latest_report, 'rb')
    # # 将报告内容传给emil_content,邮件正文
    # email_content = f.read()
    # f.close()

    # sender function server
    # smtpserver = 'smtp.163.com' #163
    smtpserver = 'smtp.qq.com'
    # sender function's username and passworld
    # user = 'su_dl5599@163.com'  # 163
    # password = 'ejwqq169'   #163
    user = '986157657@qq.com'  # qq
    password = 'ajxhejdyceehbbdg'   # qq

    # send function address and reveive emil address
    # sender = 'su_dl5599@163.com'   # 163
    sender = '986157657@qq.com'  # qq
    receivers = ['986157657@qq.com', '1321145301@qq.com', 'su_dl5599@163.com']

    # send function theme and content
    suject = 'OPEN API 接口测试报告'
    content = '<html><h1 style="color:purple">这是本次新增接口的测试报告，请查收！</h1><p>下载后再打开查看效果更佳哦！</p></html>'

    # structure attachment content
    send_file = open(latest_report, 'rb').read()

    att = MIMEText(send_file, 'base64', 'utf-8')  # base64 二进制编码，主要针对附件传送进行编码
    att["Content-Type"] = 'application/octet-stream'  # 设定Content-Type,以字节流方式传送，附近为二进制文件
    att['Content-Disposition'] = 'attachment; filename ='+ os.path.split(latest_report)[1]  # 定义内容属性

    # structure send and receive message
    msgRoot = MIMEMultipart()  # 用于发送附件及中文内容
    msgRoot.attach(MIMEText(content, 'html', 'utf-8'))
    msgRoot['subject'] = suject
    msgRoot['From'] = sender
    msgRoot['To'] = ','.join(receivers)
    msgRoot.attach(att)

    # SSL nmp port is use 465
    smtp = smtplib.SMTP_SSL(smtpserver, 465)

    # HELO mark the user ID for server
    smtp.helo(smtpserver)
    # confirm the server return result
    smtp.ehlo(smtpserver)
    # the sending function server's username and password
    smtp.login(user, password)

    print("Start to send function...")
    smtp.sendmail(sender, receivers, msgRoot.as_string())
    smtp.quit()
    print("Email send end!")


if __name__ == '__main__':
    latest_report = r'D:\open_api_test\test_report\2021-04-08 20_41_57result.html'
    send_email(latest_report)