#批量计算考拉供货价和考拉价的比值


from mysql.pymongo_db import Mongodb

d = Mongodb("opensku")
client = d.get_mongodb_client()

db = client.opensku
productdb = db.opensku_product
results = productdb.find({"merchant_id":1000}).limit(10000)
productList = []
for result in results:
    productList.append(result['_id'])

num = 0

nu1 = 0
nu2 = 0
nu3 = 0
nu4 = 0
nu5 = 0
nu6 = 0
nu7 = 0
nu8 = 0
nu9 = 0
nu10 = 0

n = 0

skudb = db.opensku_product_stock
for id in productList:
    results = skudb.find({"product_id":id})
    for stocks in results:
        for stock in stocks['stock']:
            nu = float(str(stock['delivery_price'])) / float(str(stock['guide_price']))
            if int(nu * 10) == 1:
                nu1 += 1
                print("1",id)
            elif int(nu * 10) == 2:
                nu2 += 1
                print("2", id)
            elif int(nu * 10) == 3:
                nu3 += 1
                print("3", id)
            elif int(nu * 10) == 4:
                print("4", id)
                nu4 += 1
            elif int(nu * 10) == 5:
                print("5", id)
                nu5 += 1
            elif int(nu * 10) == 6:
                nu6 += 1
            elif int(nu * 10) == 7:
                nu7 += 1
            elif int(nu * 10) == 8:
                nu8 += 1
            elif int(nu * 10) == 9:
                nu9 += 1
            elif int(nu * 10) == 10:
                nu10 += 1
            # # print("未计算之前",num)
            # num += nu
            # # print("计算之后",num)
            n += 1
print("一共查询了%s个sku,供货价与考拉价的比值的分布情况:" %n)
print("比值约为百分之十的有%s个"%nu1)
print("比值约为百分之二十的有%s个"%nu2)
print("比值约为百分之三十的有%s个"%nu3)
print("比值约为百分之四十的有%s个"%nu4)
print("比值约为百分之五十的有%s个"%nu5)
print("比值约为百分之六十的有%s个"%nu6)
print("比值约为百分之七十的有%s个"%nu7)
print("比值约为百分之八十的有%s个"%nu8)
print("比值约为百分之九十的有%s个"%nu9)
print("比值约为一比一的有%s个"%nu10)
d.close()

# 计算考拉库存范围


# from mysql.pymongo_db import Mongodb
#
# d = Mongodb("opensku")
# client = d.get_mongodb_client()
# db = client.opensku
# productdb = db.opensku_product
# results = productdb.find({"merchant_id":1000})
# productList = []
# for result in results:
#     productList.append(result['_id'])
#
# num = 0
# nu1 = 0
# nu2 = 0
# nu3 = 0
# nu4 = 0
# nu5 = 0
# nu6 = 0
# nu7 = 0
# nu8 = 0
# nu9 = 0
# nu10 = 0
# n = 0
#
# skudb = db.opensku_product_stock
# for id in productList:
#     results = skudb.find({"product_id":id})
#     for stocks in results:
#         for stock in stocks['stock']:
#             quantity = stock['quantity']
#             if quantity <=100:
#                 nu1 += 1
#             elif 300 >= quantity > 100:
#                 nu2 += 1
#             elif 600 >= quantity > 300:
#                 nu3 += 1
#             elif 1000 >= quantity > 600:
#                 nu4 += 1
#             elif quantity > 1000:
#                 nu5 += 1
#             n += 1
# print("一共查询了%s个sku,sku库存分布:" %n)
# print("库存小于100的考拉sku有%s个"%nu1)
# print("库存在100到300的考拉sku有%s个"%nu2)
# print("库存在300到600的考拉sku有%s个"%nu3)
# print("库存在600到1000的考拉sku有%s个"%nu4)
# print("库存大于1000的考拉sku有%s个"%nu5)
# d.close()



