


#查询库存为0的考拉商品
from mysql.pymongo_db import Mongodb
from common.logger import Log

from decimal import *
'''
path: 测试环境
验证考拉建卡是否正确'''

'''
1、读取考拉商品
2、验证建卡规则
'''


class TestCreateCard():
    '''链接Mongo数据库'''
    dbobj = Mongodb("opensku")
    client = dbobj.get_mongodb_client()
    db = client.opensku
    log = Log()



    def test_data(self):
        collection = self.db.opensku_product
        id = collection.find({"merchant_id":1000},{"_id":1})
        L = []
        for i in id:
            L.append(i)
        collection2 = self.db.opensku_product_stock
        j = 0

        for i in L:
            quan = collection2.find({"product_id":i['_id']},{"stock.quantity"})
            for q in quan:

                for n in q['stock']:
                    if n['quantity'] != 0:
                        break
                else:
                    j += 1

                    # print(q)

        print("考拉商品一共有%s个商品库存为0" %(j))

        self.dbobj.close()
        print("测试完成")


obj = TestCreateCard()
obj.test_data()



