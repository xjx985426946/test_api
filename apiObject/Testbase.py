import json
from common.logger import Log
from common.httprequest import HttpRquest
from apiObject.jsoncheck import Check
class BaseCase():
    result = None
    data = None
    def setup(self):
        Log().info("START".center(66, '*'))
        self.http = HttpRquest()
        self.check_json = Check()

    def send_request(self,data,cookies):
        """
        接口请求
        :param data: 测试数据
        :param cookies:
        :return: 接口返回值
        """
        self.data = data
        Log().info("执行用例: " + data['api_name'] + "-->" + data['discriptions'])
        response = self.http.http_request(data['method'], data['url'],
                                          data['param'],
                                          data['header'], cookies=cookies)

        print("请求值：".center(66, "-") + "\n", json.dumps(data, ensure_ascii=False, indent=2), "\n")
        print("返回状态码：".center(66, "-") + "\n", response.status_code, "\n")
        Log().info(response.status_code)
        self.result = response.json()
        return self.result



    def reassert(self):
        """
        返回值校验，校验方式为json校验
        :return:
        """
        # 判断结果是否与预期相符
        # try:
        #     assert self.result == self.data['Expect']
        #     Log().info("测试通过")
        # except AssertionError as e:  # 抛出断言错误异常
        #     Log().error("断言结果为False~{0}".format(e))
        #     raise e
        # finally:
        #     print("返回结果：".center(66, "-") + "\n", json.dumps(self.result, ensure_ascii=False, indent=2))

        re = self.check_json.check_json(self.data['Expect'],self.result)

        try:
            assert re == 'success'

            Log().info("测试通过")
        except AssertionError as e:  # 抛出断言错误异常
            Log().info( str(re))
            Log().error("断言结果为False~{0}".format(e))
            raise e
        finally:
            print("返回结果：".center(66, "-") + "\n", json.dumps(self.result, ensure_ascii=False, indent=2))

    def dbcheck(self):
        """
        数据库校验
        :return: True or False
        """
        pass

    def teardown(self):
        # 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格。
        Log().info("END".center(66, '*'))
        print('\n')

# class TestUserLogin(BaseCase):   # 这里直接继承BaseCase
#     data_list = [1,6]
#
#     #重写断言方法
#     def reassert(self):
#         assert self.result + 5 == self.data
#     @pytest.mark.parametrize("data",data_list)
#     def test_user_login_normal(self,data):
#         """level1:正常登录"""
#         self.send_request(data,cookies='111')
#         self.reassert()

