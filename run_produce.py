import pytest
import time,os
from apiObject.setupApi import SetupApi
from common.save_value import SaveValue
from send_dingding_production import Message

token_c = SetupApi().login_c("13729542194","b7ec7a6d28c12f213b79627fa75f588e")['access_token']
SaveValue.TOKEN_C = token_c


token_f = SetupApi().login_f("13902879682","25d55ad283aa400af464c76d713c07ad")['access_token']
SaveValue.TOKEN = token_f

token_v = SetupApi().login_c("13729542194","b7ec7a6d28c12f213b79627fa75f588e")['access_token']
SaveValue.TOKEN_V = token_v


cur_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
path = cur_path + '/web/autotest/api/'


now = time.strftime("%Y-%m-%d")
xml_file =  path + 'apiproduction_result.xml'
report_file =  path + now +'_apiproduction_result.html'


pytest.main(["-m","produce",
             "-v",
             "test_prdenv",
             "--html=%s" %(report_file),
             "--junitxml=%s" %(xml_file)])

# Message().sends_text()


