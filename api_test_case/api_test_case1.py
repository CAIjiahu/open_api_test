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


class call_detail(unittest.TestCase):
    def setUp(self) -> None:
        log.info("==============init data==============")
        # self.proxies = {'http':'http://125.118.124.22:6666'}  # set the proxies to avoid IP seized
        pass

    def test_call_detail_parm_true(self):
        log.info("case 1:参数正确传递")
        task_id = "6087a76be28548009d4713f6"
        begin = 0
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['data'][0]['number'], '18825114992')
        self.assertEqual(result[1]['data'][1]['number'], '18818868994')
        self.assertEqual(result[1]['data'][2]['number'], '18818866959')
        self.assertEqual(result[1]['data'][3]['number'], '13822251231')
        self.assertEqual(result[1]['total'], 99)

    def test_call_detail_two_parms(self):
        log.info('case 2:一次传递两个ID')
        task_id = "6087a76be28548009d4713f6,6087a76be28548009d4713f6"
        begin = 0
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['data'], [])
        # self.assertEqual(result[1]['data'][1]['number'], '18910491046')
        # self.assertEqual(result[1]['data'][2]['number'], '18929653027')
        # self.assertEqual(result[1]['data'][3]['number'], '13621192346')
        self.assertEqual(result[1]['total'], 0)

    def test_call_detail_long_parm(self):
        log.info("case 3:长字符串")
        task_id = "57887e6cf933756357887e6cf933756357887e6cf933756357887e6cf933756357887e6cf933756357887e6cf9337563" \
               "57887e6cf933756357887e6cf933756357887e6cf933756357887e6cf933756357887e6cf933756357887e6cf9337563" \
               "57887e6cf933756357887e6cf933756357887e6cf933756357887e6cf933756357887e6cf933756357887e6cf9337563"
        begin = 0
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['code'], 'ParamsIllegal')
        self.assertEqual(result[1]['msgCN'], '非法参数')

    def test_call_detail_less_parm(self):
        log.info("case 4:传入的ID比实际少一位")
        task_id = "6087a76be28548009d4713f"
        begin = 0
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)

        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['data'], [])
        # self.assertEqual(result[1]['data'][1]['number'], '18910491046')
        # self.assertEqual(result[1]['data'][2]['number'], '18929653027')
        # self.assertEqual(result[1]['data'][3]['number'], '13621192346')
        self.assertEqual(result[1]['total'], 0)

    def test_call_detail_more_parm(self):
        log.info("case 5:传入的ID比实际多一位")
        task_id = "6087a76be28548009d4713f67"
        begin = 0
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)

        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['data'], [])
        # self.assertEqual(result[1]['data'][1]['number'], '18910491046')
        # self.assertEqual(result[1]['data'][2]['number'], '18929653027')
        # self.assertEqual(result[1]['data'][3]['number'], '13621192346')
        self.assertEqual(result[1]['total'], 0)

    def test_call_detail_notexist_parm(self):
        log.info("case 6:传入的不存在的ID")
        task_id = "57887e6cf933756"
        begin = 0
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)

        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['data'], [])
        # self.assertEqual(result[1]['data'][1]['number'], '18910491046')
        # self.assertEqual(result[1]['data'][2]['number'], '18929653027')
        # self.assertEqual(result[1]['data'][3]['number'], '13621192346')
        self.assertEqual(result[1]['total'], 0)

    def test_call_detail_no_parm(self):
        log.info("case 7:参数传入为空")
        task_id = ""
        begin = 0
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)

        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['code'], 'ParamsIllegal')
        self.assertEqual(result[1]['msgCN'], '非法参数')

    def test_call_detail_special_parm(self):
        log.info("case 8:传入特殊字符串")
        task_id = "#$#%%^&^%^%^&%^%☎☏✄☪☣☢☠♨« »큐〓㊚㊛囍㊒㊖☑✔☐☒✘㍿☯☰☷♥♠♤ ♂♀"
        begin = 0
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)

        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['data'], [])
        # self.assertEqual(result[1]['data'][1]['number'], '18910491046')
        # self.assertEqual(result[1]['data'][2]['number'], '18929653027')
        # self.assertEqual(result[1]['data'][3]['number'], '13621192346')
        self.assertEqual(result[1]['total'], 0)

    def test_call_detail_black_parm(self):
        log.info("case 9:参数传入为空格")
        task_id = "                 "
        begin = 0
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)

        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['data'], [])
        # self.assertEqual(result[1]['data'][1]['number'], '18910491046')
        # self.assertEqual(result[1]['data'][2]['number'], '18929653027')
        # self.assertEqual(result[1]['data'][3]['number'], '13621192346')
        self.assertEqual(result[1]['total'], 0)

    def test_call_detail_none_parm(self):
        log.info("case 10:参数传入为：None")
        task_id = None
        begin = 0
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)

        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['code'], 'ParamsInvalid')
        self.assertEqual(result[1]['msgCN'], '缺少必要的必填参数')

    def test_call_detail_parm_NULL(self):
        log.info("case 11:参数传入为：'NULL'")
        task_id = "NULL"
        begin = 0
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)

        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['data'], [])
        # self.assertEqual(result[1]['data'][1]['number'], '18910491046')
        # self.assertEqual(result[1]['data'][2]['number'], '18929653027')
        # self.assertEqual(result[1]['data'][3]['number'], '13621192346')
        self.assertEqual(result[1]['total'], 0)

    def test_call_detail_parm_null(self):
        log.info("case 12:参数传入为：'null'")
        task_id = "null"
        begin = 0
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)

        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['data'], [])
        # self.assertEqual(result[1]['data'][1]['number'], '18910491046')
        # self.assertEqual(result[1]['data'][2]['number'], '18929653027')
        # self.assertEqual(result[1]['data'][3]['number'], '13621192346')
        self.assertEqual(result[1]['total'], 0)

    def test_call_detail_100_word(self):
        log.info("case 13:参数传入为：100个字符长度数据")
        task_id = "60700c14976a3964fd86852760700c14976a3964fd86852760700c14976a3964fd86852760700c14976a3964fd8685276070"
        begin = 0
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)

        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['data'], [])
        # self.assertEqual(result[1]['data'][1]['number'], '18910491046')
        # self.assertEqual(result[1]['data'][2]['number'], '18929653027')
        # self.assertEqual(result[1]['data'][3]['number'], '13621192346')
        self.assertEqual(result[1]['total'], 0)

    def test_call_detail_101_word(self):
        log.info("case 14:参数传入为：101个字符长度数据")
        task_id = "60700c14976a3964fd86852760700c14976a3964fd86852760700c14976a3964fd86852760700c14976a3964fd86852760700"
        begin = 0
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)

        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['code'], 'ParamsIllegal')
        self.assertEqual(result[1]['msgCN'], '非法参数')

    def test_call_detail_23_word(self):
        log.info("case 15:参数传入为：23个字符长度数据")
        task_id = "60700c14976a3964fd86852"
        begin = 0
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)

        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['data'], [])
        # self.assertEqual(result[1]['data'][1]['number'], '18910491046')
        # self.assertEqual(result[1]['data'][2]['number'], '18929653027')
        # self.assertEqual(result[1]['data'][3]['number'], '13621192346')
        self.assertEqual(result[1]['total'], 0)

    def test_call_detail_CN_word(self):
        log.info("case 16:参数传入为：中文")
        task_id = "中文中文中文中文中文中文中文"
        begin = 0
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)

        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['data'], [])
        # self.assertEqual(result[1]['data'][1]['number'], '18910491046')
        # self.assertEqual(result[1]['data'][2]['number'], '18929653027')
        # self.assertEqual(result[1]['data'][3]['number'], '13621192346')
        self.assertEqual(result[1]['total'], 0)

    def test_call_detail_epl1_word(self):
        log.info("case 17:参数传入为：' or 1<> '1")
        task_id = "' or 1<> '1"
        begin = 0
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)

        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['data'], [])
        # self.assertEqual(result[1]['data'][1]['number'], '18910491046')
        # self.assertEqual(result[1]['data'][2]['number'], '18929653027')
        # self.assertEqual(result[1]['data'][3]['number'], '13621192346')
        self.assertEqual(result[1]['total'], 0)

    def test_call_detail_epl2_word(self):
        log.info('''case 19:参数传入为：<script>alert("123");</script>''')
        task_id = '<script>alert("123");</script>'
        begin = 0
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)

        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['data'], [])
        # self.assertEqual(result[1]['data'][1]['number'], '18910491046')
        # self.assertEqual(result[1]['data'][2]['number'], '18929653027')
        # self.assertEqual(result[1]['data'][3]['number'], '13621192346')
        self.assertEqual(result[1]['total'], 0)

    def test_call_detail_epl3_word(self):
        log.info("case 20:参数传入为：' ' or '1' = '1")
        task_id = "' or '1' = '1"
        begin = 0
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)

        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['data'], [])
        # self.assertEqual(result[1]['data'][1]['number'], '18910491046')
        # self.assertEqual(result[1]['data'][2]['number'], '18929653027')
        # self.assertEqual(result[1]['data'][3]['number'], '13621192346')
        self.assertEqual(result[1]['total'], 0)

    def test_call_detail_epl4_word(self):
        log.info("case 21:参数传入为：' or '1'<> '2")
        task_id = "' or '1'<> '2"
        begin = 0
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)

        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['data'], [])
        # self.assertEqual(result[1]['data'][1]['number'], '18910491046')
        # self.assertEqual(result[1]['data'][2]['number'], '18929653027')
        # self.assertEqual(result[1]['data'][3]['number'], '13621192346')
        self.assertEqual(result[1]['total'], 0)

    def test_call_detail_epl5_word(self):
        log.info("case 22:参数传入为：@&%……")
        task_id = "@&%……^<>()__"
        begin = 0
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)

        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['data'], [])
        # self.assertEqual(result[1]['data'][1]['number'], '18910491046')
        # self.assertEqual(result[1]['data'][2]['number'], '18929653027')
        # self.assertEqual(result[1]['data'][3]['number'], '13621192346')
        self.assertEqual(result[1]['total'], 0)

    def test_call_detail_channge_paraorder(self):
        log.info("case 23:调整参数顺序")
        begin = 0
        end = 200
        task_id = "6087a76be28548009d4713f6"
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['data'][0]['number'], '18825114992')
        self.assertEqual(result[1]['data'][1]['number'], '18818868994')
        self.assertEqual(result[1]['data'][2]['number'], '18818866959')
        self.assertEqual(result[1]['data'][3]['number'], '13822251231')
        self.assertEqual(result[1]['total'], 99)

    def test_call_detail_pages_true(self):
        log.info("case 24:页数begin=0，end=200")
        task_id = "6087a76be28548009d4713f6"
        begin = 0
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['data'][0]['callTime'], 1619503052808)
        self.assertEqual(result[1]['data'][98]['callTime'], 1619502955265)
        self.assertEqual(result[1]['total'], 99)

    def test_call_detail_pages_gaperror(self):
        log.info("case 25:页数begin=0，end=201")
        task_id = "6087a76be28548009d4713f6"
        begin = 0
        end = 201
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['code'], 'ParamsIllegal')
        self.assertEqual(result[1]['msgCN'], '非法参数')

    def test_call_detail_begin_greater_than_all(self):
        log.info("case 27:页数begin>查询任务通话数据量")
        task_id = "6087a76be28548009d4713f6"
        begin = 488
        end = 500
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['data'], [])
        self.assertEqual(result[1]['total'], 99)

    def test_call_detail_begin_pages_void(self):
        log.info("case 28:页数begin为空，end传入正常")
        task_id = "6087a76be28548009d4713f6"
        begin = ''
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 400)
        self.assertEqual(result[1]['err'], 10)
        self.assertEqual(result[1]['msg'], 'Bad Request')
        self.assertEqual(result[1]['sub_msg'], 'Params begin type error')

    def test_call_detail_end_pages_void(self):
        log.info("case 29:页数begin传入正常，end传入为空")
        task_id = "6087a76be28548009d4713f6"
        begin = 0
        end = ''
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 400)
        self.assertEqual(result[1]['err'], 10)
        self.assertEqual(result[1]['msg'], 'Bad Request')
        self.assertEqual(result[1]['sub_msg'], 'Params end type error')

    def test_call_detail_beginend_pages_void(self):
        log.info("case 30:页数begin和end均传入均为空")
        task_id = "6087a76be28548009d4713f6"
        begin = ''
        end = ''
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 400)
        self.assertEqual(result[1]['err'], 10)
        self.assertEqual(result[1]['msg'], 'Bad Request')
        self.assertEqual(result[1]['sub_msg'], 'Params begin type error')

    def test_call_detail_begin_greater_than_end(self):
        log.info("case 31:页数begin传入数值大于end传入数值")
        task_id = "6087a76be28548009d4713f6"
        begin = 50
        end = 20
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['code'], 'ParamsIllegal')
        self.assertEqual(result[1]['msgCN'], '非法参数')

    def test_call_detail_begin_is_null(self):
        log.info("case 32:页数begin传入为null/NULL/None")
        task_id = "6087a76be28548009d4713f6"
        begin = 'null'
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 400)
        self.assertEqual(result[1]['err'], 10)
        self.assertEqual(result[1]['msg'], 'Bad Request')
        self.assertEqual(result[1]['sub_msg'], 'Params begin type error')

    def test_call_detail_begin_is_NULL(self):
        log.info("case 33:页数begin传入为null/NULL/None")
        task_id = "6087a76be28548009d4713f6"
        begin = 'NULL'
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 400)
        self.assertEqual(result[1]['err'], 10)
        self.assertEqual(result[1]['msg'], 'Bad Request')
        self.assertEqual(result[1]['sub_msg'], 'Params begin type error')

    def test_call_detail_begin_is_None(self):
        log.info("case 34:页数begin传入为null/NULL/None")
        task_id = "6087a76be28548009d4713f6"
        begin = None
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['code'], 'SignatureError')
        self.assertEqual(result[1]['msgCN'], '请求的signature不正确')

    def test_call_detail_end_is_null(self):
        log.info("case 35:页数end传入为null/NULL/None")
        task_id = "6087a76be28548009d4713f6"
        begin = 0
        end = 'null'
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 400)
        self.assertEqual(result[1]['err'], 10)
        self.assertEqual(result[1]['msg'], 'Bad Request')
        self.assertEqual(result[1]['sub_msg'], 'Params end type error')

    def test_call_detail_end_is_NULL(self):
        log.info("case 36:页数end传入为null/NULL/None")
        task_id = "6087a76be28548009d4713f6"
        begin = 0
        end = 'NULL'
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 400)
        self.assertEqual(result[1]['err'], 10)
        self.assertEqual(result[1]['msg'], 'Bad Request')
        self.assertEqual(result[1]['sub_msg'], 'Params end type error')

    def test_call_detail_end_is_None(self):
        log.info("case 37:页数end传入为null/NULL/None")
        task_id = "6087a76be28548009d4713f6"
        begin = 0
        end = None
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['code'], 'SignatureError')
        self.assertEqual(result[1]['msgCN'], '请求的signature不正确')

    def test_call_detail_begin_is_space(self):
        log.info("case 38:页数begin传入为纯空格")
        task_id = "6087a76be28548009d4713f6"
        begin = '                                                '
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 400)
        self.assertEqual(result[1]['err'], 10)
        self.assertEqual(result[1]['msg'], 'Bad Request')
        self.assertEqual(result[1]['sub_msg'], 'Params begin type error')

    def test_call_detail_end_is_space(self):
        log.info("case 39:页数end传入为纯空格")
        task_id = "6087a76be28548009d4713f6"
        begin = 0
        end = '                                                '
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 400)
        self.assertEqual(result[1]['err'], 10)
        self.assertEqual(result[1]['msg'], 'Bad Request')
        self.assertEqual(result[1]['sub_msg'], 'Params end type error')

    def test_call_detail_begin_is_longstring(self):
        log.info("case 40:页数begin传入为超长字符串")
        task_id = "6087a76be28548009d4713f6"
        begin = '32323333333333333333333333333333333333333566666666666666666666666666666899999999999999999999998'
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['code'], 'ParamsIllegal')
        self.assertEqual(result[1]['msgCN'], '非法参数')

    def test_call_detail_end_is_longstring(self):
        log.info("case 41:页数end传入为超长字符串")
        task_id = "6087a76be28548009d4713f6"
        begin = 0
        end = '32323333333333333333333333333333333333333566666666666666666666666666666899999999999999999999998'
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['code'], 'ParamsIllegal')
        self.assertEqual(result[1]['msgCN'], '非法参数')

    def test_call_detail_begin_is_Chinese(self):
        log.info("case 42:页数begin传入中文字符串")
        task_id = "6087a76be28548009d4713f6"
        begin = '中文中文中文'
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 400)
        self.assertEqual(result[1]['err'], 10)
        self.assertEqual(result[1]['msg'], 'Bad Request')
        self.assertEqual(result[1]['sub_msg'], 'Params begin type error')

    def test_call_detail_end_is_Chinese(self):
        log.info("case 43:页数end传入中文字符串")
        task_id = "6087a76be28548009d4713f6"
        begin = 0
        end = '中文中文中文'
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 400)
        self.assertEqual(result[1]['err'], 10)
        self.assertEqual(result[1]['msg'], 'Bad Request')
        self.assertEqual(result[1]['sub_msg'], 'Params end type error')

    def test_call_detail_begin_is_English(self):
        log.info("case 44:页数begin传入英文字符串")
        task_id = "6087a76be28548009d4713f6"
        begin = 'dfdgrgtrgrgrgere'
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 400)
        self.assertEqual(result[1]['err'], 10)
        self.assertEqual(result[1]['msg'], 'Bad Request')
        self.assertEqual(result[1]['sub_msg'], 'Params begin type error')

    def test_call_detail_end_is_English(self):
        log.info("case 45:页数end传入英文字符串")
        task_id = "6087a76be28548009d4713f6"
        begin = 0
        end = 'dfdgrgtrgrgrgere'
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 400)
        self.assertEqual(result[1]['err'], 10)
        self.assertEqual(result[1]['msg'], 'Bad Request')
        self.assertEqual(result[1]['sub_msg'], 'Params end type error')

    def test_call_detail_begin_is_special_string1(self):
        log.info("case 46:页数begin传入特殊字符-' or 1<> '1")
        task_id = "6087a76be28548009d4713f6"
        begin = "' or 1<> '1"
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 400)
        self.assertEqual(result[1]['err'], 10)
        self.assertEqual(result[1]['msg'], 'Bad Request')
        self.assertEqual(result[1]['sub_msg'], 'Params begin type error')

    def test_call_detail_end_is_special_string1(self):
        log.info("case 47:页数end传入特殊字符-' or 1<> '1")
        task_id = "6087a76be28548009d4713f6"
        begin = 0
        end = "' or 1<> '1"
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 400)
        self.assertEqual(result[1]['err'], 10)
        self.assertEqual(result[1]['msg'], 'Bad Request')
        self.assertEqual(result[1]['sub_msg'], 'Params end type error')

    def test_call_detail_begin_is_special_string2(self):
        log.info("case 48:页数begin传入特殊字符-' or '1' = '1")
        task_id = "6087a76be28548009d4713f6"
        begin = "' or '1' = '1"
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 400)
        self.assertEqual(result[1]['err'], 10)
        self.assertEqual(result[1]['msg'], 'Bad Request')
        self.assertEqual(result[1]['sub_msg'], 'Params begin type error')

    def test_call_detail_end_is_special_string2(self):
        log.info("case 49:页数end传入特殊字符-' or '1' = '1")
        task_id = "6087a76be28548009d4713f6"
        begin = 0
        end = "' or '1' = '1"
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 400)
        self.assertEqual(result[1]['err'], 10)
        self.assertEqual(result[1]['msg'], 'Bad Request')
        self.assertEqual(result[1]['sub_msg'], 'Params end type error')

    def test_call_detail_begin_is_special_string3(self):
        log.info("case 50:页数begin传入特殊字符-' or '1'<> '2")
        task_id = "6087a76be28548009d4713f6"
        begin = "' or '1'<> '2"
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 400)
        self.assertEqual(result[1]['err'], 10)
        self.assertEqual(result[1]['msg'], 'Bad Request')
        self.assertEqual(result[1]['sub_msg'], 'Params begin type error')

    def test_call_detail_end_is_special_string3(self):
        log.info("case 51:页数end传入特殊字符-' or '1'<> '2")
        task_id = "6087a76be28548009d4713f6"
        begin = 0
        end = "' or '1'<> '2"
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 400)
        self.assertEqual(result[1]['err'], 10)
        self.assertEqual(result[1]['msg'], 'Bad Request')
        self.assertEqual(result[1]['sub_msg'], 'Params end type error')

    def test_call_detail_begin_is_special_string4(self):
        log.info('case 52:页数begin传入特殊字符-<script>alert("123");</script>')
        task_id = "6087a76be28548009d4713f6"
        begin = '<script>alert("123");</script>'
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 400)
        self.assertEqual(result[1]['err'], 10)
        self.assertEqual(result[1]['msg'], 'Bad Request')
        self.assertEqual(result[1]['sub_msg'], 'Params begin type error')

    def test_call_detail_end_is_special_string4(self):
        log.info('case 53:页数end传入特殊字符-<script>alert("123");</script>')
        task_id = "6087a76be28548009d4713f6"
        begin = 0
        end = '<script>alert("123");</script>'
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 400)
        self.assertEqual(result[1]['err'], 10)
        self.assertEqual(result[1]['msg'], 'Bad Request')
        self.assertEqual(result[1]['sub_msg'], 'Params end type error')

    def test_call_detail_begin_is_special_string5(self):
        log.info("case 54:页数begin传入特殊字符-#@%%%&^*()^<>{}[]""//'';\\\\|;;;::\\")
        task_id = "6087a76be28548009d4713f6"
        begin = '#@%%%&^*()^<>{}[]""//'';\\\\|;;;::\\'
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 400)
        self.assertEqual(result[1]['err'], 10)
        self.assertEqual(result[1]['msg'], 'Bad Request')
        self.assertEqual(result[1]['sub_msg'], 'Params begin type error')

    def test_call_detail_end_is_special_string5(self):
        log.info("case 55:页数end传入特殊字符-#@%%%&^*()^<>{}[]""//'';\\\\|;;;::\\")
        task_id = "6087a76be28548009d4713f6"
        begin = 0
        end = '#@%%%&^*()^<>{}[]""//'';\\\\|;;;::\\'
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 400)
        self.assertEqual(result[1]['err'], 10)
        self.assertEqual(result[1]['msg'], 'Bad Request')
        self.assertEqual(result[1]['sub_msg'], 'Params end type error')


    def test_call_detail_all_true(self):
        log.info("case 1:参数正确传递")
        task_id = "60c8212be285480813f740f1"
        begin = 0
        end = 200
        result = open_api_list.All_open_api().call_detail(task_id, begin, end)
        log.info(result)

        self.assertEqual(result[0], 200)
        self.assertEqual(result[1]['data'][161]['number'], '13760440611')
        self.assertEqual(result[1]['data'][161]['taskName'], '智能呼叫接口测试')
        self.assertEqual(result[1]['data'][161]['tpName'], '')
        self.assertEqual(result[1]['data'][161]['robotName'], '电话机器人01')
        self.assertEqual(result[1]['data'][161]['result'], '接通')
        self.assertEqual(result[1]['data'][161]['intention'], '其他')
        self.assertEqual(result[1]['data'][161]['graphName'], 'UAT-开放平台测试')
        self.assertEqual(result[1]['data'][161]['callTime'], 1616403853000)
        self.assertEqual(result[1]['data'][161]['duration'], '00:01:02')
        # self.assertEqual(result[1]['data'][161]['soundUrl'], 'http://mockingbird-dev.tangees.com/oss-download/dev/'
        #                                                      'recordings/sound/2021-03-22/5f0e5ab1976a39639b340f90'
        #                                                      '_02787873275.17-04-13.02787873275.wav?Signature=sdXw32'
        #                                                      'PByBRSgOZZaGn3i2jce8M%3D&Expires=1623834120&OSSAccessKe'
        #                                                      'yId=LTAI5tLvmfypHg1Nkq6fRyw5')
        # self.assertEqual(result[1]['data'][161]['textUrl'], 'http://mockingbird-dev.tangees.com/oss-download/dev/'
        #                                                     'recordings/text/2021-03-22/5f0e5ab1976a39639b340f90_02787873275'
        #                                                     '.tsv?Signature=t8FFPvdcokeyYfA0PUH4p3aH4n0%3D&Expires=1623834'
        #                                                     '120&OSSAccessKeyId=LTAI5tLvmfypHg1Nkq6fRyw5')
        self.assertIn('5f0e5ab1976a39639b340f90_02787873275.17-04-13.02787873275.wav', result[1]['data'][161]['soundUrl'])
        self.assertIn('5f0e5ab1976a39639b340f90_02787873275.tsv', result[1]['data'][161]['textUrl'])
        self.assertEqual(result[1]['total'], 162)



if __name__ == '__main__':
        unittest.main()