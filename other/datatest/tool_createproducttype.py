from mysql.pymongo_db import Mongodb

d = Mongodb("opensku")
client = d.get_mongodb_client()

db = client.opensku
collection = db.opensku_product
pr = collection.find({"_id":17713})
print(pr[0]['product_type'])
opensku_order = db.opensku_order
ord = opensku_order.find({"order_no":"101155136382638905"})
print(ord[0]['order_status'])
# order_query = { "product_type": {'$exists': False} }
# orders=opensku_order.find(order_query)
# # for o in orders:
# #     print(o)
# print(orders.count())

d.close()


