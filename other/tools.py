import time
from common.httprequest import HttpRquest
from mysql.my import Pydb,Mongodb
from common.readyaml import read_yaml
from conf import read_path,config
from common.readyaml import update_yaml
from apiObject.setupApi import SetupApi
from mysql.pymysql_db import Connectmysql
import time
from common import changetime,save_value

class Tool(object):
    def __init__(self,token_f=None,token_c=None,token_v=None):

        self.http = HttpRquest()
        self.dir = read_path.tooldata
        self.url = config.url
        #
        # if token_f != None:
        #     self.token_f = token_f
        # elif save_value.SaveValue.TOKEN == None:
        #     res_f = SetupApi().login_f()
        #     self.token_f = res_f['access_token']
        #     self.uuid_f = res_f['uuid']
        # else:
        #     self.token_f = save_value.SaveValue.TOKEN
        #     self.uuid_f = save_value.SaveValue.F_UUID
        #
        # if token_c != None:
        #     self.token_c = token_c
        # elif save_value.SaveValue.TOKEN_C == None:
        #     res_c = SetupApi().login_c()
        #     self.token_c = res_c['access_token']
        #     self.uuid_c = res_c['uuid']
        # else:
        #     self.token_c = save_value.SaveValue.TOKEN_C
        #     self.uuid_c = save_value.SaveValue.C_UUID
        #
        # if token_v != None:
        #     self.token_v = token_v
        # elif save_value.SaveValue.TOKEN_V == None:
        #     res_v = SetupApi().login_v()
        #     self.token_v = res_v['access_token']
        #     self.uuid_v = res_v['uuid']
        # else:
        #     self.token_v = save_value.SaveValue.TOKEN_V
        #     self.uuid_v = save_value.SaveValue.V_UUID


        if save_value.SaveValue.TOKEN == None and save_value.SaveValue.C_UUID == None and save_value.SaveValue.V_UUID == None:

            res_f = SetupApi().login_f()
            self.token_f = res_f['access_token']
            self.uuid_f = res_f['uuid']

            res_c = SetupApi().login_c()
            self.token_c = res_c['access_token']
            self.uuid_c = res_c['uuid']

            res_v = SetupApi().login_v()
            self.token_v = res_v['access_token']
            self.uuid_v = res_v['uuid']

        else:
            self.token = save_value.SaveValue.TOKEN

            self.token_f = save_value.SaveValue.TOKEN
            self.uuid_f = save_value.SaveValue.F_UUID

            self.token_c = save_value.SaveValue.TOKEN_C
            self.uuid_c = save_value.SaveValue.C_UUID

            self.token_v = save_value.SaveValue.TOKEN_V
            self.uuid_v = save_value.SaveValue.V_UUID


        self.data = read_yaml(self.dir, 'tooldata.yaml', self.url, token=self.token_f)

    @property
    def create_product(self):
        """
        创建商品
        :return:
            code : 0
            message: 'success
            result: product_id
        """
        name = update_yaml(read_path.commondata, "data.yaml", 'num')
        self.data[0]['param']['product_name'] = self.data[0]['param']['product_name'] + str(name)
        response = self.http.http_request(self.data[0]['method'], self.data[0]['url'],
                                          self.data[0]['param'],
                                          self.data[0]['header'], cookies=None)
        print(self.data[0]['param'])
        print(self.data[0]['url'])
        result = response.json()
        print("商品创建成功：---------------",result)
        return result


    @property
    def product_no_postage(self):
        '''创建免邮商品'''
        response = self.http.http_request(self.data[1]['method'], self.url,
                                          self.data[1]['param'],
                                          self.data[1]['header'], cookies=None)
        result = response.json()
        return result

    @property
    def create_card(self):
        """
            发布普通蜂卡
            return :response、product_id、 card_id
        """
        self.data[2]['param']['product_id'] = self.create_product['result']

        name = update_yaml(read_path.commondata, "data.yaml", 'num')
        self.data[2]['param']['task_info']['task_name'] = self.data[2]['param']['task_info']['task_name'] + str(name)

        response = self.http.http_request(self.data[2]['method'], self.data[2]['url'],
                                          self.data[2]['param'],
                                          self.data[2]['header'], cookies=None)
        print(self.data[2])
        result = response.json()
        print("普通蜂卡发布成功:------------------",result)
        import time
        time.sleep(1)
        con = Connectmysql("intbee")
        sql = 'SELECT * FROM intbee_task_info WHERE product_id= %s;'
        params = [self.data[2]['param']['product_id']]
        data = con.fetchone(sql,params)
        print(data)
        return result,self.data[2]['param']['product_id'],data['id']




    def create_card2(self):
        '''发布定向蜂卡'''

        self.data[3]['param']['product_id'] = self.create_product['result']
        self.data[3]['param']['uuids'] = [self.uuid_v]
        print(self.data[3])
        response = self.http.http_request(self.data[3]['method'], self.data[3]['url'],
                                          self.data[3]['param'],
                                          self.data[3]['header'], cookies=None)
        result = response.json()

        import time
        time.sleep(1)
        con = Connectmysql("intbee")
        sql = 'SELECT * FROM intbee_task_info WHERE product_id= %s;'
        params = [self.data[3]['param']['product_id']]
        data = con.fetchone(sql, params)

        return data['id']

    @property
    def create_card3(self):
        '''发布蜂团蜂卡'''
        self.data[4]['param']['product_id'] = self.create_product['result']
        response = self.http.http_request(self.data[4]['method'], self.data[4]['url'],
                                          self.data[4]['param'],
                                          self.data[4]['header'], cookies=None)
        print(self.data[4]['param'])
        result = response.json()
        return result

    @property
    def create_card4(self):
        '''发布拼团蜂卡'''
        # self.data[5]['param']['product_id'] = self.product_no_postage['result']['result']
        response = self.http.http_request(self.data[5]['method'], self.url,
                                          self.data[5]['param'],
                                          self.data[5]['header'], cookies=None)
        result = response.json()
        return result

    @property
    def accept_card(self):
        """
        :return: product_id,card_id,sucard_id
        # """
        self.card = self.create_card
        data = self.card
        time.sleep(2)
        # self.data[6]['url'] = self.data[6]['url'] + "/"+ str(data[2])+ '/accept'
        # self.data[6]['header']['access_token'] = self.token_v
        # response = self.http.http_request(self.data[6]['method'],  self.data[6]['url'],
        #                                   self.data[6]['param'],
        #                                   self.data[6]['header'], cookies=None)

        self.data[26]['header']['access_token'] = self.token_v
        self.data[26]['url'] = self.data[26]['url'] + str(data[2])
        response = self.http.http_request(self.data[26]['method'], self.data[26]['url'],
                                          self.data[26]['param'],
                                          self.data[26]['header'], cookies=None)

        con = Connectmysql("intbee")
        sql = 'SELECT * FROM intbee_subcard WHERE card_id= %s;'
        params = [data[2]]
        re = con.fetchone(sql, params)
        result = response.json()
        print(self.data[26])
        print("成功申请普通蜂卡-----------------",result)
        return data[1],data[2],re['id']


    @property
    def confirm(self,**kwargs):
        '''下单不使用优惠券'''
        if kwargs:
            self.data[7]['param']['product_id'] = kwargs['product_id']
            self.data[7]['param']['sku_list'][0]['sku'] = str(kwargs['product_id']) + '_1'
            self.data[7]['header']['access_token'] = self.token_c
            self.data[7]['header']['param']['spreader_uuid'] = self.uuid_v
            self.data[7]['param']['subcard_id'] = kwargs['card_id']
            self.data[7]['param']['card_id'] = kwargs['subcard_id']
            self.data[7]['param']['address_id'] = Tool().createaddress
        else:
            re = self.accept_card
            self.data[7]['param']['product_id'] = re[0]
            self.data[7]['param']['sku_list'][0]['sku'] = str(re[0]) + '_1'
            self.data[7]['header']['access_token'] = self.token_c
            self.data[7]['param']['spreader_uuid'] = self.uuid_v
            self.data[7]['param']['subcard_id'] = re[2]
            self.data[7]['param']['card_id'] = re[1]
            self.data[7]['param']['address_id'] = Tool().createaddress
        response = self.http.http_request(self.data[7]['method'], self.data[7]['url'],
                                          self.data[7]['param'],
                                          self.data[7]['header'], cookies=None)
        print(self.data[7])
        result = response.json()
        print("成功下单---------------------",result)

        return result


    def confirm2(self,**kwargs):
        '''下单不使用优惠券'''
        if kwargs:
            self.data[7]['param']['product_id'] = kwargs['product_id']
            self.data[7]['param']['sku_list'][0]['sku'] = str(kwargs['product_id']) + '_1'
            self.data[7]['header']['access_token'] = self.token_c
            self.data[7]['param']['spreader_uuid'] = self.uuid_v
            self.data[7]['param']['subcard_id'] = kwargs['card_id']
            self.data[7]['param']['card_id'] = kwargs['subcard_id']
            self.data[7]['param']['address_id'] = Tool().createaddress
        else:
            re = self.accept_card
            p_id = re[0]
            self.data[7]['param']['product_id'] = p_id
            self.data[7]['param']['sku_list'][0]['sku'] = str(p_id) + '_1'
            self.data[7]['header']['access_token'] = self.token_c
            self.data[7]['param']['spreader_uuid'] = self.uuid_v
            self.data[7]['param']['subcard_id'] = re[2]
            self.data[7]['param']['card_id'] = re[1]
            self.data[7]['param']['address_id'] = Tool().createaddress

        response = self.http.http_request(self.data[7]['method'], self.data[7]['url'],
                                          self.data[7]['param'],
                                          self.data[7]['header'], cookies=None)
        print(self.data[7])
        result = response.json()
        print("成功下单---------------------",result)

        return result



    def confirm_freind(self,**kwargs):
        '''送好友订单'''
        if kwargs:
            self.data[15]['param']['product_id'] = kwargs['product_id']
            self.data[15]['param']['sku_list'][0]['sku'] = str(kwargs['product_id']) + '_1'
            self.data[15]['param']['subcard_id'] = kwargs['card_id']
            self.data[15]['param']['card_id'] = kwargs['subcard_id']
            self.data[15]['param']['spreader_uuid'] = self.uuid_v
            self.data[15]['header']['access_token'] = self.token_c
            self.data[7]['param']['address_id'] = Tool().createaddress
        else:
            re = self.accept_card
            self.data[15]['param']['product_id'] = re[0]
            self.data[15]['param']['sku_list'][0]['sku'] = str(re[0]) + '_1'
            self.data[15]['param']['subcard_id'] = re[2]
            self.data[15]['param']['card_id'] = re[1]
            self.data[7]['param']['address_id'] = Tool().createaddress

            self.data[15]['param']['spreader_uuid'] = self.uuid_v
            self.data[15]['header']['access_token'] = self.token_c
        response = self.http.http_request(self.data[15]['method'], self.data[15]['url'],
                                          self.data[15]['param'],
                                          self.data[15]['header'], cookies=None)
        print(self.data[15])
        result = response.json()
        print("成功下单---------------------",result)

        return result

    #fapi/activity/coupon
    @property
    def createcoupone(self):
        """
        创建店铺优惠券（无金额限制）
        :return: coupon_id
        """

        response = self.http.http_request(self.data[8]['method'], self.data[8]['url'],
                                          self.data[8]['param'],
                                          self.data[8]['header'], cookies=None)


        result = response.json()
        print("成功创建优惠券---------------------", result)


        con = Connectmysql("intbee")
        sql = 'SELECT * FROM intbee_activity_coupon WHERE corporate_uuid="5b2a1535b0bcdf00088d7cea" ORDER BY id DESC limit 1;'
        data = con.fetchone(sql)
        return  data['id']


    #fapi/postage
    @property
    def createpostage(self):
        '''创建运费模板'''
        self.data[9]['param']['shop_info']['shop_id'] = save_value.SaveValue.F_UUID
        response = self.http.http_request(self.data[9]['method'], self.data[9]['url'],
                                          self.data[9]['param'],
                                          self.data[9]['header'], cookies=None)

        result = response.json()
        print("成功创建运费模板---------------------", result)

        d = Mongodb("opensku")
        client = d.get_mongodb_client()
        db = client.opensku
        time.sleep(2)
        collection = db.opensku_postage
        results = collection.find({"shop_info.shop_id": save_value.SaveValue.F_UUID}).sort("_id", -1)
        a = results[0]
        d.close()
        print("成功创建规格---------------------", result)
        return a['_id']



    @property
    def createaddress(self):
        '''创建地址'''
        self.data[11]['header']['access_token'] = self.token_c
        # self.data[5]['param']['product_id'] = self.product_no_postage['result']['result']
        response = self.http.http_request(self.data[11]['method'],  self.data[11]['url'],
                                          self.data[11]['param'],
                                          self.data[11]['header'], cookies=None)
        # print(self.data[11])
        result = response.json()
        return result['result']['id']

    @property
    def card_v(self):
        '''发布定向卡'''
        product_id = self.create_product['result']
        result = self.create_card2(product_id)
        return result

    @property
    def createinventory(self):
        '''创建清单'''
        self.data[12]['header']['access_token'] = self.token_v
        response = self.http.http_request(self.data[12]['method'],  self.data[12]['url'],
                                          self.data[12]['param'],
                                          self.data[12]['header'], cookies=None)
        result = response.json()
        return result['result']['inventory_id']
    @property
    def createstandard(self):
        response = self.http.http_request(self.data[10]['method'], self.data[10]['url'],
                                          self.data[10]['param'],
                                          self.data[10]['header'], cookies=None)
        result = response.json()
        print(result)
        d = Mongodb("opensku")
        client = d.get_mongodb_client()
        db = client.opensku
        time.sleep(2)
        collection = db.opensku_standard
        results= collection.find({"shop_info.shop_id": save_value.SaveValue.F_UUID}).sort("_id", -1)
        a = results[0]
        d.close()
        print("成功创建规格---------------------", result)
        return a['_id']


    #/public/order/pay/notify/{order_no}/{channel}/{merchant_no}
    def notify(self,**kwargs):
        '''模拟支付回调'''

        self.data[13]['header']['access_token'] = self.token_c
        if kwargs:
            self.data[13]['url'] =  self.data[13]['url'] + str(kwargs['order_no']) + '/wx/1367026602' + '?sign=intbee-order-notify-b1c7bc32-4b7a-11e9-8646-d663bd873d93'
            self.order_no = kwargs['order_no']
        else:
            self.order_no = self.confirm2()['result']['order_no']
            self.data[13]['url'] = self.data[13]['url'] + str(self.order_no) + '/wx/1367026602' + '?sign=intbee-order-notify-b1c7bc32-4b7a-11e9-8646-d663bd873d93'
        response = self.http.http_request(self.data[13]['method'], self.data[13]['url'],
                                          self.data[13]['param'],
                                             self.data[13]['header'], cookies=None)

        print(self.data[13])

        result = response.json()
        print(result)

        print("支付成功---------------------", result)
        return result,self.order_no


    def delivery(self,**kwargs):
        '''发货'''
        carrier_no = str(round(time.time()))
        self.data[14]['param']['carrier_no'] = carrier_no

        if kwargs:
            self.data[14]['url'] = self.data[14]['url'] + kwargs['order_no']
            self.order_no = kwargs['order_no']
        else:
            self.order_no = self.notify()[1]
            self.data[14]['url'] = self.data[14]['url'] + str(self.order_no)
        response = self.http.http_request(self.data[14]['method'], self.data[14]['url'],
                                          self.data[14]['param'],
                                          self.data[14]['header'], cookies=None)
        result = response.json()

        return result,self.order_no

    def completed(self):
        '''确认收货'''
        self.order_no = self.delivery()[1]
        self.data[16]['header']['access_token'] = self.token_c
        self.data[16]['url'] =  self.data[16]['url'] + str(self.order_no)
        response = self.http.http_request(self.data[16]['method'], self.data[16]['url'],
                                          self.data[16]['param'],
                                          self.data[16]['header'], cookies=None)

        result = response.json()

        return result,self.order_no

    def audit(self):
        """
        修改结算时间
        :return: self.order_no 订单号
        """
        self.order_no = self.completed()[1]
        import datetime
        utime =(datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d %H:%M:%S")
        con = Connectmysql("intbee")
        sql =  'UPDATE intbee_sell_history set settle_time=str_to_date(%s,"%%Y-%%m-%%d %%H:%%i:%%S") WHERE order_no=%s;'
        params = [utime, str(self.order_no)]
        count = con.update(sql,params)
        if count:
            print('操作成功.')
        else:  # None,False,0
            print('操作失败')
        return self.order_no


    def create_card_ce(self):
        """
        创建测品蜂卡
        :return: card_id
        """
        self.data[17]['param']['product_id'] = self.create_product['result']
        response = self.http.http_request(self.data[17]['method'], self.data[17]['url'],
                                          self.data[17]['param'],
                                          self.data[17]['header'], cookies=None)
        print(self.data[17])
        result = response.json()
        print("成功创建测品蜂卡:------------------",result)
        con = Connectmysql("intbee")
        sql = 'SELECT * FROM intbee_card WHERE product_id= %s;'
        params = [self.data[17]['param']['product_id']]
        data = con.fetchone(sql, params)
        return result,self.data[17]['param']['product_id'],data['id']


    def distribution_addproduct(self):
        re = self.create_card
        product_id = re[1]
        card_id = re[2]
        self.data[18]['param']['sale_products'][0]['product_id'] = product_id
        self.data[18]['param']['sale_products'][0]['card_id'] = card_id
        self.data[18]['header']['access_token'] = self.token_FEN
        response = self.http.http_request(self.data[18]['method'], self.data[18]['url'],
                                          self.data[18]['param'],
                                          self.data[18]['header'], cookies=None)
        print( self.data[18]['param'])
        return response.json(),re[1],re[2]



    def distribution_createorder(self):
        re = self.distribution_addproduct()
        product_id = re[1]
        sku = str(re[1]) + '_1'
        self.data[19]['param']['product_id'] = product_id
        self.data[19]['param']['sku_list'][0]['sku'] = sku
        self.data[19]['header']['access_token'] = self.token_FEN
        response = self.http.http_request(self.data[19]['method'], self.data[19]['url'],
                                                  self.data[19]['param'],
                                                  self.data[19]['header'], cookies=None)
        # print(self.data[18]['param'])
        return response.json()

    def distribution_pay(self):
        re = self.distribution_createorder()
        order_no = re['result']['order_no']
        self.data[20]['url'] =  self.data[20]['url'] + str(order_no) + '/pay'
        self.data[20]['header']['access_token'] = self.token_FEN
        print(self.data[20]['url'])
        response = self.http.http_request(self.data[20]['method'], self.data[20]['url'],
                                          self.data[20]['param'],
                                          self.data[20]['header'], cookies=None)

        return response.json(),order_no


    def create_task(self,**kwargs):
        """
        创建纯cps任务
        :return: product_id ,card_id
        """
        card_end_time = changetime.getnow()
        self.data[21]['param']['task_end_time'] = card_end_time
        if kwargs:
            self.data[21]['param']['product_id'] = kwargs['product_id']
        else:
            self.data[21]['param']['product_id'] = self.create_product['result']

        name = update_yaml(read_path.commondata, "data.yaml", 'num')
        self.data[21]['param']['task_info']['task_name'] = self.data[21]['param']['task_info']['task_name'] + str(name)

        response = self.http.http_request(self.data[21]['method'], self.data[21]['url'],
                                          self.data[21]['param'],
                                          self.data[21]['header'], cookies=None)
        result = response.json()

        print("创建任务",result)
        import time
        time.sleep(1)
        con = Connectmysql("intbee")
        sql = 'SELECT * FROM intbee_task_info WHERE product_id={0};'.format(self.data[21]['param']['product_id'])

        data = con.fetchone(sql)
        return self.data[21]['param']['product_id'],data['id']


    def create_cpm(self,**kwargs):
        """
        创建任务，含cpm
        :return:
        """
        card_end_time = changetime.gettime(2)
        self.data[22]['param']['task_end_time'] = card_end_time
        if kwargs:
            self.data[22]['param']['product_id'] = kwargs['product_id']
        else:
            self.data[22]['param']['product_id'] = self.create_product['result']

        name = update_yaml(read_path.commondata, "data.yaml", 'num')
        self.data[22]['param']['task_info']['task_name'] = self.data[22]['param']['task_info']['task_name'] + str(name)

        response = self.http.http_request(self.data[22]['method'], self.data[22]['url'],
                                          self.data[22]['param'],
                                          self.data[22]['header'], cookies=None)
        result = response.json()
        print(self.data[22])
        print("创建cpm任务:------------------", result)
        import time
        time.sleep(1)
        con = Connectmysql("intbee")
        sql = 'SELECT * FROM intbee_task_info WHERE product_id= %s;'
        params = [self.data[22]['param']['product_id']]
        data = con.fetchone(sql, params)
        return self.data[22]['param']['product_id'],data['id']


    def create_ce(self,**kwargs):
        """
        创建任务，含测品+测品+cpm
        :return:
        """
        card_end_time = changetime.gettime(2)
        self.data[23]['param']['task_end_time'] = card_end_time
        if kwargs:
            self.data[23]['param']['product_id'] = kwargs['product_id']
        else:
            self.data[23]['param']['product_id'] = self.create_product['result']

        name = update_yaml(read_path.commondata, "data.yaml", 'num')
        self.data[23]['param']['task_info']['task_name'] = self.data[23]['param']['task_info']['task_name'] + str(name)

        response = self.http.http_request(self.data[23]['method'], self.data[23]['url'],
                                          self.data[23]['param'],
                                          self.data[23]['header'], cookies=None)
        result = response.json()
        import time
        time.sleep(1)
        con = Connectmysql("intbee")
        sql = 'SELECT * FROM intbee_task_info WHERE product_id= %s;'
        params = [self.data[23]['param']['product_id']]

        data = con.fetchone(sql, params)
        return self.data[23]['param']['product_id'], data['id']



    def review(self,type=3,**kwargs):
        """
        父任务审核
        :param kwargs:
        type: 1 纯cpm  2、纯cpp 3、cpp+cpm
        :return:
        """
        if kwargs:
            self.data[24]['param']['card_id'] = kwargs['task_id']
        else:
            if type == 1:
                self.data[24]['param']['card_id'] = self.create_cpm()[1]    #self.create_ce()[1]
            if type == 2:
                self.data[24]['param']['card_id'] = self.create_zce()[1]
            if type == 3:
                self.data[24]['param']['card_id'] = self.create_ce()[1]
        response = self.http.http_request(self.data[24]['method'], self.data[24]['url'],
                                          self.data[24]['param'],
                                          self.data[24]['header'], cookies=None)
        result = response.json()

        print("父任务审核",result)
        time.sleep(2)
        con = Connectmysql("intbee")
        sql = 'SELECT * FROM intbee_activity_deposit_order WHERE card_id=%s;'
        params = [self.data[24]['param']['card_id']]
        data = con.fetchone(sql, params)

        return self.data[24]['param']['card_id'],data['order_no']


    def task_pay(self,type=3,**kwargs):
        """
        余额支付
        :param kwargs:
        :return:
        """
        if kwargs:
            self.data[25]['param']['order_no'] = kwargs['order_no']
        else:
            self.data[25]['param']['order_no'] = self.review(type)[1]
        response = self.http.http_request(self.data[25]['method'], self.data[25]['url'],
                                          self.data[25]['param'],
                                          self.data[25]['header'], cookies=None)
        result = response.json()

        print("余额支付",result)
        return self.data[24]['param']['card_id']

    def accept_task(self,type=3,**kwargs):
        """
        :return: product_id,card_id
        # """

        self.data[6]['header']['access_token'] = self.token_v
        if kwargs:
            self.data[6]['url'] = self.data[6]['url'] + "/" + str(kwargs['task_id']) + '/accept'
            self.task_id = kwargs['task_id']
        else:
            self.task_id = self.task_pay(type)

            self.data[6]['url'] = self.data[6]['url'] + "/" + str(self.task_id) + '/accept'

        response = self.http.http_request(self.data[6]['method'], self.data[6]['url'],
                                          self.data[6]['param'],
                                          self.data[6]['header'], cookies=None)
        result = response.json()
        print(self.data[6]['url'])
        print("成功上架商品-----------------", result)
        return self.task_id


    def task_apply(self,type=3,**kwargs):
        """
        申请任务
        :param task_id:
        :return:
        """
        self.data[26]['header']['access_token'] = self.token_v
        if kwargs:
            self.data[26]['url'] = self.data[26]['url'] + str(kwargs['task_id'])
            self.task_id = kwargs['task_id']
        else:
            self.task_id = self.task_pay(type)
            self.data[26]['url'] = self.data[26]['url'] + str(self.task_id)
        response = self.http.http_request(self.data[26]['method'], self.data[26]['url'],
                                          self.data[26]['param'],
                                          self.data[26]['header'], cookies=None)
        print(self.data[26])
        result = response.json()
        print("申请任务:------------------", result)
        return self.task_id




    def task_subaudit(self,type=3,**kwargs):
        """
        子任务审核
        :param task_id:
        :return:
        """
        if kwargs:
            task_id = kwargs['task_id']
            self.data[27]['param']['card_id'] = kwargs['task_id']
            self.data[27]['param']['spread_uuid'] = self.uuid_v
        else:
            task_id = self.task_apply(type)
            self.data[27]['param']['card_id'] = task_id
            self.data[27]['param']['spread_uuid'] = self.uuid_v
        response = self.http.http_request(self.data[27]['method'], self.data[27]['url'],
                                          self.data[27]['param'],
                                          self.data[27]['header'], cookies=None)
        print(self.data[27])
        result = response.json()
        print("子任务审核:------------------", result)
        return task_id


    def task_ceaddress(self, type=3,**kwargs):
        """
        填写测品地址
        :param task_id:
        :return:
        """
        self.data[28]['header']['access_token'] = self.token_v
        if kwargs:
            task_id = kwargs['task_id']
            self.data[28]['url'] =self.data[28]['url'] + str(kwargs['task_id'])
        else:
            task_id = self.task_subaudit(type)
            self.data[28]['url'] = self.data[28]['url'] + str(task_id)
        response = self.http.http_request(self.data[28]['method'], self.data[28]['url'],
                                          self.data[28]['param'],
                                          self.data[28]['header'], cookies=None)
        print(self.data[28])
        result = response.json()
        print("填写测品地址:------------------", result)
        return task_id


    def task_carrier(self,type=3,**kwargs):
        """
        测品发货
        :return:
        """
        carrier_no = str(round(time.time()))
        if kwargs:
            task_id = kwargs['task_id']
            self.data[29]['url'] = self.data[29]['url'] + str(task_id) + '/' + self.uuid_v
            self.data[29]['param']['carrier_no'] = carrier_no
        else:
            task_id = self.task_ceaddress(type)
            self.data[29]['url'] = self.data[29]['url'] + str(task_id) + '/' + self.uuid_v
            self.data[29]['param']['carrier_no'] = carrier_no
        response = self.http.http_request(self.data[29]['method'], self.data[29]['url'],
                                          self.data[29]['param'],
                                          self.data[29]['header'], cookies=None)
        result = response.json()

        print("填写发货地址:------------------", result)
        return task_id


    def task_getcarrier(self,type=3,**kwargs):
        """
        V测品确认收货
        :return:
        """
        self.data[30]['header']['access_token'] = self.token_v
        if kwargs:
            task_id = kwargs['task_id']
            self.data[30]['url'] = self.data[30]['url'] + str(task_id)

        else:
            task_id = self.task_carrier(type)
            self.data[30]['url'] = self.data[30]['url'] + str(task_id)
        response = self.http.http_request(self.data[30]['method'], self.data[30]['url'],
                                          self.data[30]['param'],
                                          self.data[30]['header'], cookies=None)
        result = response.json()
        print("确认收货===:",result)
        return task_id


    def task_addurl(self,type=3,**kwargs):
        """
        V端填写开团地址
        :return:
        """
        self.data[31]['header']['access_token'] = self.token_v
        if kwargs:
            task_id = kwargs['task_id']
            self.data[31]['url'] = self.data[31]['url'] + str(task_id)

        else:
            if type == 1:
                task_id = self.task_subaudit(type)
            else:
                task_id = self.task_getcarrier(type)
            self.data[31]['url'] = self.data[31]['url'] + str(task_id)
        response = self.http.http_request(self.data[31]['method'], self.data[31]['url'],
                                          self.data[31]['param'],
                                          self.data[31]['header'], cookies=None)
        result = response.json()
        print("填写开团地址===:", result)

        time.sleep(2)
        con = Connectmysql("intbee")
        sql = 'SELECT * FROM intbee_task_info WHERE id=%s;'
        params = [task_id]
        data = con.fetchone(sql, params)
        return task_id,data['task_no']




    def create_activity(self):
        """
        创建活动
        :param check:
        :param kwargs:
        :return:
        """

        start = changetime.getnow()
        self.data[33]['param']['activity_start_time'] = start
        activity_end_time = changetime.gettime(2)
        self.data[33]['param']['activity_end_time'] = activity_end_time
        self.data[33]['param']['apply_end_time'] = activity_end_time


        response = self.http.http_request(self.data[33]['method'], self.data[33]['url'],
                                          self.data[33]['param'],
                                          self.data[33]['header'], cookies=None)
        result = response.json()
        print(result)

        con = Connectmysql("intbee")
        sql = 'SELECT * from intbee_activity_market ORDER BY id DESC limit 1;'

        data = con.fetchone(sql)
        return data['id']


    def create_zce(self,**kwargs):
        """
        创建任务，只含测品含活动
        :return:
        """
        activity_id = self.create_activity()
        card_end_time = changetime.gettime(1)
        self.data[35]['param']['task_end_time'] = card_end_time
        if kwargs:
            self.data[35]['param']['product_id'] = kwargs['product_id']
        else:
            self.data[35]['param']['product_id'] = self.create_product['result']
            self.data[35]['param']['market_activity_id'] = activity_id

        name = update_yaml(read_path.commondata, "data.yaml", 'num')
        self.data[35]['param']['task_info']['task_name'] = self.data[35]['param']['task_info']['task_name'] + str(name)

        response = self.http.http_request(self.data[35]['method'], self.data[35]['url'],
                                          self.data[35]['param'],
                                          self.data[35]['header'], cookies=None)
        result = response.json()
        import time
        time.sleep(1)
        con = Connectmysql("intbee")
        sql = 'SELECT * FROM intbee_task_info WHERE product_id= %s;'
        params = [self.data[35]['param']['product_id']]
        data = con.fetchone(sql, params)
        return self.data[35]['param']['product_id'], data['id']

    def task_check(self,type=3,**kwargs):
        """
         待结算标记
        :return:
        """

        if kwargs:
            self.data[36]['param']['parent_card_no'] = kwargs['parent_card_no']
            task_id = 0
        else:
            re = self.task_addurl(type)
            task_id = re[0]
            self.data[36]['param']['parent_card_no'] = re[1]
        if type == 3:
            self.data[36]['param']['type'] = '8,9'
        if type == 1:
            self.data[36]['param']['type'] = '9'
        if type == 2:
            self.data[36]['param']['type'] = '8'
        self.data[36]['param']['spread_uuid'] = self.uuid_v


        response = self.http.http_request(self.data[36]['method'], self.data[36]['url'],
                                          self.data[36]['param'],
                                          self.data[36]['header'], cookies=None)

        result = response.json()
        print(self.data[36])
        print("结算验收",result)
        return task_id,self.data[36]['param']['parent_card_no']

    def applystop(self,**kwargs):
        """
        申请终止任务
        :param kwargs:
        :return:
        """
        if kwargs:
            task_id = kwargs['task_id']
            self.data[37]['url'] =  self.data[37]['url'] + str(task_id)
        else:
            task_id = self.task_check()[0]
            self.data[37]['url'] = self.data[37]['url'] + str(task_id)

        response = self.http.http_request(self.data[37]['method'], self.data[37]['url'],
                                          self.data[37]['param'],
                                          self.data[37]['header'], cookies=None)
        result = response.json()

        return task_id

    def stopcard(self,**kwargs):
        """
        确认终止
        :param kwargs:
        :return:
        """

        if kwargs:
            task_id = kwargs['task_id']
            self.data[38]['url'] = self.data[38]['url'] + str(task_id)
        else:
            task_id = self.applystop()
            self.data[38]['url'] = self.data[38]['url'] + str(task_id)

        response = self.http.http_request(self.data[38]['method'], self.data[38]['url'],
                                          self.data[38]['param'],
                                          self.data[38]['header'], cookies=None)
        result = response.json()
        print(task_id)
        return result

    def putCanSettleOrderToAuditJodHandle(self):
        """
        执行定时器，将可结算的订单写进任务结算审核表
        :return:
        """

        response = self.http.http_request(self.data[39]['method'], self.data[39]['url'],
                                          self.data[39]['param'],
                                          self.data[39]['header'], cookies=None)
        result = response.json()

        return result


    def applyreturn(self):
        """
        申请退货
        :return:
        """
        order_no = Tool().delivery()[1]
        self.data[40]['header']['access_token'] = self.token_c
        self.data[40]['param']['order_no'] =  order_no
        self.data[40]['param']['carrier_no'] = str(round(time.time()))
        response = self.http.http_request(self.data[40]['method'], self.data[40]['url'],
                                          self.data[40]['param'],
                                          self.data[40]['header'], cookies=None)
        result = response.json()

        return order_no


    def create_baotask(self):
        """
        创建非商品任务
        :return:
        """
        name = update_yaml(read_path.commondata, "data.yaml", 'num')
        self.data[41]['param']['task_info']['task_name'] = self.data[41]['param']['task_info']['task_name'] + str(name)
        response = self.http.http_request(self.data[41]['method'], self.data[41]['url'],
                                          self.data[41]['param'],
                                          self.data[41]['header'], cookies=None)

        name = update_yaml(read_path.commondata, "data.yaml", 'num')
        self.data[41]['param']['task_info']['task_name'] = self.data[41]['param']['task_info']['task_name'] + str(name)

        result = response.json()
        import time
        time.sleep(1)
        con = Connectmysql("intbee")
        sql = 'select * from intbee_task_info where manufacture_uuid="%s" order by id DESC ;'%SaveValue.F_UUID
        data = con.fetchone(sql)
        return data['id']



    def taskSetSettleJodHandle(self):
        """
        执行定时器，将终止或已结束的任务设置为可结算
        :return:
        """

        response = self.http.http_request(self.data[42]['method'], self.data[42]['url'],
                                          self.data[42]['param'],
                                          self.data[42]['header'], cookies=None)
        result = response.json()

        return result

    def taskAudit(self,type=3,**kwargs):
        """
        任务结算财务审核
        :return:
        """

        re = self.task_check(type=type)
        parent_card_no = re[1]
        self.data[43]['param'][0]['card_no'] = parent_card_no
        con = Connectmysql("intbee")
        sql = 'SELECT * FROM intbee_activity_deposit_order_audit WHERE card_no="%s";' % (parent_card_no)
        data = con.fetchone(sql)

        self.data[43]['param'][0]['cpm_receivable_sell'] = float(str(data['cpm_receivable_sell']))
        self.data[43]['param'][0]['cpp_receivable_sell'] = float(str(data['cpp_receivable_sell']))
        self.data[43]['param'][0]['receivable_spread'] = float(str(data['receivable_spread']))
        self.data[43]['param'][0]['subcard_no'] = data['subcard_no']
        self.data[43]['param'][0]['order_no'] = data['order_no']
        self.data[43]['param'][0]['id'] = data['id']

        response = self.http.http_request(self.data[43]['method'], self.data[43]['url'],
                                          self.data[43]['param'],
                                          self.data[43]['header'], cookies=None)
        result = response.json()
        print(self.data[43]['url'])
        print(self.data[43]['param'])
        print(result)
        return re

    def taskSettleToDoneJodHandle(self):
        """
        执行定时器，扫描结算状态已经是待审核的主任务,是否达到父任务结算条件
        :return:
        """

        response = self.http.http_request(self.data[44]['method'], self.data[44]['url'],
                                          self.data[44]['param'],
                                          self.data[44]['header'], cookies=None)
        result = response.json()
        print("执行定时器")
        return result


    def stopCard(self,task_id):
        param = {'task_id':task_id}
        self.applystop(**param)
        a = self.stopcard(**param)
        return a


if __name__ == '__main__':

    # from apiObject.setupApi import SetupApi
    from common.save_value import SaveValue

    # F端用户登录
    res_f = SetupApi().login_f("13729543834", 'e10adc3949ba59abbe56e057f20f883e')
    SaveValue.TOKEN = res_f['access_token']
    SaveValue.F_UUID = res_f['uuid']

    # V端用户登录

    res_v = SetupApi().login_v("13729547100", 'e10adc3949ba59abbe56e057f20f883e')
    SaveValue.TOKEN_V = res_v['access_token']
    SaveValue.V_UUID = res_v['uuid']

    # C端用户登录
    res_c = SetupApi().login_c("13729547062", 'e10adc3949ba59abbe56e057f20f883e')
    SaveValue.TOKEN_C = res_c['access_token']
    SaveValue.C_UUID = res_c['uuid']


    # print(Tool().task_subaudit(type=3))
    # print(Tool().accept_card)
    # print(Tool().confirm2())
    # print(Tool().task_check())
    # param = {'task_id':177668}
    # print(Tool().applystop(**param))177671
    # print(Tool().stopcard(**param))
    # print(Tool().task_apply())
    # print(Tool().task_pay(type=3))

    print(Tool().task_check(type=3))

    # print(Tool().putCanSettleOrderToAuditJodHandle())
    # print(Tool().taskAudit(type=3))
    # print(Tool().task_check(type=3))
    # print(Tool().taskSetSettleJodHandle())
    # print(Tool().putCanSettleOrderToAuditJodHandle())
    # print(Tool().taskSettleToDoneJodHandle())























