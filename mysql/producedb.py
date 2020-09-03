from pymysql import connect,cursors
import pymongo
from sshtunnel import SSHTunnelForwarder

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
        mongo_host = '10.0.1.44'
        mongo_database = self.mongo_database
        mongo_user = 'viewer'
        mongo_password = 'viewer2018'

        # 连接SSH
        self.server = SSHTunnelForwarder(
            ssh_address_or_host = (ecs_host,20039),
            ssh_password=ecs_password,
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

    def dodb(self):
        # 跳板参数 ssh
        ecs_host = '119.23.252.140'
        ecs_user = 'intbee'
        ecs_password = 'IntbeE2018'

        # 远程mysql服务配置
        mysql_host = '10.0.1.44'
        mysql_database = self.data_db
        mysql_user = 'yunying'
        mysql_password = 'yunying2018'

        #连接ssh

        self.server = SSHTunnelForwarder(
            (ecs_host, 20039),  # B机器的配置
            ssh_password = ecs_password,
            ssh_username = ecs_user,
            remote_bind_address=(mysql_host, 3306))  # A机器的配置

        self.server.start()

        self.conn = connect(host='127.0.0.1',
                       port=self.server.local_bind_port,
                       user = mysql_user,
                       passwd = mysql_password,
                       db = mysql_database,
                       cursorclass=cursors.DictCursor)
        self.cursor = self.conn.cursor()

        return self.cursor

    def close(self):
        self.cursor.close()
        self.server.close()
        self.conn.close()
# a = Pydb("intbee")
# cursor = a.dodb()
# sql ='SELECT id FROM `intbee_card` WHERE product_id={0};'.format(73197)
# cursor.execute(sql)
# results = cursor.fetchall()
# print(results[0]['id'])
# # for re in results:
# #     print(re)
# print(results)
# a.close()


# if __name__ == '__main__':
#     a = Pydb("intbee")
#     cursor = a.dodb()
#     sql ='SELECT id FROM `intbee_card` WHERE product_id={0};'.format(73197)
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     print(results[0]['id'])
#     # for re in results:
#     #     print(re)
#     print(results)
#     a.close()



