

# 考拉商品修复运费模板，脚本测试

from mysql.new import Mongodb, Pydb
d = Mongodb("opensku")
client = d.get_mongodb_client()

db = client.opensku
collection = db.opensku_product
result = collection.find({"merchant_id": 1000})
L = []
for i in result:
    collection2 = db.opensku_product_stock
    for i in result:
        result2 = collection2.find({"product_id": i['_id']})
        for n in result2:
            stockList = n['stock']
            n = 0
            for stocks in stockList:
                delivery_price = float(str(stocks["delivery_price"]))
                n += 1
                if delivery_price == 88.00:
                    if i['postage_id'] == '5c99c0d552faff000584c2b6':
                        print(i['_id'])
                        pass
                    else:
                        print("失败")
                        print(i['_id'])

                    break

                else:

                    if n == len(stockList):
                        if i['postage_id'] == '0':
                            print(i['_id'])
                        else:
                            print("失败")
                            print(i['_id'])
                    else:
                        continue

print("测试完成")
d.close()

