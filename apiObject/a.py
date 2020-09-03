# import requests
#
# url = "https://test-www.intbee.com/auth/signin/customer"
#
# payload = "{\n\t\"mobile\": \"13729542194\",\n\t\"password\": \"e10adc3949ba59abbe56e057f20f883e\"\n}"
# headers = {
#     'Content-Type': "application/json",
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# print(response.cookies)


# d = open("../conf/config.py",encoding="utf-8")
# print(d.read())

# with open("../conf/config.py",'w',encoding="utf-8") as f:
#     d = 'url = "http://api.intbee.com"' + "\n" + \
#         'url_f = "https://111"'
#
#     f.write(d)

#
# import urllib.parse
# test = "深圳测试"
# print(test)
# new = urllib.parse.quote('中文')
# print(new)
# print(urllib.parse.unquote('%E4%B8%8A%E6%B5%B7%E5%B8%82'))

# md5加密
# import hashlib
# m = hashlib.md5()
# m.update('123456'.encode(encoding="utf-8"))
# print(m.hexdigest())
#
# import base64
# s1 = base64.encodestring('hello world')
# s2 = base64.decodestring(s1)
# print (s1, s2)

# from common.httprequest import HttpRquest
# from conf import config
# from common.logger import Log
# import  os,json
# from common.readyaml import read_yaml
# from conf import read_path
# import pytest
# from apiObject.setupApi import SetupApi
# from common.save_value import SaveValue
# from common.logger import Log
# import os,sys


#
# token = 11
#

# test_data = read_yaml(read_path.test_homepage_data, 'test_accepton.yaml', config.url, token)



# result  =[1,2,2,6,9,8]
# ls = []
# for i in result:
#     ls.append(i)
# result = sorted(result,reverse=True)
# print(result)
# print(ls)
# assert result == ls

# from apiObject.setupApi import SetupApi
#
#
# import requests
#
# url = "https://merchant.intbee.com/store/frontend/order/profile/within"
#
# querystring = {"t":1542599451803,"begin":1539532800000,"end":1539619199999}
#
# headers = {
#     'Content-Type': 'application/json'
#
#     }
# cookies = SetupApi().login_f("13902879682","25d55ad283aa400af464c76d713c07ad")
# print(cookies)
#
# response = requests.get(url, headers=headers, params=querystring, cookies=cookies)
#
# print(response.text)


# from apiObject import b
# print(b.g())

# b = '<form name="punchout_form" method="post" action="https://openapi.alipay.com/gateway.do?charset=UTF-8&method=alipay.trade.wap.pay&sign=aPCMC7hspd%2FJZFPxpTWikbBaxArStnAJ%2FLNH9KzhaucfFgO2jc7V9E8CpqlnZPJorPyFQw3kDpxCf0%2Fe6c78GBPPGV8f5EpGbXMWrAbXPPWyoETftxhTKi%2F1c75w1JogSHFesKJ8fEE9XrkMCzwuOAVZRT94j182zOkDM%2FOOE0E%3D&return_url=http%3A%2F%2Ftest-www.intbee.com%2Fapp%2Ffinance%2Fpersonal&notify_url=http%3A%2F%2Ftest-pay.intbee.com%2Fpublic%2Fpay%2Falipay%2Fnotify%2Fv2&version=1.0&app_id=2016052401436400&sign_type=RSA&timestamp=2018-11-21+14%3A42%3A52&alipay_sdk=alipay-sdk-java-dynamicVersionNo&format=json"><input type="hidden" name="biz_content" value="{&quot;out_trade_no&quot;:&quot;112018112114425297111380&quot;,&quot;product_code&quot;:&quot;INTBEE_WAP_PAY&quot;,&quot;seller_id&quot;:&quot;2088221861486600&quot;,&quot;subject&quot;:&quot;充值智蜂&quot;,&quot;total_amount&quot;:&quot;10.00&quot;}"><input type="submit" value="立即支付" style="display:none" ></form><script>document.forms[0].submit();</script>'
# # c = 'https://openapi.alipay.com/gateway'
# # if c in b:
# #     print(1)
# # else:
# #     print(2)

# import yaml
#
# yaml_data = open("procedure.yaml", encoding="utf-8")
# test_data = yaml.load(yaml_data)
# print(test_data)
# 'https://test-www.intbee.com/store/frontend/product'


