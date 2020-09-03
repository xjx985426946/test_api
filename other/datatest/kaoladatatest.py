# # this kaola data test
# from mysql.pymongo_db import Mongodb
# from common.logger import Log
# from pymysql import connect,cursors
# from sshtunnel import SSHTunnelForwarder
# from decimal import *
# '''
# path: 测试环境
# 验证考拉建卡是否正确'''
#
# '''
# 1、读取考拉商品
# 2、验证建卡规则
# '''
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
#         mysql_host = '192.168.1.53'
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
#             remote_bind_address=(mysql_host, 3306))  # A机器的配置
#
#         self.server.start()
#
#         conn = connect(host='127.0.0.1',
#                        port=self.server.local_bind_port,
#                        user = mysql_user,
#                        passwd = mysql_password,
#                        db = mysql_database,
#                        cursorclass = cursors.DictCursor)
#         self.cursor = conn.cursor()
#
#         return self.cursor
#
#     def close(self):
#         self.cursor.close()
#         self.server.close()
#
#
#
# class TestCreateCard():
#     '''链接Mongo数据库'''
#     dbobj = Mongodb("opensku")
#     client = dbobj.get_mongodb_client()
#     db = client.opensku
#     log = Log()
#
#     '''链接mysql数据库'''
#     a = Pydb("intbee")
#     cursor = a.dodb()
#
#
#     def test_data(self):
#         collection = self.db.opensku_product
#         num = collection.find({"merchant_id":1000}).count()
#         self.log.info("考拉商品一共有%s条数据" %(num))
#         self.log.info("根据规则计算多少条数据符合建卡数量")
#         id = collection.find({"merchant_id":1000},{"_id":1})
#
#         collection2 = self.db.opensku_product_stock
#
#         for i in id:
#             result = collection2.find({"product_id":i['_id']})
#             for stock in result[0]['stock']:
#                 intbee_price = round(0.98 * float(str(stock['guide_price'])))
#                 intbee_reward = round(0.5 * (0.98 * float(str(stock['guide_price'])) - float(str(stock['delivery_price']))))
#                 if intbee_price - float(str(stock['delivery_price'])) > 0:
#                     # self.log.info("考拉商品%s符合建卡" %(i['_id']))
#                     # self.log.info("查看符合建卡的商品是否成功建卡")
#                     sql ='SELECT * FROM intbee_card WHERE product_id={0};'.format(i['_id'])
#                     self.cursor.execute(sql)
#                     results = self.cursor.fetchall()
#                     if results != ():
#                         for result in results:
#                             if int(result['product_price']) == int(intbee_price) and int(intbee_reward) == int(result['reward_amount']):
#                                 # self.log.info(int(result['product_price']))
#                                 # self.log.info(intbee_price)
#                                 # self.log.info(intbee_reward)
#                                 # self.log.info(int(result['reward_amount']))
#                                 # self.log.info("商品%s建卡成功" %(i['_id']))
#                                 pass
#                             else:
#                                 # self.log.info("商品%s建卡成功,但金额或者服务费不正确" % (i['_id']))
#                                 # self.log.info(int(result['product_price']))
#                                 # self.log.info(intbee_price)
#                                 # self.log.info(intbee_reward)
#                                 # self.log.info(int(result['reward_amount']))
#                                 # self.log.info("商品%s建卡成功" % (i['_id']))
#                                 pass
#                     else:
#                         self.log.info("商品%s建卡失败" % (i['_id']))
#                     # print(i['_id'])
#                     # print(results)
#                 else:
#                     continue
#         self.a.close()
#
#         self.dbobj.close()
#         print("测试完成")
#
#
# obj = TestCreateCard()
# obj.test_data()
#
#
#







# this kaola data test
from mysql.pymongo_db import Mongodb
from common.logger import Log
from pymysql import connect,cursors
from sshtunnel import SSHTunnelForwarder
from decimal import *
'''
path: 测试环境
验证考拉建卡是否正确'''

