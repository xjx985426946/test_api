# from common.excle import Excel
# from mysql.producedb import Mongodb
# import requests
# from common.logger import Log
#
# ex = Excel("11.1.xlsx")
# datas = ex.getData(sheetName="Sheet1")
#
# d = Mongodb("admin")
# client = d.get_mongodb_client()
#
# db = client.opensku
# collection = db.opensku_product_stock
#
# #登录用户：
#
# l = 'https://api.intbee.com/api/uc/auth/login'
# d =  {
# 	"mobile": "13902872836",
#     "password": "516ebb62b31164372fce7425ab6febb5"
#  }
#
# heade = {
#     'app_id': "101",
#     }
#
# response = requests.request("POST", l, json=d, headers=heade)
# access_token = response.json()['result']['access_token']
# print(access_token)
#
# headers = {
#     'app_id': "101",
#     'access_token': access_token
#     }
#
# url = 'https://api.intbee.com/fapi/card/create'
#
# for data in datas:
#
#     #查询商品id
#     results = collection.find({"stock.sku": data['商品sku编号']})
#
#     for result in results:
#         Log().info(result['product_id'])
#         param1 = {
#             "card_type": 1,
#             "kind_cpm": {
#                 "reward_amount": 60,
#                 "user_limit": 30
#             },
#             "product_id": result['product_id'],
#             "reward_amount": float(str(data['佣金']).split(',')[0][1:]),
#             "reward_vip_amount":float(str(data['佣金']).split(',')[0][1:])
#         }
#
#         response1 = requests.request("POST", url, data=param1, headers=headers)
#
#         print("创建60cpm---",response1.json())
#
#
#
#         param2 = {
#             "card_type": 1,
#             "kind_cpm": {
#                 "reward_amount": 80,
#                 "user_limit": 30
#             },
#             "product_id": result['product_id'],
#             "reward_amount": float(str(data['佣金']).split(',')[0][1:]),
#             "reward_vip_amount": float(str(data['佣金']).split(',')[0][1:])
#         }
#
#         response2 = requests.request("POST", url, data=param2, headers=headers)
#
#         print("创建80cpm---", response2.json())
#
#         param3 = {
#             "card_type": 1,
#             "kind_cpm": {
#                 "reward_amount": 150,
#                 "user_limit": 30
#             },
#             "product_id": result['product_id'],
#             "reward_amount": float(str(data['佣金']).split(',')[0][1:]),
#             "reward_vip_amount": float(str(data['佣金']).split(',')[0][1:])
#         }
#
#         response3 = requests.request("POST", url, data=param3, headers=headers)
#
#         print("创建150cpm---", response3.json())
#
#         param4 = {
#             "card_type": 1,
#             "kind_cpm": {
#                 "reward_amount": 300,
#                 "user_limit": 30
#             },
#             "product_id": result['product_id'],
#             "reward_amount": float(str(data['佣金']).split(',')[0][1:]),
#             "reward_vip_amount": float(str(data['佣金']).split(',')[0][1:])
#         }
#
#         response4= requests.request("POST", url, data=param4, headers=headers)
#
#         print("创建300cpm---", response4.json())
#
#         param5 = {
#             "card_type": 1,
#             "kind_cpm": {
#                 "reward_amount": 500,
#                 "user_limit": 30
#             },
#             "product_id": result['product_id'],
#             "reward_amount": float(str(data['佣金']).split(',')[0][1:]),
#             "reward_vip_amount": float(str(data['佣金']).split(',')[0][1:])
#         }
#
#         response5 = requests.request("POST", url, data=param5, headers=headers)
#
#         print("创建500cpm---", response5.json())
#
#
# print("所有任务创建成功")
# d.close()