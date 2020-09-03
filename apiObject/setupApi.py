from common.httprequest import HttpRquest
from conf import config
from common.readyaml import read_yaml
from conf import read_path
import  requests
from common.logger import Log
from common.readyaml import update_yaml
from mysql.pymysql_db import Connectmysql
class SetupApi(object):

    http = HttpRquest()
    test_data = read_yaml(read_path.test_common, 'setupApi.yaml', config.url)
    test_data_f = read_yaml(read_path.test_common,'setupApi.yaml',config.url_f)
    test_data_c = read_yaml(read_path.test_common,'setupApi.yaml',config.url_c)
    test_data_u = read_yaml(read_path.test_common,'setupApi.yaml',config.url_u)

    #用户登录功能
    def login_v(self,user = None,pwd = None):
        """
        V端用户的登录
        :param user: 用户账号
        :param pwd:  用户密码
        :return: token 登录成功的token
        """
        if user != None and pwd != None:
            self.test_data[0]['param']['mobile'] = user
            self.test_data[0]['param']['password'] = pwd
        try:
            response = self.http.http_request(self.test_data[0]['method'], self.test_data[0]['url'],self.test_data[0]['param'],
                                    self.test_data[0]['header'], cookies=None)

            Log().info("登录状态码{0}".format(response))
            Log().info(self.test_data[0]['url'])

            self.result = response.json()


            Log().info("登录结果{0}".format(self.result))

            if 'result' in self.result.keys():

                if 'access_token' in self.result['result'].keys():

                    res = {}
                    res['access_token'] = self.result['result']['access_token']
                    res['uuid'] = self.result['result']['uuid']
                    return res

                else:
                    Log().error("登录失败啦")
            else:
                Log().error("登录失败啦")
        except Exception as e:
            Log().error("登录出错啦")
            raise e


    def login_f(self,user = None,pwd = None):
        """
        f端用户的登录
        :param user: 用户账号
        :param pwd:  用户密码
        :return: token 登录成功的token uuid
        """
        if user != None and pwd != None:
            self.test_data[1]['param']['mobile'] = user
            self.test_data[1]['param']['password'] = pwd
        try:
            response = self.http.http_request(self.test_data[1]['method'], self.test_data[1]['url'],self.test_data[1]['param'],
                                    self.test_data[1]['header'], cookies=None)

            Log().info("登录状态码{0}".format(response))
            Log().info(self.test_data[1]['url'])

            self.result = response.json()


            Log().info("登录结果{0}".format(self.result))

            if 'result' in self.result.keys():

                if 'access_token' in self.result['result'].keys():
                    res = {}
                    res['access_token'] = self.result['result']['access_token']
                    res['uuid'] =  self.result['result']['uuid']
                    return res

                else:
                    Log().error("登录失败啦")
            else:
                Log().error("登录失败啦")
        except Exception as e:
            Log().error("登录出错啦")
            raise e

    def login_c(self,user = None,pwd = None):
        """
        C端用户的登录
        :param user: 用户账号
        :param pwd:  用户密码
        :return: token 登录成功的token
        """
        if user != None and pwd != None:
            self.test_data[2]['param']['mobile'] = user
            self.test_data[2]['param']['password'] = pwd
        try:
            response = self.http.http_request(self.test_data[2]['method'], self.test_data[2]['url'],self.test_data[2]['param'],
                                    self.test_data[2]['header'], cookies=None)

            Log().info("登录状态码{0}".format(response))
            Log().info(self.test_data[2]['url'])

            self.result = response.json()


            Log().info("登录结果{0}".format(self.result))

            if 'result' in self.result.keys():

                if 'access_token' in self.result['result'].keys():

                    res = {}
                    res['access_token'] = self.result['result']['access_token']
                    res['uuid'] = self.result['result']['uuid']
                    return res

                else:
                    Log().error("登录失败啦")
            else:
                Log().error("登录失败啦")
        except Exception as e:
            Log().error("登录出错啦")
            raise e

    def login_wxappF(self,user = None,pwd = None):
        """
        F端小程序用户的登录
        :param user: 用户账号
        :param pwd:  用户密码
        :return: token 登录成功的token
        """
        if user != None and pwd != None:
            self.test_data[8]['param']['mobile'] = user
            self.test_data[8]['param']['password'] = pwd
        try:
            response = self.http.http_request(self.test_data[8]['method'], self.test_data[8]['url'], self.test_data[8]['param'],
                                    self.test_data[8]['header'], cookies=None)

            Log().info("登录状态码{0}".format(response))
            Log().info(self.test_data[8]['url'])

            self.result = response.json()


            Log().info("登录结果{0}".format(self.result))

            if 'result' in self.result.keys():

                if 'access_token' in self.result['result'].keys():

                    return self.result['result']['access_token']

                else:
                    Log().error("登录失败啦")
            else:
                Log().error("登录失败啦")
        except Exception as e:
            Log().error("登录出错啦")
            raise e

    def login_c_jianxin(self,user = None,pwd = None):
        """
        C端用户的登录
        :param user: 用户账号
        :param pwd:  用户密码
        :return: token 登录成功的token
        """
        if user != None and pwd != None:
            self.test_data[9]['param']['mobile'] = user
            self.test_data[9]['param']['password'] = pwd
        try:
            response = self.http.http_request(self.test_data[9]['method'], self.test_data[9]['url'], self.test_data[9]['param'],
                                    self.test_data[9]['header'], cookies=None)

            Log().info("登录状态码{0}".format(response))
            Log().info(self.test_data[9]['url'])

            self.result = response.json()


            Log().info("登录结果{0}".format(self.result))

            if 'result' in self.result.keys():

                if 'access_token' in self.result['result'].keys():

                    return self.result['result']['access_token']

                else:
                    Log().error("登录失败啦")
            else:
                Log().error("登录失败啦")
        except Exception as e:
            Log().error("登录出错啦")
            raise e

    def dotest(self):
        """
        新增个CV用户
        :return:
        """
        test_data = read_yaml(read_path.test_common, 'setupApi.yaml', config.url_u)

        mobile = update_yaml(read_path.commondata, 'data.yaml', 'mobile')
        test_data[4]['param']['mobile'] = mobile

        # 注册用户
        register_response = requests.request("POST", test_data[4]['url'], json=test_data[4]['param'],
                                             headers=test_data[4]['header'])
        print(register_response.json())

        login_response = self.login_v(mobile,"e10adc3949ba59abbe56e057f20f883e")
        print(login_response)
        self.test_data[5]['header']['access_token'] = login_response
        self.test_data[5]['param']['mobile'] = mobile
        adduser_response = requests.request("POST", self.test_data[5]['url'], json=self.test_data[5]['param'],
                                            headers=self.test_data[5]['header'])

    def createFUser(self):
        """
         创建一个已认证的F用户
        :return:
        """
        test_data = read_yaml(read_path.test_common, 'setupApi.yaml', config.url_u)

        mobile = update_yaml(read_path.commondata, 'data.yaml', 'mobile')
        test_data[10]['param']['mobile'] = mobile
        # 注册用户
        register_response = requests.request("POST", test_data[10]['url'], json=test_data[10]['param'],
                                             headers=test_data[10]['header'])

        # 登录
        access_token = self.login_f(user=mobile,pwd='e10adc3949ba59abbe56e057f20f883e')

        #添加F用户
        test_data[15]['header']['access_token'] = access_token['access_token']
        test_data[15]['param']['mobile'] = mobile
        e = requests.request("POST", test_data[15]['url'], json=test_data[15]['param'],
                                             headers=test_data[15]['header'])

        # 添加店铺昵称
        test_data[11]['header']['access_token'] = access_token['access_token']
        e = requests.request("POST", test_data[11]['url'], json=test_data[11]['param'],
                         headers=test_data[11]['header'])

        #添加店铺名称
        test_data[12]['header']['access_token'] = access_token['access_token']
        e = requests.request("POST", test_data[12]['url'], json=test_data[12]['param'],
                         headers=test_data[12]['header'])

        #添加客服信息
        test_data[13]['header']['access_token'] = access_token['access_token']
        e = requests.request("POST", test_data[13]['url'], json=test_data[13]['param'],
                         headers=test_data[13]['header'])

        #打款认证
        test_data[16]['header']['access_token'] = access_token['access_token']
        import time
        test_data[16]['param']['busi_no'] = int(round(time.time() * 1000))
        _result = requests.request("post", test_data[16]['url'], json=test_data[16]['param'],
                                   headers=test_data[16]['header'])
        uuid = _result.json()['result']['uuid']

        #获取认证金额
        test_data[14]['header']['access_token'] = access_token['access_token']
        _result = requests.request("get", test_data[14]['url'], json=test_data[14]['param'],
                         headers=test_data[14]['header'])
        pay_amount = _result.json()['result']['pay_amount']


        #金额认证
        test_data[17]['header']['access_token'] = access_token['access_token']
        test_data[17]['param']['tran_amount'] = pay_amount
        _result = requests.request("post", test_data[17]['url'], json=test_data[17]['param'],
                                   headers=test_data[17]['header'])
        con = Connectmysql("intbee")
        sql = 'UPDATE intbee_manufacture_authenticate set is_payment=1 WHERE uuid="%s";'%uuid
        con.update(sql)

        #给F账户充值金额
        sql = 'UPDATE intbee_bank_corporate set available_money=1000 WHERE uuid="%s";'%uuid
        count = con.update(sql)
        print(count)

        # #同时成为V用户
        test_data[18]['header']['access_token'] = access_token['access_token']
        test_data[18]['param']['mobile'] = mobile
        _result = requests.request("get", test_data[18]['url'], json=test_data[18]['param'],
                                   headers=test_data[18]['header'])

        #成为c用户
        test_data[19]['header']['access_token'] = access_token['access_token']
        test_data[19]['param']['mobile'] = mobile
        _result = requests.request("get", test_data[19]['url'], json=test_data[19]['param'],
                                   headers=test_data[19]['header'])

        res = {}
        res['mobile'] = mobile
        res['uuid'] = uuid
        res['access_token'] = access_token['access_token']
        return res


    def createCUser(self):
        """
            创建一个已认证的C用户
           :return:
        """
        test_data = read_yaml(read_path.test_common, 'setupApi.yaml', config.url_u)

        mobile = update_yaml(read_path.commondata, 'data.yaml', 'mobile')
        test_data[10]['param']['mobile'] = mobile

        # 注册用户
        requests.request("POST", test_data[10]['url'], json=test_data[10]['param'],
                                             headers=test_data[10]['header'])
        # 登录
        re = self.login_f(user=mobile, pwd='e10adc3949ba59abbe56e057f20f883e')

        #同时成为C用户
        test_data[19]['header']['access_token'] = re['access_token']
        test_data[19]['param']['mobile'] = mobile
        _result = requests.request("get", test_data[19]['url'], json=test_data[19]['param'],
                                   headers=test_data[19]['header'])
        res = {}
        res['mobile'] = mobile
        res['uuid'] =re['uuid']
        print(test_data[10])
        return res


    def createVUser(self):
        """
            创建一个已认证的V用户
           :return:
        """
        test_data = read_yaml(read_path.test_common, 'setupApi.yaml', config.url_u)

        mobile = update_yaml(read_path.commondata, 'data.yaml', 'mobile')
        # test_data[4]['param']['mobile'] = mobile
        #
        # # 注册用户
        # requests.request("POST", test_data[4]['url'], json=test_data[4]['param'],
        #                                      headers=test_data[4]['header'])

        test_data[10]['param']['mobile'] = mobile

        # 注册用户
        requests.request("POST", test_data[10]['url'], json=test_data[10]['param'],
                         headers=test_data[10]['header'])

        # 登录
        re = self.login_f(user=mobile, pwd='e10adc3949ba59abbe56e057f20f883e')

        # 成为V用户
        test_data[18]['header']['access_token'] = re['access_token']
        test_data[18]['param']['mobile'] = mobile
        _result = requests.request("get", test_data[18]['url'], json=test_data[18]['param'],
                                   headers=test_data[18]['header'])

        #绑定自媒体
        test_data[20]['header']['access_token'] = re['access_token']
        _result = requests.request("post", test_data[20]['url'], json=test_data[20]['param'],
                                   headers=test_data[20]['header'])

        print(_result.json())
        print(test_data[20])

        res = {}
        res['mobile'] = mobile
        res['uuid'] =re['uuid']
        print(test_data[10])
        return res

    def getpassword(self,user,flag):
        """
        获取验证码
        :param user:  手机号
        :param flag:  验证码类型
        :return:
        """
        self.test_data_u[3]['param']['mobile'] = user

        self.test_data_u[3]['param']['flag'] = flag
        response = requests.request(self.test_data_u[3]['method'], self.test_data_u[3]['url'],
                                    json=self.test_data_u[3]['param'], headers=self.test_data_u[3]['header'])
        result = response.json()
        return result['result']


    def fenxiao(self, app_key=None, app_secret=None):
        if app_secret != None and app_key != None:
            self.test_data[6]['param']['app_key'] = app_key
            self.test_data[6]['param']['app_secret'] = app_secret
        try:
            response = self.http.http_request(self.test_data[6]['method'], self.test_data[6]['url'],
                                              self.test_data[6]['param'],
                                              self.test_data[6]['header'], cookies=None)

            Log().info("登录状态码{0}".format(response))
            Log().info(self.test_data[6]['url'])

            self.result = response.json()

            Log().info("登录结果{0}".format(self.result))


            if 'result' in self.result.keys():

                if 'access_token' in self.result['result'].keys():

                    return self.result['result']['access_token']

                else:
                    Log().error("登录失败啦")
            else:
                Log().error("登录失败啦")
        except Exception as e:
            Log().error("登录出错啦")
            raise e

    def fenxiaofront(self, mobile=None, password=None):
        if mobile != None and password != None:
            self.test_data[7]['param']['mobile'] = mobile
            self.test_data[7]['param']['password'] = password
        try:
            response = self.http.http_request(self.test_data[7]['method'], self.test_data[7]['url'],
                                              self.test_data[7]['param'],
                                              self.test_data[7]['header'], cookies=None)

            Log().info("登录状态码{0}".format(response))
            Log().info(self.test_data[7]['url'])

            self.result = response.json()

            Log().info("登录结果{0}".format(self.result))

            if 'result' in self.result.keys():

                if 'access_token' in self.result['result'].keys():

                    return self.result['result']['access_token']

                else:
                    Log().error("登录失败啦")
            else:
                Log().error("登录失败啦")
        except Exception as e:
            Log().error("登录出错啦")
            raise e


    def user_register(self):
        test_data = read_yaml(read_path.test_common, 'setupApi.yaml', config.url_u)

        mobile = update_yaml(read_path.commondata, 'data.yaml', 'mobile')
        test_data[10]['param']['mobile'] = mobile

        # 注册用户
        register_response = requests.request("POST", test_data[10]['url'], json=test_data[10]['param'],
                                             headers=test_data[10]['header'])
        return mobile

if __name__ == '__main__':


    print(SetupApi().createVUser())





