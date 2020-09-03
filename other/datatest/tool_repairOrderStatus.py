from mysql.my import Mongodb,Pydb

d = Mongodb("opensku")
client = d.get_mongodb_client()

db = client.opensku
collection = db.opensku_order



a = Pydb("intbee")
cursor = a.dodb()



'''
取消订单，订单状态不一致问题
'''
result = collection.find({'order_status':"10"})
num = 0
for i in result:
    sql = 'SELECT pay_status FROM  intbee_sell_history WHERE order_no={0};'.format(i['order_no'])
    cursor.execute(sql)
    results = cursor.fetchall()

    for re in results:
       # print(re[0])
        if re[0] == 0:
            print(i['order_no'])
            num += 1
print("订单状态错误的订单有%s笔"%(num))


'''
收货订单，状态不一致问题
'''

result = collection.find({'order_status':"27"})
num = 0
for i in result:
    sql = 'SELECT ship_status FROM  intbee_sell_history WHERE order_no={0};'.format(i['order_no'])
    cursor.execute(sql)
    results = cursor.fetchall()

    for re in results:
       # print(re[0])
        if re[0] == 2:
            print(i['order_no'])
            num += 1
print("订单状态错误的订单有%s笔"%(num))

a.close()
d.close()