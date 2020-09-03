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
        self.test_data = read_yaml(path_dir, 'test_merchantService_data.yaml', config.url, token=token)

    @auth
    def reassert(self):
        if self.data['case_id'] == 1:
            assert self.result['code'] == 0
            assert self.result['message'] == 'SUCCESS'
            assert self.result['result']['title'] == '【测算任务】佣金高达85%，分享占卜星座测算专属链接，帮你轻松流量变现  佣金 85%'
        elif self.data['case_id'] == 3:
            assert self.result['data'][0]['merchant_name'] == 'lingji'
        elif self.data['case_id'] == 4:
            assert self.result['result'][0]['channel_name'] == '5acec58aec68a84bc7c1b495'
        else:
            assert self.result['code'] == 0
            assert self.result['message'] == 'SUCCESS'

    def test_caseone(self):
        '''V小程序-测算-品类栏目列表'''
        self.send_request(self.test_data[0], cookies=None)
        self.reassert()

    def test_casetwo(self):
        '''V小程序-测算-任务描述'''
        self.send_request(self.test_data[1], cookies=None)
        self.reassert()

    def test_casethree(self):
        '''V小程序-测算-用户'''
        self.send_request(self.test_data[2], cookies=None)
        self.reassert()

    def test_casefour(self):
        '''V小程序-测算-商品列表'''
        self.send_request(self.test_data[3], cookies=None)
        self.reassert()

    def test_casefive(self):
        '''V小程序-测算-收益'''
        self.send_request(self.test_data[4], cookies=None)
        self.reassert()
