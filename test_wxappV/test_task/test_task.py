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
        self.test_data = read_yaml(path_dir, 'test_task_data.yaml', config.url, token=token)

    @auth
    def reassert(self):
        assert self.result['code'] == 0
        assert self.result['message'] == 'SUCCESS'

    def test_caseone(self):
        '''V小程序-任务-任务列表-最热'''
        self.send_request(self.test_data[0], cookies=None)
        self.reassert()

    def test_casetwo(self):
        '''V小程序-任务-任务列表-最新'''
        self.send_request(self.test_data[1], cookies=None)
        self.reassert()
