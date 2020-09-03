import sys
sys.path.append("../")
from conf import config
from common.readyaml import read_yaml
import pytest
from common.save_value import SaveValue
from apiObject.Testbase import BaseCase
from common.Decorate import auth
import os

@pytest.mark.demos
class TestTaskData(BaseCase):

    def setup_class(self):
        token = SaveValue.TOKEN_wxappV
        path_dir = os.path.dirname(os.path.realpath(__file__)) + '/test_data/'
        self.test_data = read_yaml(path_dir, 'test_user_data.yaml', config.url, token=token)

    @auth
    def reassert(self):
        if self.data['case_id'] == 0:
            assert self.result['code'] == 0
            assert self.result['message'] == 'SUCCESS'
            assert self.result['result']['uuid'] == '5acec58aec68a84bc7c1b495'
        elif self.data['case_id'] == 2:
            assert self.result['result']['page_size'] == 10
        elif self.data['case_id'] == 3:
            assert self.result['result']['data'][0]['subcard_status'] == 9
        elif self.data['case_id'] == 4:
            assert self.result['result']['data'][0]['subcard_status'] == 24 or 21
        else:
            assert self.result['code'] == 0
            assert self.result['message'] == 'SUCCESS'

    def test_caseone(self):
        '''V小程序-我的-可提现金额'''
        self.send_request(self.test_data[0], cookies=None)
        self.reassert()

    def test_casetwo(self):
        '''V小程序-我的-用户授权绑定信息'''
        self.send_request(self.test_data[1], cookies=None)
        self.reassert()

    def test_casethree(self):
        '''V小程序-我的-我的任务列表-进行中'''
        self.send_request(self.test_data[2], cookies=None)
        self.reassert()

    def test_casefour(self):
        '''V小程序-我的-我的任务列表-已完成'''
        self.send_request(self.test_data[3], cookies=None)
        self.reassert()

    def test_casefive(self):
        '''V小程序-我的-我的任务列表-已失败'''
        self.send_request(self.test_data[4], cookies=None)
        self.reassert()

    def test_casesix(self):
        '''V小程序-我的-地址管理-地址列表'''
        self.send_request(self.test_data[5], cookies=None)
        self.reassert()
