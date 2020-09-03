import pytest
import time,os
from apiObject.setupApi import SetupApi
from common.save_value import SaveValue

token = SetupApi().login_v()
SaveValue.TOKEN = token

token_c = SetupApi().login_c()
SaveValue.TOKEN_C = token_c

cookies_f = SetupApi().login_f()
SaveValue.COOKIES_F = cookies_f

token_V = SetupApi().login_c_jianxin()
SaveValue.TOKEN_wxappV = token_V

# token_u = SetupApi().login_u()
# SaveValue.token_u = token_u
# cookies_wc = SetupApi().login_cw()
# SaveValue.COOKIES_WC = cookies_wc

# token_shop = SetupApi().shop_center("bc3b2a3cda4e4cbca0f045b7becd180c","71bd7240fb904e26807197aebc1c41b3")
# token_shop = SetupApi().shop_center("bc3b2a3cda4e4cbca0f045b7becd180a","71bd7240fb904e26807197aebc1c41b4")
# SaveValue.SHOP_TOKEN = token_shop

# SaveValue.SHOP_AUTHRIZATION = 'aW50YmVlLWFwaTpmdzQxVmh6N1Y2OElkdWFGN0VBMUNnPT0='

cur_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
path = cur_path + '/web/autotest/api/'


now = time.strftime("%Y-%m-%d")
xml_file = path + 'api_result.xml'
report_file = path + now +'_api_result.html'


# def dorun():
#     pytest.main(["-m","domes",
#                  "-v",
#                  "test_case_V/",
#                  # "test_case_F/",
#                  # "test_case_C/",
#                  # "test_intbeebusiness_case",
#                  # "test_shop_center/test_createproduction.py",
#                  # "test_migration/test_category.py",
#                  "--html=%s" %(report_file),
#                  "--junitxml=%s" %(xml_file)])
#     time.sleep(60)

# import datetime
# def main(h=13, m=48):
#     '''h表示设定的小时，m为设定的分钟'''
#     while True:
#         # 判断是否达到设定时间，例如0:00
#         while True:
#             now = datetime.datetime.now()
#             # 到达设定时间，结束内循环
#             if now.hour == h and now.minute == m:
#                 break
#                 # 不到时间就等20秒之后再次检测
#             time.sleep(20)
#         # 做正事，一天做一次
#         dorun()
# main()

pytest.main(["-m", "demos",
             "-v",
             # "test_case_V2/test_bank/test_updatepassword.py",
             "--html=%s" % (report_file),
             "--junitxml=%s" % (xml_file)])

#
# from apiObject.procedure import Procedure
# Procedure().repay("101154518224437769")