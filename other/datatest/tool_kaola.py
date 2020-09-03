# this kaola data test
from mysql.pymongo_db import Mongodb
from common.logger import Log
from pymysql import connect,cursors
from sshtunnel import SSHTunnelForwarder
from decimal import *
'''
path: 测试环境
验证不符合考拉建卡的数据'''


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
        j = 0
        for i in id:
            result = collection2.find({"product_id":i['_id']})
            for stock in result[0]['stock']:
                intbee_price = round(0.98 * float(str(stock['guide_price'])))
                intbee_reward = int(0.5 * (0.98 * float(str(stock['guide_price'])) - float(str(stock['delivery_price']))))
                if intbee_price - float(str(stock['delivery_price'])) <= 0:
                    # self.log.info("不符合建卡")
                    sql = 'SELECT * FROM intbee_card WHERE product_id={0};'.format(i['_id'])
                    self.cursor.execute(sql)
                    results = self.cursor.fetchall()
                    print(results)
                    if results == ():
                        # self.log.info("不符合建卡的没有成功建卡，通过")
                        break
                        pass
                    else:
                        self.log.info("不符合建卡的商品也建卡了，不通过商品%s" %(i['_id']))
            else:
                j += 1
        print(j)
        Log().info("未符合价格建卡的数据%s" %(j))
        self.a.close()

        self.dbobj.close()
        print("测试完成")


obj = TestCreateCard()
obj.test_data()