'''
1、读取考拉商品
2、验证建卡规则
'''


class Pydb(object):

    def __init__(self,data_db):

        #数据库名称
        self.data_db = data_db
        self.server = None
        self.cursor = None

    def dodb(self):
        # 跳板参数 ssh
        ecs_host = '119.23.252.140'
        ecs_user = 'intbee'
        ecs_password = 'IntbeE2018'

        # 远程mysql服务配置
        mysql_host = '192.168.1.53'
        mysql_database = self.data_db
        mysql_user = 'intbee'
        mysql_password = 'intbee@mysql'

        #连接ssh

        self.server = SSHTunnelForwarder(
            (ecs_host, 22),  # B机器的配置
            ssh_password = ecs_password,
            ssh_username = ecs_user,
            remote_bind_address=(mysql_host, 3306))  # A机器的配置

        self.server.start()

        conn = connect(host='127.0.0.1',
                       port=self.server.local_bind_port,
                       user = mysql_user,
                       passwd = mysql_password,
                       db = mysql_database,
                       cursorclass = cursors.DictCursor)
        self.cursor = conn.cursor()

        return self.cursor

    def close(self):
        self.cursor.close()
        self.server.close()



class TestCreateCard():
    '''链接Mongo数据库'''
    dbobj = Mongodb("opensku")
    client = dbobj.get_mongodb_client()
    db = client.opensku
    log = Log()

    '''链接mysql数据库'''
    a = Pydb("intbee")
    cursor = a.dodb()


    def test_data(self):
        collection = self.db.opensku_product
        num = collection.find({"merchant_id":1000}).count()
        self.log.info("考拉商品一共有%s条数据" %(num))
        self.log.info("根据规则计算多少条数据符合建卡数量")
        id = collection.find({"merchant_id":1000},{"_id":1})

        collection2 = self.db.opensku_product_stock

        for i in id:
            result = collection2.find({"product_id":i['_id']})
            for re in result:
                for stock in re['stock']:
                    #目前的是只要有一个商品的规格不符合建卡，就不建卡
                    intbee_price = round(0.98 * float(str(stock['guide_price'])))
                    intbee_reward = round(0.5 * (0.98 * float(str(stock['guide_price'])) - float(str(stock['delivery_price']))))
                    if 0.98 * float(str(stock['guide_price'])) - float(str(stock['delivery_price'])) <= 0:
                        break
                    else:
                        if re['total_quantity'] > 0:
                            # self.log.info("考拉商品%s符合建卡" %(i['_id']))
                            # self.log.info("查看符合建卡的商品是否成功建卡")
                            sql ='SELECT * FROM intbee_card WHERE product_id={0};'.format(i['_id'])
                            self.cursor.execute(sql)
                            results = self.cursor.fetchall()
                            if results != ():
                                for result in results:
                                    if int(result['product_price']) == int(intbee_price) and int(intbee_reward) == int(result['reward_amount']):
                                        # self.log.info(int(result['product_price']))
                                        # self.log.info(intbee_price)
                                        # self.log.info(intbee_reward)
                                        # self.log.info(int(result['reward_amount']))
                                        # self.log.info("商品%s建卡成功" %(i['_id']))
                                        pass

                                    else:
                                        self.log.info("商品%s建卡成功,但金额或者服务费不正确" % (i['_id']))
                                        # self.log.info(int(result['product_price']))
                                        # self.log.info(intbee_price)
                                        # self.log.info(intbee_reward)
                                        # self.log.info(int(result['reward_amount']))
                                        # self.log.info("商品%s建卡成功" % (i['_id']))
                                        pass

                            else:

                                # self.log.info("商品%s建卡失败" % (i['_id']))
                                pass


                                # print(i['_id'])
                                # print(results)





        self.a.close()

        self.dbobj.close()
        print("测试完成")


obj = TestCreateCard()
obj.test_data()