# import requests
#
# url = "https://test-item.intbee.com/frontend/customers/address/default"
#
# payload = "{\"id\":\"34374\"}"
# headers = {
#     'Content-Type': "application/json",
#     'access_token': "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOm51bGwsImF1ZCI6IjEwMSIsInN1YiI6IjVjMjE5N2YwZGMwZTgyMDAwNTkwNmI0MyIsImFwcGlkIjoiMTAxIiwiZXhwIjoxNTQ2MzM3MzE2LCJqdGkiOiJfeFJ5dV91S0RRYmF5WUhoOEtjOEpnIiwiaWF0IjoxNTQ1NzMyNTE2fQ.dO9bAbyD5TtgzjV6a0ay_2_7GHE8BXsY5uqnGOndwJ4",
#     'Cache-Control': "no-cache",
#     'Postman-Token': "614232c9-debb-41f0-b5fe-ab5cb50f7b1c"
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# print(response.text)


# import requests
#
# url = "http://test-api.intbee.com/opensku/v1/merchant/postage"
# payload = {
#     "calculate_way": 1,
#     "name": "模版名称",
#     "delivery_way": {
#         "name": "运输方式名称",
#         "postage": "100",
#         "plus": "10",
#         "postageplus": "10.00",
#         "rule_list": {
#             "postage": "100",
#             "plus": "10",
#             "postageplus": "10",
#             "province": {
#                 "code": "code",
#                 "name": "省名称",
#                 "city_code": [101, 102]
#             }
#         }
#     }
#
# }
# headers = {
#     'Content-Type': "application/json",
#     'access_token': "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJvcGVuc2t1IiwiYXVkIjoiZDFlYzk0Yjc5OWM5MWIzYWNmOTk3YjM4NzFkYjU3OGMiLCJzdWIiOiIyIiwiYXBwaWQiOiJkMWVjOTRiNzk5YzkxYjNhY2Y5OTdiMzg3MWRiNTc4YyIsImV4cCI6MTU0ODk4OTMyMSwianRpIjoiRHg1ZEZRMXNYbTh2R0FsX09rcEF1dyIsImlhdCI6MTU0NjM5NzMyMX0.Grezmt39H7JAVb8Gax8DnADZeNX25874GsEXp7zIK8o",
#     'Postman-Token': "5504cbf5-20c7-4dfe-950b-e1ddbc4747ec"
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# print(response.text)
# import base64
# a = "intbee-api:fw41Vhz7V68IduaF7EA1Cg=="
# uft_str = a.encode("iso-8859-1")
# b = base64.b64encode(uft_str)
# print(b)


# import requests
#
# url = "http://192.168.3.21:9999/api/trade/payment/pay"
#
# payload = "{\n  \"amount\": 1,\n  \"app_id\": \"101\",\n  \"channel\": \"alipay_qr\",\n  \"order_no\": 1546851998000,\n  \"subject\": \"test\",\n  \"client_ip\":\"111\"\n}"
# headers = {
#     'Content-Type': "application/json",
#     'access_token': "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOm51bGwsImF1ZCI6IjEwMSIsInN1YiI6IjViY2RhYWVmOWExZDA5MDAwN2EwNTA1YSIsImFwcGlkIjoiMTAxIiwiZXhwIjoxNTQ3NDU2NTQyLCJqdGkiOiJPb0M4bTF2cEhITUxIRi1QN1VXTTB3IiwiaWF0IjoxNTQ2ODUxNzQyfQ.BPCHY4YxquP_dqPkHivTiEAdNjRn-kdRlVB1xFYA5_I",
#     'Postman-Token': "362a364e-a0ec-490e-9004-2e8b5748f5af"
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# print(response.text)





# import requests
#
# url = "http:/test-kaola.intbee.com/v1/kaola/order/orderconfirm"
#
# payload = "{"orderItemList":[{\n\t"goodsId\":\"1597463\",\n\t\t\t\"skuId\":\"2\",\n\t\t\t\"buyAmount\":1,\n\t\t\t\"channelSalePrice\":49.00\n\t\t}\n\t\t],\n\t\t\"userInfo\":{\n\t\t\t\"accountId\":\"123\",\n\t\t\t\"name\":\"112\",\n\t\t\t\"mobile\":\"13729542194\",\n\t\t\t\"provinceName\":\"1223\",\n\t\t\t\"cityName\":\"123\",\n\t\t\t\"districtName\":\"223\",\n\t\t\t\"address\":\"3455\"\n\t\t}\n\t\t\n}"
# headers = {
#     'Content-Type': "application/json",
#     'Postman-Token': "75a02d74-de9c-4e5c-8059-b657e5fea2d2"
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# print(response.text)


# def fun(a):
#     num = 0
#     dic = {}
#     for i in a:
#         dic[num] = i
#         num += 1
#     return dic
#
# a = [1,2,34,5464]
# r = fun(a)
# print(r)
# d = [2,6,8,9]
# for i in d:
#     print(d.index(i))


