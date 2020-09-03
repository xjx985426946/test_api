# from common.excle import Excel
# from mysql.producedb import Mongodb,Pydb
# import requests
# from common.logger import Log
#
# ex = Excel("22.xlsx")
# datas = ex.getData(sheetName="Sheet1")
#
#
#
#
#
#
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
#
# headers = {
#     'app_id': "101",
#     'access_token': access_token
# }
#
#
# for i in datas:
#
#     url = 'https://api.intbee.com/fapi/user/task/pay'
#     param = {
#         "order_no": i['order_no'],
#         "pay_channel": 'YuE',
#     }
#
#     response4 = requests.request("POST", url, json=param, headers=headers)
#
#     print("支付成功---", response4.json())
#     # print( i['order_no'])
#
# print("执行成功")