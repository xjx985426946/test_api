# from pymysql import connect,cursors
# from pymysql.err import  OperationalError
# import configparser as cparser
# from sshtunnel import SSHTunnelForwarder
# import pymongo
# from sshtunnel import SSHTunnelForwarder
#
# class Pydb(object):
#
#     def __init__(self,data_db):
#
#         #数据库名称
#         self.data_db = data_db
#         self.server = None
#         self.cursor = None
#
#     def dodb(self):
#
#         # 远程mysql服务配置
#         mysql_host = '10.0.1.193'
#         mysql_database = self.data_db
#         mysql_user = 'intbee'
#         mysql_password = 'intbee@mysql'
#
#         conn = connect(host=mysql_host,
#                        port=3306,
#                        user = mysql_user,
#                        passwd = mysql_password,
#                        db = mysql_database)
#         self.cursor = conn.cursor()
#         return self.cursor
#
#     def close(self):
#         self.cursor.close()
#
#
#
# class Mongodb(object):
#     def __init__(self, mongo_database):
#         self.mongo_database = mongo_database
#         self.server = None
#         self.client = None
#
#     def get_mongodb_client(self):
#         # 远程mongo服务配置
#         mongo_host = '10.0.1.193'
#         mongo_database = self.mongo_database
#         mongo_user = 'intbee'
#         mongo_password = 'mongo_test2016'
#
#         self.client = pymongo.MongoClient(mongo_host, 27017)
#         mongo_database = self.client[mongo_database]
#         mongo_database.authenticate(mongo_user, mongo_password)
#
#         return self.client
#
#     def close(self):
#         self.client.close()
#
#     # def do(self,db):
#     #     d = Mongodb(db)
#     #     client = d.get_mongodb_client()
#     #     return client
#
#
# # d = Mongodb("opensku2")
# # client = d.get_mongodb_client()
# # db = client.opensku2
# # collection = db.opensku_category
# # result = collection.find({}).sort("_id",-1)
# # print(result[0]['_id'])
# # d.close()
#



# from mysql.pymysql_db import Connectmysql
#
#
#
#
# class A(object):
#     def __init__(self):
#         self.b = 11
#     @property
#     def a(self):
#         con = Connectmysql("intbee")
#         sql = 'SELECT * FROM intbee_card WHERE product_id= %s;'
#         params = [618]
#         data = con.fetchone(sql, params)
#         print(data['id'])
#
# A().a



import requests

url = "https://test-www.intbee.com/fapi/card/cardtoactivity"

payload = "{\"card_id\":159921,\"plan_open_group\":true}"
headers = {
    'access_token': "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOm51bGwsImF1ZCI6IjEwMSIsInN1YiI6IjU4YTI3YTM0MDAwNmY5OWU3Y2I0MzA4NiIsImFwcGlkIjoiMTAxIiwiZXhwIjoxNTY1MDYxNDczLCJqdGkiOiJpQVpHQmZsTlpGQUdybWZQX2dkUTZBIiwiaWF0IjoxNTY0NDU2NjczLCJhdXRoX21vZGUiOiJtb2JpbGUiLCJhdXRoX2lkIjoiKzg2LTEzOTAyODcyODM2In0.B5Ty7Pv6Ncmc34VAYt5ZgjQCga8ynnHfl4NBCwagwMw",
    'Content-Type': "application/json",
    'Postman-Token': "ac0d3f19-2558-4f50-89eb-00f16456a74d"
    }

response = requests.request("POST", url, data=payload, headers=headers)

data = response.json
import time
start = time.clock()
while data:
    import requests

    url = "https://test-www.intbee.com/fapi/card"

    querystring = {"limit": "6", "cardStatus": "1", "cardNo": "19-10000557-126196", "offset": "0"}

    payload = ""
    headers = {
        'access_token': "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOm51bGwsImF1ZCI6IjEwMSIsInN1YiI6IjU4YTI3YTM0MDAwNmY5OWU3Y2I0MzA4NiIsImFwcGlkIjoiMTAxIiwiZXhwIjoxNTY1MDYxNDczLCJqdGkiOiJpQVpHQmZsTlpGQUdybWZQX2dkUTZBIiwiaWF0IjoxNTY0NDU2NjczLCJhdXRoX21vZGUiOiJtb2JpbGUiLCJhdXRoX2lkIjoiKzg2LTEzOTAyODcyODM2In0.B5Ty7Pv6Ncmc34VAYt5ZgjQCga8ynnHfl4NBCwagwMw",
        'Postman-Token': "4f2c3af2-a4c1-43ad-82bf-44be53b3f706"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    print("输出：",response.json()['result']['data'][0]['activity_ids'])
    if response.json()['result']['data'][0]['activity_ids'] == '8':
        end = time.clock()
        print("延迟时间为：", end - start)
        break