# 定时器
# import threading,time
# def fun_timer():
#     print('Hello Timer!')
#     global timer
#     timer = threading.Timer(3, fun_timer)
#     timer.start()
#
# timer = threading.Timer(1, fun_timer)
# timer.start()
# time.sleep(30) # 15秒后停止定时器
# timer.cancel()



# import datetime
# # now = datetime.datetime.now()
# # print(now.hour)
# # print(now.minute)
#
# import time
# def doSth():
#
#     print('test')
#     # 假装做这件事情需要一分钟
#     time.sleep(60)
#
# def main(h=17, m=56):
#     '''h表示设定的小时，m为设定的分钟'''
#     while True:
#         # 判断是否达到设定时间，例如0:00
#         while True:
#             now = datetime.datetime.now()
#             # 到达设定时间，结束内循环
#             if now.hour == h and now.minute == m:
#                 break
#                 # 不到时间就等20秒之后再次检测
#             time.sleep(20)
#         # 做正事，一天做一次
#         doSth()
# main()



# class People:
#
#     def __init__(self,name):
#
#         self.name=name
#
#     def eat(self):
#
#         print("%s he/she is eating" %(self.name))
#
#     def sleep(self):
#
#         print("sleeping")
#
# class Man(People):
#
#     def __init__(self,name,age):#重写构造函数
#
#     #People.__init__(self,name)
#
#         super(Man,self).__init__(name)#重写构造函数 更方便的一种方式  新式类的写法
#
#         self.age=age
#
#         print("男人比女人有钱")
#
#     def strong(self):
#
#         print("a man who is strong")
#
# class Woman(People):
#
#     def beautiful(self):
#
#         print("a  woman who is beautiful")
#
#     def sleep(self):#重写父类方法
#
#             print("wuman sleep before man")
#
# man=Man("chenxiaoming","56")
#
# man.eat()

# woman=Woman("chenxiaohua")
#
# woman.sleep()


#登录装饰器
# import json
# from common.logger import Log
# # def auth(func):
# #     def inner():
# #         try:
# #             func()
# #         except AssertionError as e:  # 抛出断言错误异常
# #             print("成功写入日志")
# #             raise e
# #         finally:
# #             print("返回结果：".center(66, "-"))
# #     return inner
#
# def auth(func):
#     def inner(something,*args,**kwargs):
#         try:
#             result = func(something)
#             print(result)
#             # Log().info("测试通过")
#         except AssertionError as e:  # 抛出断言错误异常
#             # Log().error("断言结果为False~{0}".format(e))
#             raise e
#         finally:
#             with open("1.txt", "a+", encoding="utf-8") as f:
#
#                 f.write(result)
#     return inner
#
#
# dics = "{'a': 1, 'b': 2}"
# @auth
# def fu(somthing):
#     # with open("1.txt","a+",encoding="utf-8") as f:
#     #     f.write("111")
#     try:
#         assert 1==2
#     except:
#         pass
#     return "666"
# fu("44")
# def te(user,*args,**kwargs):
#     print(user)
#     # print("args:", args)
#     # print("*args:", *args)
#     print("kwargs:",kwargs)
#     # print("**kwargs:",**kwargs)
#
# user = '1'
# lists = [1,2]
# dics = {'a':1,'b':2}
# te(user,**dics)
#
#
# import requests
#
# url = "https://test-api.intbee.com/store2/api/v1/authentication/pingxx/cache"
#
# headers = {
#     'access_token': "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOm51bGwsImF1ZCI6IjEwMSIsInN1YiI6IjViZWEyY2RmNzY2MzgzMDAwNmYxNDBjMiIsImFwcGlkIjoiMTAxIiwiZXhwIjoxNTUxMjYyNTcxLCJqdGkiOiJVR216QUsxOHprNW56a0NTRG5fVVRRIiwiaWF0IjoxNTUwNjU3NzcxfQ.oQ6PLtrGoW4VQf0GONZhXfriAwN0_fCSjCvmd4LfUe4",
#     'cache-control': "no-cache",
#     'postman-token': "0f229fd8-14c2-b487-615c-876b7ed10b26"
#     }
#
# response = requests.get("url", data=1, headers=headers)
#
# print(response.text)


#
# import time
#
# #将参数的时间替换为当前时间戳
# for i in test_data:
#     i['param']['t'] = int(round(time.time() * 1000))
#
#
# import datetime,time
# utime = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d %H:%M:%S")
# print(utime)
# stamp_array = time.strptime(utime, '%Y-%m-%d %H:%M:%S')
# stamp = int(time.mktime(stamp_array) * 1000)
# print(stamp)




# def tests(**kwargs):
#     if kwargs:
#         a = kwargs['product_id']
#         b = kwargs['card_id']
#         print(a+b)
#     else:
#         a = 1
#         b = 2
#         print(a+b)
# param = {'product_id':2,'card_id':6}
# tests(**param)
#
# import time
# print(round(time.time()))

