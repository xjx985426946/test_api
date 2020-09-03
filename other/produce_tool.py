import time
from common.httprequest import HttpRquest
from mysql.producedb import Pydb,Mongodb
from common.readyaml import read_yaml
import os
from conf import read_path
from common.readyaml import update_yaml
import requests


class Tool(object):
    def __init__(self):
        self.http = HttpRquest()
        self.dir =  os.path.dirname(os.path.realpath(__file__)) + "/tooldata/"
        self.url = 'http://api.intbee.com/'

        url = "http://api.intbee.com/api/uc/auth/login"

        payload = "{\"mobile\":\"13729542194\",\"password\":\"b7ec7a6d28c12f213b79627fa75f588e\"}"
        headers = {
            'Content-Type': "application/json",
            'app_id': "101",
            'Postman-Token': "508b371a-71c5-4524-9dc7-889dd6f95cea"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        self.token_c =response.json()['result']['access_token']

        url = "http://api.intbee.com/api/uc/auth/login"

        payload = "{\"mobile\":\"13902879682\",\"password\":\"25d55ad283aa400af464c76d713c07ad\"}"
        headers = {
            'Content-Type': "application/json",
            'app_id': "101",
            'Postman-Token': "508b371a-71c5-4524-9dc7-889dd6f95cea"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        self.token_f = response.json()['result']['access_token']

        self.data = read_yaml(self.dir, 'tooldataproduce.yaml', self.url, token=self.token_f)

    @property
    def create_product(self):
        '''创建商品'''
        name = update_yaml(read_path.commondata, "data.yaml", 'num')
        self.data[0]['param']['product_name'] = self.data[0]['param']['product_name'] + str(name)
        response = self.http.http_request(self.data[0]['method'], self.data[0]['url'],
                                          self.data[0]['param'],
                                          self.data[0]['header'], cookies=None)
        result = response.json()
        print("商品创建成功：---------------",result)
        return result



    # @property
    # def create_card(self,product_id):
    #     '''发布普通蜂卡'''
    #     self.data[2]['param']['product_id'] = product_id
    #     response = self.http.http_request(self.data[2]['method'], self.data[2]['url'],
    #                                       self.data[2]['param'],
    #                                       self.data[2]['header'], cookies=None)
    #     print(self.data[2])
    #     result = response.json()
    #     print("普通蜂卡发布成功:------------------",result)
    #     db = Pydb("intbee")
    #     cursor = db.dodb()
    #     import time
    #     time.sleep(3)
    #     sql = 'SELECT id FROM `intbee_card` WHERE product_id={0};'.format(self.data[2]['param']['product_id'])
    #     cursor.execute(sql)
    #     results = cursor.fetchall()
    #     db.close()
    #     return result,self.data[2]['param']['product_id'],results[0][0]



    def create_cardto(self,product_id):
        '''发布定向蜂卡'''

        self.data[3]['param']['product_id'] = product_id
        print(self.data[3])
        response = self.http.http_request(self.data[3]['method'], self.data[3]['url'],
                                          self.data[3]['param'],
                                          self.data[3]['header'], cookies=None)
        result = response.json()
        db = Pydb("intbee")
        cursor = db.dodb()
        import time
        time.sleep(3)
        sql = 'SELECT id FROM `intbee_card` WHERE product_id={0};'.format(product_id)
        cursor.execute(sql)
        results = cursor.fetchall()
        db.close()
        return results[0]['id'],result

    # @property
    # def create_card3(self):
    #     '''发布蜂团蜂卡'''
    #     self.data[4]['param']['product_id'] = self.create_product['result']
    #     response = self.http.http_request(self.data[4]['method'], self.data[4]['url'],
    #                                       self.data[4]['param'],
    #                                       self.data[4]['header'], cookies=None)
    #     print(self.data[4]['param'])
    #     result = response.json()
    #     return result
    #
    # @property
    # def create_card4(self):
    #     '''发布拼团蜂卡'''
    #     # self.data[5]['param']['product_id'] = self.product_no_postage['result']['result']
    #     response = self.http.http_request(self.data[5]['method'], self.url,
    #                                       self.data[5]['param'],
    #                                       self.data[5]['header'], cookies=None)
    #     result = response.json()
    #     return result
    #
    # @property
    # def accept_card(self):
    #     '''接受蜂卡'''
    #
    #     db = Pydb("intbee")
    #     cursor = db.dodb()
    #     b = self.create_card[1]
    #     import time
    #     time.sleep(3)
    #     sql = 'SELECT id FROM `intbee_card` WHERE product_id={0};'.format(b)
    #     cursor.execute(sql)
    #     results = cursor.fetchall()
    #     self.data[6]['url'] = self.data[6]['url'] + "/"+str(results[0][0]) + '/accept'
    #     self.data[6]['header']['access_token'] = self.token_c
    #     response = self.http.http_request(self.data[6]['method'],  self.data[6]['url'],
    #                                       self.data[6]['param'],
    #                                       self.data[6]['header'], cookies=None)
    #     result = response.json()
    #     print(self.data[6])
    #     print("成功接受普通蜂卡-----------------",result)
    #     db.close()
    #     return b,results[0][0]
    #
    #
    @property
    def confirm(self):
        '''下单不使用优惠券'''
        self.data[7]['header']['access_token'] = self.token_c
        response = self.http.http_request(self.data[7]['method'], self.data[7]['url'],
                                          self.data[7]['param'],
                                          self.data[7]['header'], cookies=None)
        print(self.data[7])
        result = response.json()
        print("成功下单---------------------",result)

        return result

    #
    # #fapi/activity/coupon
    # @property
    # def createcoupone(self):
    #     '''创建店铺优惠券（无金额限制）'''
    #     response = self.http.http_request(self.data[8]['method'], self.data[8]['url'],
    #                                       self.data[8]['param'],
    #                                       self.data[8]['header'], cookies=None)
    #
    #
    #     result = response.json()
    #     print("成功创建优惠券---------------------", result)
    #
    #     db = Pydb("intbee")
    #     cursor = db.dodb()
    #     sql = 'SELECT * FROM intbee_activity_coupon WHERE corporate_uuid="5b2a1535b0bcdf00088d7cea" ORDER BY id DESC limit 1';
    #     cursor.execute(sql)
    #     results = cursor.fetchall()[0][0]
    #     db.close()
    #
    #     return results
    #
    # #fapi/postage
    # @property
    # def createpostage(self):
    #     '''创建运费模板'''
    #     response = self.http.http_request(self.data[9]['method'], self.data[9]['url'],
    #                                       self.data[9]['param'],
    #                                       self.data[9]['header'], cookies=None)
    #
    #     result = response.json()
    #     print("成功创建运费模板---------------------", result)
    #     return result
    #
    #
    # @property
    # def createaddress(self):
    #     '''创建地址'''
    #     self.data[11]['header']['access_token'] = self.token_c
    #     # self.data[5]['param']['product_id'] = self.product_no_postage['result']['result']
    #     response = self.http.http_request(self.data[11]['method'],  self.data[11]['url'],
    #                                       self.data[11]['param'],
    #                                       self.data[11]['header'], cookies=None)
    #     # print(self.data[11])
    #     result = response.json()
    #     return result['result']['id']
    #
    # @property
    # def card_v(self):
    #     '''发布定向卡'''
    #     product_id = self.create_product['result']
    #     result = self.create_card2(product_id)
    #     return result
    #
    # @property
    # def createinventory(self):
    #     '''创建清单'''
    #     self.data[12]['header']['access_token'] = self.token_c
    #     response = self.http.http_request(self.data[12]['method'],  self.data[12]['url'],
    #                                       self.data[12]['param'],
    #                                       self.data[12]['header'], cookies=None)
    #     result = response.json()
    #     return result['result']['inventory_id']
    # @property
    # def createstandard(self):
    #     response = self.http.http_request(self.data[10]['method'], self.data[10]['url'],
    #                                       self.data[10]['param'],
    #                                       self.data[10]['header'], cookies=None)
    #     result = response.json()
    #     d = Mongodb("opensku")
    #     client = d.get_mongodb_client()
    #     db = client.opensku
    #     time.sleep(2)
    #     collection = db.opensku_standard
    #     results= collection.find({"shop_info.shop_id": "5b2a1535b0bcdf00088d7cea"}).sort("_id", -1)
    #     a = results[0]
    #     d.close()
    #     print("成功创建规格---------------------", result)
    #     return a['_id']
# print(Tool().create_cardto(Tool().create_product['result']))
# print(Tool().createstandard)
# print(Tool().accept_card)
# print(Tool().create_product)
# print(Tool().createinventory)
#
# print(Tool().createcoupone)
# print(Tool().create_product)
# print(Tool().create_card3)

t = Tool()
# print(t.confirm)
# print(t.create_cardto(product_id))