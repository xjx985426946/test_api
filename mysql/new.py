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
            ssh_pkey=os.path.dirname(__file__) + '/intbee-test-intbee.key',
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
        mysql_host = '192.168.1.53'
        mysql_database = self.data_db
        mysql_user = 'intbee'
        mysql_password = 'intbee@mysql'

        #连接ssh

        self.server = SSHTunnelForwarder(
            (ecs_host, 22),  # B机器的配置
            ssh_password = ecs_password,
            ssh_pkey=os.path.dirname(__file__) + '/intbee-test-intbee.key',
            ssh_username = ecs_user,
            remote_bind_address=(mysql_host, 3306))  # A机器的配置

        self.server.start()

        self.conn = connect(host='127.0.0.1',
                            port=self.server.local_bind_port,
                            user=mysql_user,
                            passwd=mysql_password,
                            db=mysql_database,
                            cursorclass=cursors.DictCursor
                            )

        self.cursor = self.conn.cursor()

        return self.cursor

    def close(self):
        self.cursor.close()
        self.server.close()




if __name__ == '__main__':

    pass
    # d = Mongodb("opensku")
    # client = d.get_mongodb_client()
    # db = client.opensku
    # # collection = db.opensku_product
    # # result = collection.update({'_id':106072},{'$set':{"sell_status":1}})
    #
    # collection =  db.opensku_product_stock
    # result = collection.update({'stock.sku':'2025488-adcce0d8991dad04874b3d3c5d1ae62f'},{'$set':{'stock.$.sku_sell_status':0}})
    # result2 = collection.update({'stock.sku':'2025488-ced58a93abe2a12907044660910b3b33'},{'$set':{'stock.$.sku_sell_status':0}})
    # d.close()