# for num in range(0,707829217):
#     a=''
# #质数大于 1
#     if num > 1:
#         # 查看因子
#         for i in range(2, num):
#             if (num % i) == 0:
#                 # print(num, "不是质数")
#                 # print(i, "乘于", num // i, "是", num)
#                 break
#         else:
#             print(num, "是质数")
#             for num2 in range(0,707829217):
#                 if num2 > 1:
#                     # 查看因子
#                     for i in range(2, num2):
#                         if (num2 % i) == 0:
#                             break
#                     else:
#                         # print(num2, "是质数")
#                         if num * num2 == 707829217:
#                             print(num,num2)
#                             a = 'true'
#                             break
#                 if a == 'true':
#                     break
#
#     # 如果输入的数字小于或等于 1，不是质数
#     else:
#         # print(num, "不是质数")
#      pass


# print(499 * 0.0055)
# a = 2.744
# b = 2.745
# c = 2.746
# d = 1.265
# e = 12.650
# print(round(a,2))
# print(round(b,2))
# print(round(c,2))
# print(round(e,2))


# buyer_pay_amount = 230.00
# print(round(float(buyer_pay_amount) * 0.0055,2))
#1.23456
# print(round(float(230.00) * 0.0055,2))

# f = 1.245
# print('%.4f' % f)
# print('%.3f' % f)
# print('%.2f' % f)

# def dec(num,n):
#     num = str(float(num))
#     a = num.split('.')[-1]
#     if float(a[n])<5:
#         new = str(a[0:-1])
#     else:
#         new = str(int(a[0:-1]) + 1)
#
#     num = a[0] + '.' + new
#     return float(num)



# print(dec(0.01*0.0055,2))

# a = '$0.5'
# print((a[1:]))


# import hashlib
# sha1 = hashlib.sha1()
# sha1.update('1014&1002&SHA1&44555'.encode('utf-8'))
# print(sha1.hexdigest())
#
# import hashlib
#
# data =  'This a md5 test!'.encode('utf-8')
# sah1 = hashlib.sha1(data)
# print(sah1.hexdigest())


# result = 'success'
# def check_json(src_data, dst_data):
#     """
#     校验的json
#     :param src_data:  校验内容
#     :param dst_data:  接口返回的数据（被校验的内容
#     :return:
#     """
#     global result
#     try:
#         if isinstance(src_data, dict):
#             """若为dict格式"""
#             for key in src_data:
#                 if key not in dst_data:
#                     result = 'fail'
#                 else:
#                     if src_data[key] != dst_data[key]:
#                         result = False
#                     this_key = key
#                     """递归"""
#                     if isinstance(src_data[this_key], dict) and isinstance(dst_data[this_key], dict):
#                         check_json(src_data[this_key], dst_data[this_key])
#                     elif isinstance(type(src_data[this_key]), type(dst_data[this_key])):
#                         result = 'fail'
#                     else:
#                         pass
#             return result
#         return 'fail'
#
#     except Exception as e:
#         return 'fail'
#
# a = {
#   "code": 0,
#   "message": "SUCCESS",
#   "result": [
#     {
#       "name": "ISBN",
#       "not_null": True
#     },
#     {
#       "name": "出版社",
#       "not_null": False
#     },
#     {
#       "name": "定价",
#       "not_null": False
#     }
#   ]
# }
# b = {
#     "code": 0,
#     "message": "SUCCESS",
#     "result": [
#       {
#         "name": "ISBN",
#         "not_null": True
#       },
#       {
#         "name": "出版社",
#         "not_null": False
#       },
#     {
#       "name": "定价",
#       "not_null": False
#     }
#     ]
#   }
#
#
# print(check_json(b,a))



# import zlib
# # s=b"hello world,0000000000000000000000000000"
# # print (len(s))#输出 40
# # c=zlib.compress(s)
# # print (c)#输出22
# # d=zlib.decompress(c)
# # print (d)#
#
#
# import base64
# def encode(str):
#  compressed = zlib.compress(str)
#  compressed = b'("%08X" % len(str))' + compressed
#  return base64.b64encode(compressed)
#
# s=b"hello world,0000000000000000000000000000"
# print(encode(s))




# a = "哈哈"
#
#
# #字符串转换成字节
# b = bytes(a,encoding='utf-8')
# print(b)
# b1 = bytes(a,encoding='gbk')
# print(b1)
#
# #将字节转换成字符
#
# c=str(b,encoding='utf-8')
# print(c)
#
# c1=str(b1,encoding='gbk')
# print(c1)

# a = b'12/xs'
# c=str(a,encoding='utf-8')
# print(c)

























