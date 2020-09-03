from pymysql import connect,cursors
import pymongo
from sshtunnel import SSHTunnelForwarder
import os
class Mongodb(object):

    def __init__(self,mongo_database):
        self.mongo_database = mongo_database
        self.server = None
        self.client = None
    def get_mongodb_client(self):

        # 跳板参数 ssh
        ecs_host = '119.23.252.140'
        ecs_user = 'intbee'
        ecs_password = 'IntbeE2018'

        #远程mongo服务配置
        mongo_host = 'mongo.server.com'
        mongo_database = self.mongo_database
        mongo_user = 'intbee'
        mongo_password = 'mongo_test2016'

        # 连接SSH
        self.server = SSHTunnelForwarder(
            ssh_address_or_host = (ecs_host,22),
            # ssh_password=ecs_password,
            ssh_pkey=os.path.dirname(__file__)+ '/intbee-test-intbee.key',
            ssh_username=ecs_user,
            remote_bind_address=(mongo_host, 27017))
        self.server.start()
        self.client = pymongo.MongoClient('127.0.0.1', self.server.local_bind_port) #重要：一定要连接本地
        mongo_database = self.client[mongo_database]
        mongo_database.authenticate(mongo_user, mongo_password)

        return self.client

    def close(self):
        self.client.close()
        self.server.close()



class Pydb(object):

    def __init__(self,data_db):

        #数据库名称
        self.data_db = data_db
        self.server = None
        self.cursor = None

        ecs_host = '119.23.252.140'
        ecs_user = 'intbee'
        ecs_password = 'IntbeE2018'


        # 远程mysql服务配置
        mysql_host = '192.168.1.53'
        mysql_database = self.data_db
        mysql_user = 'intbee'
        mysql_password = 'intbee@mysql'

        # 连接ssh

        self.server = SSHTunnelForwarder(
            (ecs_host, 22),  # B机器的配置
            ssh_password=ecs_password,
            ssh_pkey=os.path.dirname(__file__)+ '/intbee-test-intbee.key',
            ssh_username=ecs_user,
            remote_bind_address=(mysql_host, 3306))  # A机器的配置

        self.server.start()

        self.conn = connect(host='127.0.0.1',
                            port=self.server.local_bind_port,
                            user=mysql_user,
                            passwd=mysql_password,
                            db=mysql_database
                            # cursorclass=cursors.DictCursor
                            )
        self.cursor = self.conn.cursor()

    def dodb(self):
        # 跳板参数 ssh
        return self.cursor

    def dconn(self):
        return self.conn

    def close(self):
        self.cursor.close()
        self.server.close()
        self.conn.close()
# class A:

#     def __init__(self):
#         a = 1
#     def a(self):
#         d = Mongodb("opensku")
#         client = d.get_mongodb_client()
#         db = client.opensku
#         collection = db.opensku_standard
#         results = collection.find({"shop_info.shop_id": "5b2a1535b0bcdf00088d7cea"}).sort("_id", -1)
#         print(results[0]['_id'])
#         d.close()
#
# A().a()






# d = Mongodb("opensku")
#
# client = d.get_mongodb_client()
# db = client.opensku
# collection = db.opensku_product
# collection2 = db.opensku_product_stock
# result = collection.find({"merchant_id":1000})
# for i in result:
#     result2 = collection2.find({"product_id":i['_id']})
#     for n in result2:
#         for m in n['stock']:
#            if len(m['standards'])>1:
#                print(i['_id'])
#
# print("测试完成")
# d.close()


# d = Mongodb("opensku")
#
# client = d.get_mongodb_client()
# db = client.opensku
# collection = db.opensku_product
# collection2 = db.opensku_product_stock
# result = collection.find({"merchant_id":1000})
# active = None
# for i in result:
#     result2 = collection2.find({"product_id":i['_id']})
#     for n in result2:
#         if len(n['stock']) > 1:
#             print("有多个sku-------------------------------",i['_id'])
#             active = 1
#             break
#
#         else:
#             print("只有一个sku")
#     if active == 1:
#         break
#
#
# print("测试完成")
# d.close()

# a = Pydb("intbee")
# cursor = a.dodb()
# print(cursor)
# sql ='SELECT * FROM intbee_card WHERE merchant_id={0};'.format(1000)
# cursor.execute(sql)
# results = cursor.fetchall()
# print(results)
#
# a.close()
