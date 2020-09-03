
#查询出考拉单规格的商品
from mysql.pymongo_db import Mongodb

d = Mongodb("opensku")
client = d.get_mongodb_client()

db = client.opensku
collection = db.opensku_product

collection2 = db.opensku_product_stock
result = collection.find({'merchant_id':1000})
L = []
for i in result:
    # L.append(i['_id'])
    result = collection2.find({'product_id': i['_id']})
    for n in result:
        print(n)
        if len(['stock']) == 1:
            print(n)


d.close()




#验证空品类的商品处理正确
d = Mongodb("opensku")
client = d.get_mongodb_client()

db = client.opensku
products = db.opensku_product
result = products.find({})

categorys = db.opensku_category

for product in result:

    category = categorys.find_one({"_id": product["last_category_id"]})
    if category == None:

        if product['status'] == 1:
            print(product)
print("完成")






