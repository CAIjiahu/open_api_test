"""
Description of this file
author:
copyright:
date created: 2021-05-01
python version: 3.8

模块作用：截图方法,将截取到的图片存储到指定路径
"""

from selenium import webdriver
import os


def insert_img(driver, filename):
    func_path = os.path.dirname(__file__)  # 获取inaert_img文件当前路径，os.path.dirname返回该路径的父目录
    print(func_path)

    base_dir = os.path.dirname(func_path)  # 获取function路径
    base = base_dir.replace('\\', '/')  # 把字符串中的 old 替换成 new，如果指定第三个参数max，则替换不超过 max 次,注意 replace 不会改变原 string 的内容
    # print(base)
    # now = time.strftime("%Y-%m-%d %H_%M_%S")
    filepath = base + '/test_report/screenshot/' + filename  # 拼接截图保存路径
    print("The screenshot is save as：%s" % filepath)
    driver.get_screenshot_as_file(filepath)  # 截取当前页面并保存到filepath路径中


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('http://www.sougou.com')
    insert_img(driver,'sougou.png')
    driver.quit()
