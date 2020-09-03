import sys
sys.path.append("../")
from conf import config
from common.readyaml import read_yaml
import pytest
from common.save_value import SaveValue
from apiObject.Testbase import BaseCase
from common.Decorate import auth
from apiObject.setupApi import SetupApi
from other.tools import Tool
import os

@pytest.mark.demos
class TestTaskStatusData(BaseCase):

    def setup_class(self):
        token = SaveValue.TOKEN_wxappV
        path_dir = os.path.dirname(os.path.realpath(__file__)) + '/test_data/'
        self.test_data = read_yaml(path_dir, 'test_task_statuschange_data.yaml', config.url, token=token)

    def test_caseone(self):
        '''V小程序-任务-申请任务'''
        self.send_request(self.test_data[0], cookies=None)
        self.reassert()

    def test_casetwo(self):
        '''V小程序-任务-任务列表-最新'''
        self.send_request(self.test_data[1], cookies=None)
        self.reassert()
