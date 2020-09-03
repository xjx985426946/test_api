import pymongo
from sshtunnel import SSHTunnelForwarder
import os
from conf import dbConfig
class Mongodb(object):

    def __init__(self,mongo_database):
        self.mongo_database = mongo_database
        self.server = None
        self.client = None
    def get_mongodb_client(self):

        # 跳板参数 ssh
        ecs_host = dbConfig.ecs_host
        ecs_user = dbConfig.ecs_user
        ecs_password = dbConfig.ecs_password
        ecs_port = dbConfig.ecs_port

        #远程mongo服务配置
        mongo_host = dbConfig.mongo_host
        mongo_database = self.mongo_database
        mongo_user = dbConfig.mongo_user
        mongo_password = dbConfig.mongo_password


        # 连接SSH
        self.server = SSHTunnelForwarder(
            ssh_address_or_host = (ecs_host,ecs_port),
            ssh_password=ecs_password,
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

if __name__ == '__main__':
    # from bson.objectid import ObjectId
    # d = Mongodb("opensku")
    # client = d.get_mongodb_client()
    #
    # db = client.opensku
    # collection = db.opensku_address
    # result = collection.find({"_id":ObjectId("5e048a1092f9980006636cc5")})
    # print(result[0])
    # d.close()



    d = Mongodb("intbee")
    client = d.get_mongodb_client()

    db = client.intbee
    collection = db.intbee_apply_record
    result = collection.find({"card_id": 174257,"spreader_uuid":'5e1c05ce260f74000637aa90'})
    print(result[0]['_id'])
    d.close()


