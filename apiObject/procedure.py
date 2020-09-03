from common.save_value import SaveValue
from common.httprequest import HttpRquest
from common.logger import Log
from common.readyaml import read_yaml
from conf import read_path,config
from apiObject.setupApi import SetupApi
import json
from mysql.pymongo_db import Mongodb
from mysql.pymysql_db import Pydb
import time,hashlib,requests
from common.readyaml import update_yaml

class Procedure(object):


    Log().info("开始登录F端用户".center(66, "-"))
    print('开始登录F端用户'.center(66, "-"))
    cookies_f = SaveValue.COOKIES_F
    # cookies_f = SetupApi().login_f("13600000000","e10adc3949ba59abbe56e057f20f883e")
    if cookies_f != None:
        Log().info("F端用户登录成功")
        print('F端用户登录成功'.center(66, "-"))
    else:
        Log().info("F端用户登录失败".center(66, "-"))
        print('F端用户登录失败'.center(66, "-"))


    Log().info("开始登录V端用户".center(66, "-"))
    print('开始登录V端用户'.center(66, "-"))
    # token = SetupApi().login()
    token = SaveValue.TOKEN
    if token != None:
        Log().info("V端用户登录成功")
        print('V端用户登录成功'.center(66, "-"))
    else:
        Log().info("V端用户登录失败".center(66, "-"))
        print('V端用户登录失败'.center(66, "-"))


    # Log().info("开始登录wC端用户".center(66, "-"))   # www  环境
    # print('开始登录wC端用户'.center(66, "-"))
    # # cookies_wc = SetupApi().login_cw()
    # cookies_wc = SaveValue.COOKIES_WC
    # if cookies_wc != None:
    #     Log().info("wC端用户登录成功")
    #     print('wC端用户登录成功'.center(66, "-"))
    # else:
    #     Log().info("wC端用户登录失败".center(66, "-"))
    #     print('wC端用户登录失败'.center(66, "-"))


    Log().info("开始登录C端用户".center(66, "-"))  # www  环境
    print('开始登录C端用户'.center(66, "-"))
    # token_c = SetupApi().login_c()
    Authorization = SaveValue.TOKEN_C
    if Authorization != None:
        Log().info("C端用户登录成功")
        print('C端用户登录成功'.center(66, "-"))
    else:
        Log().info("C端用户登录失败".center(66, "-"))
        print('C端用户登录失败'.center(66, "-"))


    def __init__(self):

        self.test_data_f = read_yaml(read_path.procedure_data, 'procedure.yaml', config.url_f)
        self.test_data_v = read_yaml(read_path.procedure_data, 'procedure.yaml', config.url, token=self.token)
        self.test_data_wc = read_yaml(read_path.procedure_data, 'procedure.yaml', config.url_c,token=self.Authorization['token'])
        self.test_data_c = read_yaml(read_path.procedure_data, 'procedure.yaml', config.url_c, token=self.Authorization['token'])

    def createproduct(self):
        '''用户添加商品'''

        name = update_yaml(read_path.commondata, "data.yaml", 'num')
        self.test_data_f[0]['param']['title'] = self.test_data_f[0]['param']['title'] + str(name)
        Log().info("开始创建商品".center(66, "-"))
        print('开始创建商品'.center(66, "-"))
        Log().info("执行用例: " + self.test_data_f[0]['api_name'] + "-->" + self.test_data_f[0]['discriptions'])
        response = HttpRquest().http_request(self.test_data_f[0]['method'], self.test_data_f[0]['url'],
                                             self.test_data_f[0]['param'],
                                             self.test_data_f[0]['header'], cookies=self.cookies_f)
        if response.status_code == 200 :
            Log().info("商品创建成功".center(66, "-"))
            print('商品创建成功'.center(66, "-"))
        else:
            Log().info("商品创建失败".center(66, "-"))
            print('商品创建失败'.center(66, "-"))

        result = response.json()
        try:
            assert result['code'] == self.test_data_f[0]['Expect']['code']
            assert result['message'] == self.test_data_f[0]['Expect']['message']

        except AssertionError as e:  # 抛出断言错误异常
            Log().error("创建失败~{0}".format(e))
            print("商品创建失败")
            raise e
        finally:
            print("请求值：".center(66, "-") + "\n", json.dumps(self.test_data_f[0], ensure_ascii=False, indent=2), "\n")
            print("返回结果：".center(66, "-") + "\n", json.dumps(result, ensure_ascii=False, indent=2))

        return result

    def intbeecard_creation(self,product_id):
        '''定向发送蜂卡'''

        # d = Mongodb("intbee_product")
        # client = d.get_mongodb_client()
        # db = client.intbee_product
        # collection = db.intbee_store_product
        # # re = collection.find({'title': '流程测试的商品标题3'}).sort("_id", -1)
        # re = collection.find({'title': self.test_data_f[0]['param']['title']}).sort("_id", -1)
        # product_id = re[0]['_id']  # 保存商品id

        self.test_data_f[1]['param']['product_id'] = product_id

        # d.close()  # 关闭数据库


        Log().info("开始发送定向蜂卡".center(66, "-"))
        print('开始发送定向蜂卡'.center(66, "-"))
        Log().info("执行用例: " + self.test_data_f[1]['api_name'] + "-->" + self.test_data_f[1]['discriptions'])
        response = HttpRquest().http_request(self.test_data_f[1]['method'], self.test_data_f[1]['url'],
                                             self.test_data_f[1]['param'],
                                             self.test_data_f[1]['header'], cookies=self.cookies_f)
        if response.status_code == 200:
            Log().info("开始发送定向蜂卡成功".center(66, "-"))
            print('开始发送定向蜂卡成功'.center(66, "-"))
        else:
            Log().info("开始发送定向蜂卡失败".center(66, "-"))
            print('开始发送定向蜂卡失败'.center(66, "-"))

        result = response.json()
        try:
            assert result['code'] == self.test_data_f[1]['Expect']['code']
            assert result['message'] == self.test_data_f[1]['Expect']['message']

        except AssertionError as e:  # 抛出断言错误异常
            Log().error("开始发送定向蜂卡失败~{0}".format(e))
            print("开始发送定向蜂卡失败")
            raise e
        finally:
            print("请求值：".center(66, "-") + "\n", json.dumps(self.test_data_f[1], ensure_ascii=False, indent=2), "\n")
            print("返回结果：".center(66, "-") + "\n", json.dumps(result, ensure_ascii=False, indent=2))

        return result

    def intbeecard_creation2(self,product_id):

        self.test_data_f[14]['param']['product_id'] = product_id

        Log().info("开始发送普通蜂卡".center(66, "-"))
        print('成功发送普通蜂卡'.center(66, "-"))
        Log().info("执行用例: " + self.test_data_f[14]['api_name'] + "-->" + self.test_data_f[14]['discriptions'])
        response = HttpRquest().http_request(self.test_data_f[14]['method'], self.test_data_f[14]['url'],
                                             self.test_data_f[14]['param'],
                                             self.test_data_f[14]['header'], cookies=self.cookies_f)
        if response.status_code == 200:
            Log().info("开始发送普通蜂卡成功".center(66, "-"))
            print('开始发送普通蜂卡成功'.center(66, "-"))
        else:
            Log().info("开始发送普通蜂卡失败".center(66, "-"))
            print('开始发送普通蜂卡失败'.center(66, "-"))

        result = response.json()
        try:
            assert result['code'] == self.test_data_f[14]['Expect']['code']
            assert result['message'] == self.test_data_f[14]['Expect']['message']

        except AssertionError as e:  # 抛出断言错误异常
            Log().error("开始发送普通蜂卡失败~{0}".format(e))
            print("开始发送普通蜂卡失败")
            raise e
        finally:
            print("请求值：".center(66, "-") + "\n", json.dumps(self.test_data_f[14], ensure_ascii=False, indent=2), "\n")
            print("返回结果：".center(66, "-") + "\n", json.dumps(result, ensure_ascii=False, indent=2))

        return result


    def intbeecardacception(self,id):  #定向蜂卡时传subcard_id  普通卡时传card_id
        '''V端用户将定向峰卡上架'''

        Log().info("开始上架蜂卡".center(66, "-"))
        print('开始上架蜂卡'.center(66, "-"))

        self.test_data_v[2]['url'] = self.test_data_v[2]['url'] + str(id) + '/acception'
        Log().info("执行用例: " + self.test_data_v[2]['api_name'] + "-->" + self.test_data_v[2]['discriptions'])
        response = HttpRquest().http_request(self.test_data_v[2]['method'], self.test_data_v[2]['url'],
                                             self.test_data_v[2]['param'],
                                             self.test_data_v[2]['header'], cookies=None)


        if response.status_code == 200:
            Log().info("上架蜂卡成功".center(66, "-"))
            print('上架蜂卡成功'.center(66, "-"))
        else:
            Log().info("上架蜂卡失败".center(66, "-"))
            print('上架蜂卡失败'.center(66, "-"))

        result = response.json()
        try:
            assert result['code'] == self.test_data_v[2]['Expect']['code']
            assert result['message'] == self.test_data_v[2]['Expect']['message']

        except AssertionError as e:  # 抛出断言错误异常
            Log().error("上架蜂卡失败~{0}".format(e))
            print("上架蜂卡失败")
            raise e
        finally:
            print("请求值：".center(66, "-") + "\n", json.dumps(self.test_data_v[2], ensure_ascii=False, indent=2), "\n")
            print("返回结果：".center(66, "-") + "\n", json.dumps(result, ensure_ascii=False, indent=2))

        return result

    def commitorder(self,product_id,card_id,subcard_id):
        '''C端用户提交订单'''

        Log().info("开始提交订单".center(66, "-"))
        print('开始提交订单'.center(66, "-"))

        # 替换参数
        self.test_data_wc[3]['url'] = self.test_data_wc[3]['url'] + str(product_id) + '/subscription/order'
        self.test_data_wc[3]['param']['subcard_id'] = subcard_id
        self.test_data_wc[3]['param']['sku_list'][0]['sku'] = 'F' + str(product_id) + str(card_id) + '1'

        Log().info("执行用例: " + self.test_data_wc[3]['api_name'] + "-->" + self.test_data_wc[3]['discriptions'])
        response = HttpRquest().http_request(self.test_data_wc[3]['method'], self.test_data_wc[3]['url'],
                                             self.test_data_wc[3]['param'],
                                             self.test_data_wc[3]['header'], cookies=self.Authorization['cookies'])
        if response.status_code == 200:
            Log().info("提交订单成功".center(66, "-"))
            print('提交订单成功'.center(66, "-"))
        else:
            Log().info("提交订单失败".center(66, "-"))
            print('提交订单失败'.center(66, "-"))

        result = response.json()
        try:
            assert result['code'] == self.test_data_wc[3]['Expect']['code']
            assert result['message'] == self.test_data_wc[3]['Expect']['message']

        except AssertionError as e:  # 抛出断言错误异常
            Log().error("提交订单失败~{0}".format(e))
            print("提交订单失败")
            raise e
        finally:
            print("请求值：".center(66, "-") + "\n", json.dumps(self.test_data_wc[3], ensure_ascii=False, indent=2), "\n")
            print("返回结果：".center(66, "-") + "\n", json.dumps(result, ensure_ascii=False, indent=2))

        return result

    def order2friend(self,product_id,card_id,subcard_id):
        '''用户提交送朋友订单'''

        Log().info("开始提交订单".center(66, "-"))
        print('开始提交订单'.center(66, "-"))

        # 替换参数
        self.test_data_wc[16]['url'] = self.test_data_wc[16]['url'] + str(product_id) + '/subscription/order2friend'
        self.test_data_wc[16]['param']['subcard_id'] = subcard_id
        self.test_data_wc[16]['param']['sku_list'][0]['sku'] = 'F' + str(product_id) + str(card_id) + '1'

        Log().info("执行用例: " + self.test_data_wc[16]['api_name'] + "-->" + self.test_data_wc[16]['discriptions'])
        response = HttpRquest().http_request(self.test_data_wc[16]['method'], self.test_data_wc[16]['url'],
                                             self.test_data_wc[16]['param'],
                                             self.test_data_wc[16]['header'], cookies=self.Authorization['cookies'])
        if response.status_code == 200:
            Log().info("提交订单成功".center(66, "-"))
            print('提交订单成功'.center(66, "-"))
        else:
            Log().info("提交订单失败".center(66, "-"))
            print('提交订单失败'.center(66, "-"))

        result = response.json()
        try:
            assert result['code'] == self.test_data_wc[16]['Expect']['code']
            assert result['message'] == self.test_data_wc[16]['Expect']['message']

        except AssertionError as e:  # 抛出断言错误异常
            Log().error("提交订单失败~{0}".format(e))
            print("提交订单失败")
            raise e
        finally:
            print("请求值：".center(66, "-") + "\n", json.dumps(self.test_data_wc[16], ensure_ascii=False, indent=2), "\n")
            print("返回结果：".center(66, "-") + "\n", json.dumps(result, ensure_ascii=False, indent=2))

        return result


    def alipay(self,order_id,order_no):
        '''进入支付宝支付页面'''

        Log().info("开始进入支付页面".center(66, "-"))
        print('开始进入支付页面'.center(66, "-"))
        self.test_data_wc[4]['header']['app_id'] = '101'
        self.test_data_wc[4]['url'] = self.test_data_wc[4]['url'] + str(order_id) + '/' + str(order_no) + '/alipay'

        Log().info("执行用例: " + self.test_data_wc[4]['api_name'] + "-->" + self.test_data_wc[4]['discriptions'])
        response = HttpRquest().http_request(self.test_data_wc[4]['method'], self.test_data_wc[4]['url'],
                                             self.test_data_wc[4]['param'],
                                             self.test_data_wc[4]['header'], cookies=self.Authorization['cookies'])

        if response.status_code == 200:
            Log().info("进入支付页面成功".center(66, "-"))
            print('进入支付页面成功'.center(66, "-"))
        else:
            Log().info("进入支付页面失败".center(66, "-"))
            print('进入支付页面失败'.center(66, "-"))

        result = response.json()
        try:
            assert result['code'] == self.test_data_wc[4]['Expect']['code']
            assert result['message'] == self.test_data_wc[4]['Expect']['message']

        except AssertionError as e:  # 抛出断言错误异常
            Log().error("进入支付页面失败~{0}".format(e))
            print("进入支付页面失败")
            raise e
        finally:
            print("请求值：".center(66, "-") + "\n", json.dumps(self.test_data_wc[4], ensure_ascii=False, indent=2), "\n")
            print("返回结果：".center(66, "-") + "\n", json.dumps(result, ensure_ascii=False, indent=2))

        return result

    def wxpay(self, order_id, order_no):
        '''进入微信支付页面'''

        Log().info("开始进入支付页面".center(66, "-"))
        print('开始进入支付页面'.center(66, "-"))
        self.test_data_wc[4]['header']['app_id'] = '101'
        self.test_data_wc[4]['url'] = self.test_data_wc[4]['url'] + str(order_id) + '/' + str(order_no) + '/wxpay'

        Log().info("执行用例: " + self.test_data_wc[4]['api_name'] + "-->" + self.test_data_wc[4]['discriptions'])
        response = HttpRquest().http_request(self.test_data_wc[4]['method'], self.test_data_wc[4]['url'],
                                             self.test_data_wc[4]['param'],
                                             self.test_data_wc[4]['header'], cookies=self.Authorization['cookies'])

        if response.status_code == 200:
            Log().info("进入支付页面成功".center(66, "-"))
            print('进入支付页面成功'.center(66, "-"))
        else:
            Log().info("进入支付页面失败".center(66, "-"))
            print('进入支付页面失败'.center(66, "-"))

        result = response.json()
        try:
            assert result['code'] == self.test_data_wc[4]['Expect']['code']
            assert result['message'] == self.test_data_wc[4]['Expect']['message']

        except AssertionError as e:  # 抛出断言错误异常
            Log().error("进入支付页面失败~{0}".format(e))
            print("进入支付页面失败")
            raise e
        finally:
            print("请求值：".center(66, "-") + "\n", json.dumps(self.test_data_wc[4], ensure_ascii=False, indent=2), "\n")
            print("返回结果：".center(66, "-") + "\n", json.dumps(result, ensure_ascii=False, indent=2))

        return result



    def deleteorder(self,order_id):
        '''取消订单'''
        Log().info("开始取消订单".center(66, "-"))
        print('开始取消订单'.center(66, "-"))

        self.test_data_c[5]['url'] = self.test_data_c[5]['url'] + str(order_id)

        Log().info("执行用例: " + self.test_data_c[5]['api_name'] + "-->" + self.test_data_c[5]['discriptions'])
        response = HttpRquest().http_request(self.test_data_c[5]['method'], self.test_data_c[5]['url'],
                                             self.test_data_c[5]['param'],
                                             self.test_data_c[5]['header'], cookies=None)
        print("请求值：".center(66, "-") + "\n", json.dumps(self.test_data_c[5], ensure_ascii=False, indent=2), "\n")
        print("返回结果：".center(66, "-") + "\n", response)

        if response.status_code == 200:
            Log().info("取消订单成功".center(66, "-"))
            print('取消订单成功'.center(66, "-"))
        else:
            Log().info("取消订单失败".center(66, "-"))
            print('取消订单失败'.center(66, "-"))

        result = response.json()
        try:
            assert result['code'] == self.test_data_c[5]['Expect']['code']
            assert result['message'] == self.test_data_c[5]['Expect']['message']

        except AssertionError as e:  # 抛出断言错误异常
            Log().error("取消订单失败~{0}".format(e))
            print("取消订单失败")
            raise e
        finally:
            print("请求值：".center(66, "-") + "\n", json.dumps(self.test_data_c[5], ensure_ascii=False, indent=2), "\n")
            print("返回结果：".center(66, "-") + "\n", json.dumps(result, ensure_ascii=False, indent=2))

        return result


    def searchrorder(self,order_no,status):
        '''F查询订单状态'''
        Log().info("开始查询订单".center(66, "-"))
        print('成功查询订单'.center(66, "-"))

        self.test_data_f[6]['param']['keys'] = order_no
        #替换参数
        self.test_data_f[6]['Expect']['status'] = status

        Log().info("执行用例: " + self.test_data_f[6]['api_name'] + "-->" + self.test_data_f[6]['discriptions'])
        response = HttpRquest().http_request(self.test_data_f[6]['method'], self.test_data_f[6]['url'],
                                             self.test_data_f[6]['param'],
                                             self.test_data_f[6]['header'], cookies=self.cookies_f)


        if response.status_code == 200:
            Log().info("查询订单成功".center(66, "-"))
            print('查询订单成功'.center(66, "-"))
        else:
            Log().info("查询订单失败".center(66, "-"))
            print('查询订单失败'.center(66, "-"))

        result = response.json()
        try:
            assert result['code'] == self.test_data_f[6]['Expect']['code']
            assert result['message'] == self.test_data_f[6]['Expect']['message']
            assert result['result'][0]['status'] == self.test_data_f[6]['Expect']['status']

        except AssertionError as e:  # 抛出断言错误异常
            Log().error("查询订单断言失败~{0}".format(e))
            print("查询订单断言失败")
            raise e
        finally:
            print("请求值：".center(66, "-") + "\n", json.dumps(self.test_data_f[6], ensure_ascii=False, indent=2), "\n")
            print("返回结果：".center(66, "-") + "\n", json.dumps(result, ensure_ascii=False, indent=2))

        return result

    def deliver(self,order_id):
        '''F端发货'''
        Log().info("F端开始发货".center(66, "-"))
        print('成功发货'.center(66, "-"))

        self.test_data_f[7]['url'] = self.test_data_f[7]['url'] + str(order_id)

        Log().info("执行用例: " + self.test_data_f[7]['api_name'] + "-->" + self.test_data_f[7]['discriptions'])
        response = HttpRquest().http_request(self.test_data_f[7]['method'], self.test_data_f[7]['url'],
                                             self.test_data_f[7]['param'],
                                             self.test_data_f[7]['header'], cookies=self.cookies_f)

        if response.status_code == 200:
            Log().info("发货成功".center(66, "-"))
            print('发货成功'.center(66, "-"))
        else:
            Log().info("发货失败".center(66, "-"))
            print('发货失败'.center(66, "-"))

        result = response.json()
        try:
            assert result['code'] == self.test_data_f[7]['Expect']['code']
            assert result['message'] == self.test_data_f[7]['Expect']['message']


        except AssertionError as e:  # 抛出断言错误异常
            Log().error("发货接口断言失败~{0}".format(e))
            print("发货接口断言失败")
            raise e
        finally:
            print("请求值：".center(66, "-") + "\n", json.dumps(self.test_data_f[7], ensure_ascii=False, indent=2), "\n")
            print("返回结果：".center(66, "-") + "\n", json.dumps(result, ensure_ascii=False, indent=2))



    # def derliverorder(self):
    #     '''C端查看收货信息'''
    #     Log().info("C端开始查看收货信息".center(66, "-"))
    #     print('C端开始查看收货信息'.center(66, "-"))
    #
    #
    #
    #     Log().info("执行用例: " + self.test_data_c[8]['api_name'] + "-->" + self.test_data_c[8]['discriptions'])
    #     response = HttpRquest().http_request(self.test_data_c[8]['method'], self.test_data_c[8]['url'],
    #                                          self.test_data_c[8]['param'],
    #                                          self.test_data_c[8]['header'], cookies=None)
    #
    #
    #     if response.status_code == 200:
    #         Log().info("C端开始查看收货信息成功".center(66, "-"))
    #         print('C端开始查看收货信息成功'.center(66, "-"))
    #     else:
    #         Log().info("C端开始查看收货信息失败".center(66, "-"))
    #         print('C端开始查看收货信息失败'.center(66, "-"))
    #
    #     result = response.json()
    #     try:
    #         assert result['code'] == self.test_data_c[8]['Expect']['code']
    #         assert result['message'] == self.test_data_c[8]['Expect']['message']
    #
    #
    #     except AssertionError as e:  # 抛出断言错误异常
    #         Log().error("查看收获信息断言失败断言失败~{0}".format(e))
    #         print("查看收获信息断言失败")
    #         raise e
    #     finally:
    #         print("请求值：".center(66, "-") + "\n", json.dumps(self.test_data_f[8], ensure_ascii=False, indent=2), "\n")
    #         print("返回结果：".center(66, "-") + "\n", json.dumps(result, ensure_ascii=False, indent=2))

    def orderconfirm(self,order_id):
        '''C端确认收货'''
        Log().info("C端开始确认发货".center(66, "-"))
        print('成功确认发货'.center(66, "-"))

        #替换参数
        self.test_data_c[9]['url'] = self.test_data_c[9]['url'] + str(order_id)

        Log().info("执行用例: " + self.test_data_c[9]['api_name'] + "-->" + self.test_data_c[9]['discriptions'])
        response = HttpRquest().http_request(self.test_data_c[9]['method'], self.test_data_c[9]['url'],
                                             self.test_data_c[9]['param'],
                                             self.test_data_c[9]['header'], cookies=None)

        if response.status_code == 200:
            Log().info("确认收货成功".center(66, "-"))
            print('确认收货成功'.center(66, "-"))
        else:
            Log().info("确认发货失败".center(66, "-"))
            print('确认发货失败'.center(66, "-"))

        result = response.json()
        try:
            assert result['code'] == self.test_data_c[9]['Expect']['code']
            assert result['message'] == self.test_data_c[9]['Expect']['message']


        except AssertionError as e:  # 抛出断言错误异常
            Log().error("确认收货断言失败~{0}".format(e))
            print("确认收货断言失败")
            raise e
        finally:
            print("请求值：".center(66, "-") + "\n", json.dumps(self.test_data_c[9], ensure_ascii=False, indent=2), "\n")
            print("返回结果：".center(66, "-") + "\n", json.dumps(result, ensure_ascii=False, indent=2))



    def applyrefund(self,order_id,order_no):
        '''C端申请退款'''

        Log().info("C端开始申请退款".center(66, "-"))
        print('C端开始申请退款'.center(66, "-"))

        # 替换参数
        self.test_data_c[10]['url'] =  self.test_data_c[10]['url'] + str(order_no)
        self.test_data_c[10]['param']['order_id'] = order_id
        Log().info("执行用例: " + self.test_data_c[10]['api_name'] + "-->" + self.test_data_c[10]['discriptions'])
        response = HttpRquest().http_request(self.test_data_c[10]['method'], self.test_data_c[10]['url'],
                                             self.test_data_c[10]['param'],
                                             self.test_data_c[10]['header'], cookies=None)

        if response.status_code == 200:
            Log().info("确认收货成功".center(66, "-"))
            print('确认收货成功'.center(66, "-"))
        else:
            Log().info("确认发货失败".center(66, "-"))
            print('确认发货失败'.center(66, "-"))

        result = response.json()
        try:
            assert result['code'] == self.test_data_c[10]['Expect']['code']
            assert result['message'] == self.test_data_c[10]['Expect']['message']


        except AssertionError as e:  # 抛出断言错误异常
            Log().error("确认收货断言失败~{0}".format(e))
            print("确认收货断言失败")
            raise e
        finally:
            print("请求值：".center(66, "-") + "\n", json.dumps(self.test_data_c[10], ensure_ascii=False, indent=2), "\n")
            print("返回结果：".center(66, "-") + "\n", json.dumps(result, ensure_ascii=False, indent=2))


    def batch(self, product_id):
        ''' 用户评价功能'''
        Log().info("C端用户评价后开始评价商品".center(66, "-"))
        print('C端用户评价后开始评价商品'.center(66, "-"))

        # 替换参数
        self.test_data_c[11]['url'] = self.test_data_c[11]['url'] + str(product_id) + '/batch'
        self.test_data_c[11]['param']['productId'] = product_id
        Log().info("执行用例: " + self.test_data_c[11]['api_name'] + "-->" + self.test_data_c[11]['discriptions'])
        response = HttpRquest().http_request(self.test_data_c[11]['method'], self.test_data_c[11]['url'],
                                             self.test_data_c[11]['param'],
                                             self.test_data_c[11]['header'], cookies=None)

        if response.status_code == 200:
            Log().info("状态码成功返回200".center(66, "-"))
            print('状态码成功返回200'.center(66, "-"))
        else:
            Log().info("状态码返回失败".center(66, "-"))
            print('状态码返回失败'.center(66, "-"))

        result = response.json()
        try:
            assert result['code'] == self.test_data_c[11]['Expect']['code']
            assert result['message'] == self.test_data_c[11]['Expect']['message']


        except AssertionError as e:  # 抛出断言错误异常
            Log().error("评价预期断言结果失败~{0}".format(e))
            print("评价预期断言结果失败")
            raise e
        finally:
            print("请求值：".center(66, "-") + "\n", json.dumps(self.test_data_c[11], ensure_ascii=False, indent=2), "\n")
            print("返回结果：".center(66, "-") + "\n", json.dumps(result, ensure_ascii=False, indent=2))


    def returnproduct(self,order_id,order_no):
        '''C端退货'''

        Log().info("C端用户开始申请退货".center(66, "-"))
        print('C端用户开始申请退货'.center(66, "-"))

        # 替换参数
        self.test_data_c[12]['url'] = self.test_data_c[12]['url'] + str(order_no)
        self.test_data_c[12]['param']['order_id'] = order_id
        Log().info("执行用例: " + self.test_data_c[12]['api_name'] + "-->" + self.test_data_c[12]['discriptions'])
        response = HttpRquest().http_request(self.test_data_c[12]['method'], self.test_data_c[12]['url'],
                                             self.test_data_c[12]['param'],
                                             self.test_data_c[12]['header'], cookies=None)


        if response.status_code == 200:
            Log().info("状态码成功返回200".center(66, "-"))
            print('状态码成功返回200'.center(66, "-"))
        else:
            Log().info("状态码返回失败".center(66, "-"))
            print('状态码返回失败'.center(66, "-"))

        result = response.json()
        try:
            assert result['code'] == self.test_data_c[12]['Expect']['code']
            assert result['message'] == self.test_data_c[12]['Expect']['message']


        except AssertionError as e:  # 抛出断言错误异常
            Log().error("退货预期断言结果失败~{0}".format(e))
            print("退货预期断言结果失败")
            raise e
        finally:
            print("请求值：".center(66, "-") + "\n", json.dumps(self.test_data_c[12], ensure_ascii=False, indent=2), "\n")
            print("返回结果：".center(66, "-") + "\n", json.dumps(result, ensure_ascii=False, indent=2))


    def refuse(self,order_id):
        ''' 拒绝退货'''
        Log().info("C端用户开始申请退货".center(66, "-"))
        print('C端用户开始申请退货'.center(66, "-"))

        # 替换参数
        self.test_data_f[13]['url'] = self.test_data_f[13]['url'] + str(order_id)

        Log().info("执行用例: " + self.test_data_f[13]['api_name'] + "-->" + self.test_data_f[13]['discriptions'])
        response = HttpRquest().http_request(self.test_data_f[13]['method'], self.test_data_f[13]['url'],
                                             self.test_data_f[13]['param'],
                                             self.test_data_f[13]['header'], cookies=self.cookies_f)


        if response.status_code == 200:
            Log().info("状态码成功返回200".center(66, "-"))
            print('状态码成功返回200'.center(66, "-"))
        else:
            Log().info("状态码返回失败".center(66, "-"))
            print('状态码返回失败'.center(66, "-"))

        result = response.json()
        try:
            assert result['code'] == self.test_data_f[13]['Expect']['code']
            assert result['message'] == self.test_data_f[13]['Expect']['message']


        except AssertionError as e:  # 抛出断言错误异常
            Log().error("退货预期断言结果失败~{0}".format(e))
            print("退货预期断言结果失败")
            raise e
        finally:
            print("请求值：".center(66, "-") + "\n", json.dumps(self.test_data_f[13], ensure_ascii=False, indent=2), "\n")
            print("返回结果：".center(66, "-") + "\n", json.dumps(result, ensure_ascii=False, indent=2))


    def category(self,product_id):
        ''' 品类商品查询'''
        Log().info("V端查询三级品类商品".center(66, "-"))
        print('V端查询三级品类商品'.center(66, "-"))

        # self.test_data_v[15]['param']['searchText'] = '%E6%97%B6%E5%B0%9A%E7%BE%8E%E5%A6%860%E6%97%B6%E5%B0%9A%E5%BD%A9%E5%A6%860%E7%94%B7%E5%A3%AB%E9%A6%99%E6%B0%B40'

        Log().info("执行用例: " + self.test_data_v[15]['api_name'] + "-->" + self.test_data_v[15]['discriptions'])
        response = HttpRquest().http_request(self.test_data_v[15]['method'], self.test_data_v[15]['url'],
                                             self.test_data_v[15]['param'],
                                             self.test_data_v[15]['header'], cookies=None)


        if response.status_code == 200:
            Log().info("状态码成功返回200".center(66, "-"))
            print('状态码成功返回200'.center(66, "-"))
        else:
            Log().info("状态码返回失败".center(66, "-"))
            print('状态码返回失败'.center(66, "-"))

        result = response.json()
        try:
            assert result['code'] == self.test_data_v[15]['Expect']['code']
            assert result['message'] == self.test_data_v[15]['Expect']['message']
            assert result['result']['cards'][0]['product_id'] == str(product_id)

        except AssertionError as e:  # 抛出断言错误异常
            Log().error("品类商品断言结果失败~{0}".format(e))
            print("品类商品断言结果失败")
            raise e
        finally:
            print("请求值：".center(66, "-") + "\n", json.dumps(self.test_data_v[15], ensure_ascii=False, indent=2), "\n")
            print("返回结果：".center(66, "-") + "\n", json.dumps(result, ensure_ascii=False, indent=2))


    def repay(self,order_no):
        '''支付回调'''
        headers = {'Content-Type': 'application/json'}
        times = int(time.time()) * 1000
        salt = '2035EB6DD47C4EF69D9F7173EF15D5DF'
        salt = str(order_no) + str(times) + str(salt)
        m = hashlib.md5()
        m.update(salt.encode("utf8"))
        sign = m.hexdigest()
        Log().info("开始支付订单".center(66, "-"))
        print('成功支付订单'.center(66, "-"))
        url = 'http://test-www.intbee.com/public/pay/wxpay/notify'  # 微信支付
        param = {"timestamp": str(times), "sign": sign, "out_trade_no": order_no}
        data = json.dumps(param)
        re_order = requests.post(url=url, data=data, headers=headers)
        if re_order.json()['code'] == 0:
            Log().info("订单支付成功".center(66, "-"))
            print('订单支付成功'.center(66, "-"))
        else:
            Log().info("订单支付失败".center(66, "-"))
            print('订单支付失败'.center(66, "-"))


    def Verificationorderfriend(self,keys):
        '''验证朋友赠送商品'''

        Log().info("开始进入验证商品页面".center(66, "-"))
        print('开始进入验证商品页面'.center(66, "-"))
        self.test_data_wc[17]['header']['app_id'] = '101'
        self.test_data_wc[17]['url'] = self.test_data_wc[17]['url'] + str(keys) + '/verify'

        Log().info("执行用例: " + self.test_data_wc[17]['api_name'] + "-->" + self.test_data_wc[17]['discriptions'])
        response = HttpRquest().http_request(self.test_data_wc[17]['method'], self.test_data_wc[17]['url'],
                                             self.test_data_wc[17]['param'],
                                             self.test_data_wc[17]['header'], cookies=self.Authorization['cookies'])

        if response.status_code == 200:
            Log().info("进入验证商品页面成功".center(66, "-"))
            print('进入验证商品页面成功'.center(66, "-"))
        else:
            Log().info("进入验证商品页面失败".center(66, "-"))
            print('进入验证商品页面失败'.center(66, "-"))

        result = response.json()
        try:
            assert result['code'] == self.test_data_wc[17]['Expect']['code']
            assert result['message'] == self.test_data_wc[17]['Expect']['message']

        except AssertionError as e:  # 抛出断言错误异常
            Log().error("进入验证商品页面失败~{0}".format(e))
            print("进入验证商品页面失败")
            raise e
        finally:
            print("请求值：".center(66, "-") + "\n", json.dumps(self.test_data_wc[17], ensure_ascii=False, indent=2), "\n")
            print("返回结果：".center(66, "-") + "\n", json.dumps(result, ensure_ascii=False, indent=2))

        return result

    def getorderfriend(self,keys):
        '''验证朋友赠送商品'''

        Log().info("开始进入接受商品页面".center(66, "-"))
        print('开始进入接受商品页面'.center(66, "-"))
        self.test_data_wc[18]['header']['app_id'] = '101'
        self.test_data_wc[18]['url'] = self.test_data_wc[18]['url'] + str(keys) + '/address'

        Log().info("执行用例: " + self.test_data_wc[18]['api_name'] + "-->" + self.test_data_wc[18]['discriptions'])
        response = HttpRquest().http_request(self.test_data_wc[18]['method'], self.test_data_wc[18]['url'],
                                             self.test_data_wc[18]['param'],
                                             self.test_data_wc[18]['header'], cookies=self.Authorization['cookies'])

        if response.status_code == 200:
            Log().info("进入接受商品页面成功".center(66, "-"))
            print('进入接受商品页面成功'.center(66, "-"))
        else:
            Log().info("进入接受商品页面失败".center(66, "-"))
            print('进入接受商品页面失败'.center(66, "-"))

        result = response.json()
        try:
            assert result['code'] == self.test_data_wc[18]['Expect']['code']
            assert result['message'] == self.test_data_wc[18]['Expect']['message']

        except AssertionError as e:  # 抛出断言错误异常
            Log().error("进入接受商品页面失败~{0}".format(e))
            print("进入接受商品页面失败")
            raise e
        finally:
            print("请求值：".center(66, "-") + "\n", json.dumps(self.test_data_wc[18], ensure_ascii=False, indent=2), "\n")
            print("返回结果：".center(66, "-") + "\n", json.dumps(result, ensure_ascii=False, indent=2))

        return result

# Procedure().searchrorder("101154150240745906","cancelld")
# Procedure().repay("101154682886537154")
# Procedure().deliver(79954)
# Procedure().orderconfirm(79949)
# Procedure().wxpay(79957,101154157807745928)
# Procedure().applyrefund(79926,101154147052845897)
# Procedure().batch(18626)
# Procedure().returnproduct(79989,"101154158592945960")
# Procedure().refuse("80024")
# Procedure().createproduct()
# Procedure().intbeecardacception(15095)

# Procedure().intbeecardacception(15126)
# print(Procedure().intbeecard_creation2(18939))

