from common.excle import Excel
from mysql.pymongo_db import Mongodb
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from pymongo import MongoClient
# import mysql.connector
# import json
import requests

ex = Excel("11.xlsx")
datas = ex.getData(sheetName="Sheet1")

# conf_file = open("/etc/intbee/env.json")
# env = json.load(conf_file)
#
# mysql_env = env.get("mysql", {})
# mysql_host = mysql_env.get("host")
# mysql_port = mysql_env.get("port")
# mysql_user = mysql_env.get("user")
# mysql_passwd = mysql_env.get("password")
#
# mongo_env = env.get("mongo", {})
# mongo_host = mongo_env.get("host")
# mongo_port = mongo_env.get("port")
# mongo_user = mongo_env.get("user")
# mongo_passwd = mongo_env.get("password")
#
# conn = mysql.connector.connect(host=mysql_host,user=mysql_user, password=mysql_passwd, database='intbee',buffered=True)
# cursor = conn.cursor()
#
# client = MongoClient(mongo_host, mongo_port)
# db = client['opensku']
# db.authenticate(mongo_user, mongo_passwd)
# collection = db['opensku_product_sku']

d = Mongodb("opensku")
client = d.get_mongodb_client()

db = client.opensku
collection = db.opensku_product_stock

headers = {
    'app_id': "101",
    'access_token': 'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOm51bGwsImF1ZCI6IjEwMSIsInN1YiI6IjU4YTI3YTM0MDAwNmY5OWU3Y2I0MzA4NiIsImFwcGlkIjoiMTAxIiwiZXhwIjoxNTczMTkzMDYxLCJqdGkiOiJpdXA3U1RzejFGMGdiMk4wUUhjYVhRIiwiaWF0IjoxNTcyNTg4MjYxLCJhdXRoX21vZGUiOiJtb2JpbGUiLCJhdXRoX2lkIjoiKzg2LTEzOTAyODcyODM2In0.GhvQy8HDIJYDB5SVZz4M8_oaCqfRDV8sqyOkuDu5ksU'
    }

url = 'https://test-api.intbee.com/fapi/card/create'

for data in datas:

    #查询商品id
    results = collection.find({"stock.sku": data['商品sku编号']})

    for result in results:

        param1 = {
            "card_type": 1,
            "card_end_time": 1573228799000,
            "kind_cpm": {
                "reward_amount": 60,
                "user_limit": 30
            },
            "product_id": result['product_id'],
            "reward_amount": float(str(data['佣金']).split(',')[0][1:]),
            "reward_vip_amount":float(str(data['佣金']).split(',')[0][1:])
        }
        print(param1)
        response1 = requests.request("POST", url, json=param1, headers=headers)
        print("创建60cpm---", response1.json())


        #
        # param2 = {
        #     "card_type": 1,
        #     "kind_cpm": {
        #         "reward_amount": 80,
        #         "user_limit": 30
        #     },
        #     "product_id": result['product_id'],
        #     "reward_amount": float(str(data['佣金']).split(',')[0][1:]),
        #     "reward_vip_amount": float(str(data['佣金']).split(',')[0][1:])
        # }
        #
        # response2 = requests.request("POST", url, json=param2, headers=headers)
        #
        # print("创建80cpm---", response2.json())
        #
        # param3 = {
        #     "card_type": 1,
        #     "kind_cpm": {
        #         "reward_amount": 150,
        #         "user_limit": 30
        #     },
        #     "product_id": result['product_id'],
        #     "reward_amount": float(str(data['佣金']).split(',')[0][1:]),
        #     "reward_vip_amount": float(str(data['佣金']).split(',')[0][1:])
        # }
        #
        # response3 = requests.request("POST", url, json=param3, headers=headers)
        #
        # print("创建150cpm---", response3.json())
        #
        # param4 = {
        #     "card_type": 1,
        #     "kind_cpm": {
        #         "reward_amount": 300,
        #         "user_limit": 30
        #     },
        #     "product_id": result['product_id'],
        #     "reward_amount": float(str(data['佣金']).split(',')[0][1:]),
        #     "reward_vip_amount": float(str(data['佣金']).split(',')[0][1:])
        # }
        #
        # response4= requests.request("POST", url, json=param4, headers=headers)
        #
        # print("创建300cpm---", response4.json())
        #
        # param5 = {
        #     "card_type": 1,
        #     "kind_cpm": {
        #         "reward_amount": 500,
        #         "user_limit": 30
        #     },
        #     "product_id": result['product_id'],
        #     "reward_amount": float(str(data['佣金']).split(',')[0][1:]),
        #     "reward_vip_amount": float(str(data['佣金']).split(',')[0][1:])
        # }
        #
        # response5 = requests.request("POST", url, json=param5, headers=headers)
        #
        # print("创建500cpm---", response5.json())


print("所有任务创建成功")
client.close()