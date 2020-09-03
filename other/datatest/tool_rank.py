#封神榜相关测试

#  活跃值测试

"""
1、注册新用户
2、浏览十个商品，分别浏览两次，得到10个活跃值，重复浏览商品，不算  V浏览
3、接卡5张卡，得到活跃值 5*5 = 25 V接卡
4、创建5个新的清单，得到活跃值 5*5 = 25   V创建
5、购买5个商品，得到活跃值 5 * 5 = 25   别人购买V的商品
6、蜂卡分享被访问10次 得到活跃值 10  V分享的被其他人看
7、小店分享被访问 得到活跃值 10
8、清单分享被访问  得到活跃值  10
以上活跃总值为  115
"""

#开始执行测试

from conf import config
from common.readyaml import read_yaml
from common.save_value import SaveValue
from apiObject.Testbase import BaseCase
import os
import requests
from conf import read_path
from common.readyaml import update_yaml
class Testrank(BaseCase):

    def __init__(self):

        self.path_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '/tooldata/'
        self.test_data = read_yaml(self.path_dir, 'tool_rank.yaml', config.url_u)

        self.mobile = update_yaml(read_path.commondata, 'data.yaml', 'mobile')
        self.test_data[0]['param']['mobile'] = self.mobile
        print(self.test_data[0]['param'])
        print(self.test_data[0]['url'])
        print(self.test_data[0]['header'])

    def dotest(self):

        #注册用户
        self.test_data[0]['param']['mobile'] = self.mobile
        register_response = requests.request("POST", self.test_data[0]['url'], json=self.test_data[0]['param'], headers=self.test_data[0]['header'])
        print(register_response.json())

        #登录用户
        self.test_data[1]['param']['mobile'] = self.mobile
        login_response = requests.request("POST", self.test_data[1]['url'], json=self.test_data[1]['param'],
                                    headers=self.test_data[1]['header'])
        print(login_response.json())


        #添加V用户
        self.test_data[2]['header']['access_token'] = login_response.json()['result']['access_token']
        self.test_data[2]['param']['mobile'] = self.mobile
        adduser_response = requests.request("get", self.test_data[2]['url'], json=self.test_data[2]['param'],
                                          headers=self.test_data[2]['header'])

        # adduser_response = requests.request("POST", self.test_data[5]['url'], json=self.test_data[2]['param'],
        #                                     headers=self.test_data[5]['header'])


    def __del__(self):
        class_name = self.__class__.__name__

if __name__ == '__main__':


    print(Testrank().dotest())

