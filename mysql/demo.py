# from pymysql import connect,cursors
# import pymongo
# from sshtunnel import SSHTunnelForwarder
#
#
# # class Mongodb(object):
# #
# #     def __init__(self,mongo_database):
# #         self.mongo_database = mongo_database
# #         self.server = None
# #         self.client = None
# #     def get_mongodb_client(self):
# #
# #         # 跳板参数 ssh
# #         ecs_host = '119.23.252.140'
# #         ecs_user = 'intbee'
# #         ecs_password = 'IntbeE2018'
# #
# #         #远程mongo服务配置
# #         mongo_host = '119.23.252.140'
# #         mongo_database = self.mongo_database
# #         mongo_user = 'intbee'
# #         mongo_password = 'ULmzi1t3qxdWvopFQcnbHf8C'
# #
# #         # 连接SSH
# #         self.server = SSHTunnelForwarder(
# #             ssh_address_or_host = (ecs_host,22),
# #             ssh_password=ecs_password,
# #             ssh_username=ecs_user,
# #             remote_bind_address=(mongo_host, 20017))
# #         self.server.start()
# #         self.client = pymongo.MongoClient('127.0.0.1', self.server.local_bind_port) #重要：一定要连接本地
# #         mongo_database = self.client[mongo_database]
# #         mongo_database.authenticate(mongo_user, mongo_password)
# #
# #         return self.client
# #
# #     def close(self):
# #         self.client.close()
# #         self.server.close()
# #
# #
# #
# #
# #
# #
# #
# #
# # class Pydb(object):
# #
# #     def __init__(self,data_db):
# #
# #         #数据库名称
# #         self.data_db = data_db
# #         self.server = None
# #         self.cursor = None
# #
# #     def dodb(self):
# #         # 跳板参数 ssh
# #         ecs_host = '119.23.252.140'
# #         ecs_user = 'intbee'
# #         ecs_password = 'IntbeE2018'
# #
# #         # 远程mysql服务配置
# #         mysql_host = '119.23.252.140'
# #         mysql_database = self.data_db
# #         mysql_user = 'intbee'
# #         mysql_password = 'mysql@intbee88678'
# #
# #         #连接ssh
# #
# #         self.server = SSHTunnelForwarder(
# #             (ecs_host, 22),  # B机器的配置
# #             ssh_password = ecs_password,
# #             ssh_username = ecs_user,
# #             remote_bind_address=(mysql_host, 23306))  # A机器的配置
# #
# #         self.server.start()
# #
# #         self.conn = connect(host='127.0.0.1',
# #                        port=self.server.local_bind_port,
# #                        user = mysql_user,
# #                        passwd = mysql_password,
# #                        db = mysql_database,
# #                        cursorclass=cursors.DictCursor)
# #         self.cursor = self.conn.cursor()
# #
# #         return self.cursor
# #
# #     def close(self):
# #         self.cursor.close()
# #         self.server.close()
#
#
#
# class Mongodb(object):
#
#     def __init__(self,mongo_database):
#         self.mongo_database = mongo_database
#         self.server = None
#         self.client = None
#     def get_mongodb_client(self):
#
#         # 跳板参数 ssh
#         ecs_host = '119.23.252.140'
#         ecs_user = 'intbee'
#         ecs_password = 'IntbeE2018'
#
#         #远程mongo服务配置
#         mongo_host = 'mongo.server.com'
#         mongo_database = self.mongo_database
#         mongo_user = 'intbee'
#         mongo_password = 'mongo_test2016'
#
#         # 连接SSH
#         self.server = SSHTunnelForwarder(
#             ssh_address_or_host = (ecs_host,22),
#             ssh_password=ecs_password,
#             ssh_username=ecs_user,
#             remote_bind_address=(mongo_host, 37017))
#         self.server.start()
#         self.client = pymongo.MongoClient('127.0.0.1', self.server.local_bind_port) #重要：一定要连接本地
#         mongo_database = self.client[mongo_database]
#         mongo_database.authenticate(mongo_user, mongo_password)
#
#         return self.client
#
#     def close(self):
#         self.client.close()
#         self.server.close()
#
#
#
#
#
#
#
#
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
#         # 跳板参数 ssh
#         ecs_host = '119.23.252.140'
#         ecs_user = 'intbee'
#         ecs_password = 'IntbeE2018'
#
#         # 远程mysql服务配置
#         mysql_host = '119.23.252.140'
#         mysql_database = self.data_db
#         mysql_user = 'intbee'
#         mysql_password = 'intbee@mysql'
#
#         #连接ssh
#
#         self.server = SSHTunnelForwarder(
#             (ecs_host, 22),  # B机器的配置
#             ssh_password = ecs_password,
#             ssh_username = ecs_user,
#             remote_bind_address=(mysql_host, 33306))  # A机器的配置
#
#         self.server.start()
#
#         self.conn = connect(host='127.0.0.1',
#                        port=self.server.local_bind_port,
#                        user = mysql_user,
#                        passwd = mysql_password,
#                        db = mysql_database,
#                        cursorclass=cursors.DictCursor)
#         self.cursor = self.conn.cursor()
#
#         return self.cursor
#
#     def close(self):
#         self.cursor.close()
#         self.server.close()
#
#
# a = Pydb("intbee")
# cursor = a.dodb()
# sql ='SELECT product_id FROM intbee.intbee_card where merchant_id = 1000 and status = 0 and card_status !=2 ;'
# cursor.execute(sql)
# results = cursor.fetchall()
# # print(results)
# a.close()
#
#
# d = Mongodb("opensku")
# client = d.get_mongodb_client()
#
# db = client.opensku
# collection = db.opensku_product
# for i in results:
#     result = collection.find({"_id": i['product_id']})
#     # try:
#     #     result[0]
#     #     print()
#     # except:
#     # print("card找不到商品,商品id为%s" % i['product_id'])
#     print(result[0])
# d.close()
#
# print("执行通过")
#
# # d = Mongodb("opensku")
# # client = d.get_mongodb_client()
# #
# # db = client.opensku
# # collection = db.opensku_product
# # result = collection.find({"_id":3512})
# # try:
# #     print(result[0])
# # except:
# #    print("card找不到商品,商品id为%s" %())
# # d.close()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# """
# 验证：
#
# SELECT count(*) FROM intbee.intbee_card where merchant_id = 1000 and status = 0 and card_status !=2 ;
#
#
# db.getCollection('opensku_product').find({"merchant_id":1000,sell_status:1}).count()
#
#
# 已上架的商品 = 建卡数
#
#
# 脚本验证:
#     demo环境循环遍历出所有merchant_id = 1000 and status = 0 and card_status !=2 的card  取card对应的product_id 去mongo库product表遍历查询数据，所有数据查到对应商品，则处理通过，有数据查不到，则mysql还是存在重复card
#
#     线上环境验证：目前有card找不到商品 已知的有 41590 - 41600
#     执行成功后：抽样查询这10条卡是否已经被删除 被删除则测试通过
#
# """
#
#
#
#
#
#
#
#
#
#
#
