import pytest
import time,os
from apiObject.setupApi import SetupApi
from common.save_value import SaveValue
from send_dingding import Message
import time

cur_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
path = cur_path + '/web/autotest/api/'

# mobile = SetupApi().createFUser()['mobile']
# print(mobile)
#
# mobile_v = SetupApi().createVUser()['mobile']
# print(mobile_v)
#
# mobile_c = SetupApi().createCUser()['mobile']
# print(mobile_c)


# F端用户登录
# res_f = SetupApi().login_f(mobile,'e10adc3949ba59abbe56e057f20f883e')
# SaveValue.TOKEN = res_f['access_token']
# SaveValue.F_UUID = res_f['uuid']
#
# # V端用户登录
# res_v = SetupApi().login_v(mobile_v,'e10adc3949ba59abbe56e057f20f883e')
# SaveValue.TOKEN_V = res_v['access_token']
# SaveValue.V_UUID = res_v['uuid']
#
# # C端用户登录
# res_c = SetupApi().login_c(mobile_c,'e10adc3949ba59abbe56e057f20f883e')
# SaveValue.TOKEN_C = res_c['access_token']
# SaveValue.C_UUID = res_c['uuid']

#F端用户登录
res_f = SetupApi().login_f("13902879682","25d55ad283aa400af464c76d713c07ad")
SaveValue.TOKEN = res_f['access_token']
SaveValue.F_UUID = res_f['uuid']

# C端用户登录
res_c = SetupApi().login_c("13729542194","b7ec7a6d28c12f213b79627fa75f588e")
SaveValue.TOKEN_C = res_c['access_token']
SaveValue.C_UUID = res_c['uuid']

# V端用户登录
res_v = SetupApi().login_v("13729542194","b7ec7a6d28c12f213b79627fa75f588e")
SaveValue.TOKEN_V = res_v['access_token']
SaveValue.V_UUID = res_v['uuid']


now = time.strftime("%Y-%m-%d")
xml_file = path + 'api_result.xml'
report_file = path + now +'_api_result.html'

pytest.main(["-m", "demos",
             "-vv",
             # "--reruns", "1",  #将错误的用例重跑两次
             # "--reruns-delay","1",
             "test_testenv",
             "--html=%s" % (report_file),
             "--junitxml=%s" % (xml_file)])

#发送邮件
# time.sleep(3) #等待三秒再发送邮件
# Message().sends_text()