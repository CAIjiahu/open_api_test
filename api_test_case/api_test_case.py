"""
Description of this file
author:
copyright:
date created: 2021-05-01
python version: 3.8

模块作用：封装用例
"""

import unittest
from open_api import open_api_list
from function.test_log import *

log = Log()


class contact_test(unittest.TestCase):
    def setUp(self) -> None:
        log.info("==============init data==============")
        # self.proxies = {'http':'http://125.118.124.22:6666'}  # set the proxies to avoid IP seized
        pass

    def test_contact_parm_true(self):
        log.info("case 1:The parm is true")
        data = "广州探迹科技有限公司"
        result = open_api_list.All_open_api().contact(data)
        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['code'], 'Success')
        self.assertEqual(result[1]['msgCN'], '请求成功')


    def test_contact_two_parms(self):
        log.info('case 2:The parm is true but send more than one campany at one time')
        data = "深圳市腾讯计算机系统有限公司,广州探迹科技有限公司"
        result = open_api_list.All_open_api().contact(data)
        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['code'], 'Success')
        self.assertEqual(result[1]['msgCN'], '请求成功')


    def test_contact_long_parm(self):
        log.info("case 3:The parm is illegal: send a long text")
        data = "深圳市腾讯计算机系统有限公司深圳市腾讯计算机系统有限公司深圳市腾讯计算机系统有限公司深圳市腾讯计算机系统有限公司深圳市腾" \
               "讯计算机系统有限公司深圳市腾讯计算机系统有限公司深圳市腾讯计算机系统有限公司深圳市腾讯计算机系统有限公司深圳市腾讯计算机系" \
               "统有限公司深圳市腾讯计算机系统有限公司深圳市腾讯计算机系统有限公司深圳市腾讯计算机系统有限公司"
        result = open_api_list.All_open_api().contact(data)
        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['code'], 'ParamsIllegal')
        self.assertEqual(result[1]['msgCN'], '非法参数')


    def test_contact_mistry_parm(self):
        log.info("case 4:The parm is illegal: fuzzy search,send a section word of a company name")
        data = "腾讯"
        result = open_api_list.All_open_api().contact(data)
        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['code'], 'Success')
        self.assertEqual(result[1]['msgCN'], '请求成功')
        self.assertEqual(result[1]['total'], 0)


    def test_contact_no_parm(self):
        log.info("case 5:The parm is illegal: send parm with ''")
        data = ""
        result = open_api_list.All_open_api().contact(data)
        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['code'], 'ParamsIllegal')
        self.assertEqual(result[1]['msgCN'], '非法参数')


    def test_contact_special_parm(self):
        log.info("case 6:The parm is illegal: send a string of special character"
                 "'#$#%%^&^%^%^&%^%☎☏✄☪☣☢☠♨« »큐〓㊚㊛囍㊒㊖☑✔☐☒✘㍿☯☰☷♥♠♤ ♂♀'")
        data = "#$#%%^&^%^%^&%^%☎☏✄☪☣☢☠♨« »큐〓㊚㊛囍㊒㊖☑✔☐☒✘㍿☯☰☷♥♠♤ ♂♀"
        result = open_api_list.All_open_api().contact(data)
        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['code'], 'Success')
        self.assertEqual(result[1]['msgCN'], '请求成功')
        self.assertEqual(result[1]['total'],0)


    def test_contact_black_parm(self):
        log.info("case 7:The parm is illegal: send a string of white space character")
        data = "    "
        result = open_api_list.All_open_api().contact(data)
        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['code'], 'ParamsIllegal')
        self.assertEqual(result[1]['msgCN'], '非法参数')


    def test_contact_none_parm(self):
        log.info("case 8:The parm is illegal: send parm with None")
        data = None
        result = open_api_list.All_open_api().contact(data)
        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['code'], 'ParamsInvalid')
        self.assertEqual(result[1]['msgCN'], '缺少必要的必填参数')


    def test_contact_parm_NULL(self):
        log.info("case 9:The parm is illegal: send the word 'NULL'")
        data = "NULL"
        result = open_api_list.All_open_api().contact(data)
        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['code'], 'Success')
        self.assertEqual(result[1]['msgCN'], '请求成功')
        self.assertEqual(result[1]['total'],0)


    def test_contact_parm_null(self):
        log.info("case 10:The parm is illegal: send the word 'null'")
        data = "null"
        result = open_api_list.All_open_api().contact(data)
        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['code'], 'Success')
        self.assertEqual(result[1]['msgCN'], '请求成功')
        self.assertEqual(result[1]['total'], 0)


if __name__ == '__main__':
        unittest.main()