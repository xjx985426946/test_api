
#财务数据测试
from mysql.my import Pydb
a = Pydb("paycenter")
cursor = a.dodb()

sql ='SELECT sum(sell_income) FROM intbee.intbee_sell_history WHERE pay_status >= 2 AND merchant_no is null  AND length(pay_channel)=0;'
cursor.execute(sql)
results = cursor.fetchall()
for num in results:
    print("计算支付方式和商户号未知的订单总额为:%s"%(num[0]))


sql ='SELECT count(*) FROM intbee.intbee_sell_history WHERE pay_status >= 2 AND merchant_no is null  AND length(pay_channel)=0;'
cursor.execute(sql)
results = cursor.fetchall()
for num in results:
    print("计算支付方式和商户号未知的订单量:%s"%(num[0]))



sql ='SELECT COUNT(*) FROM pay_center_wx_sync_notify;'
cursor.execute(sql)
results = cursor.fetchall()

sql ='SELECT COUNT(*) FROM pay_center_ali_sync_notify;'
cursor.execute(sql)
results2 = cursor.fetchall()
print("旧支付中心的数量一一共有%s条" %(results[0][0] + results2[0][0]))





# 查询新支付中心表 支付方式和商户号未知的订单量在旧支付中心表可以找到订单号的数据

sql ='SELECT order_no FROM intbee.intbee_sell_history WHERE pay_status >= 2 AND merchant_no is null  AND length(pay_channel)=0;'
cursor.execute(sql)
results = cursor.fetchall()
L = []
for num in results:
    L.append(num[0])

print(len(L))

for i in L:
    sql ='SELECT * FROM pay_center_wx_sync_notify WHERE out_trade_no={0};'.format(i)
    cursor.execute(sql)
    results = cursor.fetchall()
    if results != ():
        # print("找到数据")
        pass
    elif results == ():
        sql = 'SELECT * FROM pay_center_ali_sync_notify WHERE out_trade_no={0};'.format(i)
        cursor.execute(sql)
        results2 = cursor.fetchall()
        if results2 == ():
            print("旧的订单没有找到数据%s"%(i))
        else:
            pass
a.close()

from common.logger import Log
log = Log()
sql ='SELECT order_no FROM intbee.intbee_sell_history WHERE pay_status >= 2 AND merchant_no is null  AND length(pay_channel)=0;'
cursor.execute(sql)
results = cursor.fetchall()
for num in results:
    # print("计算支付方式和商户号未知的订单号:%s"%(num))
    log.info(num)
print("完成")



sql ='SELECT * FROM pay_center_pay_history;'
cursor.execute(sql)
results = cursor.fetchall()
L = []
for i in results:
    L.append(i[2])

sql ='SELECT merchant_no FROM intbee.intbee_sell_history;'
cursor.execute(sql)
results = cursor.fetchall()
L2 = []
for i in results:
    L2.append(i[0])


d = [False for c in L if c not in L2]
if d:
  print ("商户号有的不存在")
else:
  print ("商户号都存在")

a.close()


from mysql.new import Pydb
db  = Pydb("intbee")
cursor2 = db.dodb()
sql ='SELECT * FROM intbee_sell_bill_corporate;'
cursor2.execute(sql)
results = cursor2.fetchall()
for result in results:
    if  result['sell_profit'] == result['sell_income'] -result['refund_income'] - (result['sell_fee'] - result['refund_sell_fee']) - (result['sell_expend'] - result['refund_sell_expend']) and  result['receivable_sell'] == result['sell_profit']\
            and result['balance'] == result['sell_profit'] - result['receivable_sell']:
        pass
    else:
        print("数据不正确%s" %(result['corporate_uuid']))
        print("id%s"%(result['id']))
        print(result['sell_profit'],result['sell_income'] -result['refund_income'] - (result['sell_fee'] - result['refund_sell_fee']) - (result['sell_expend'] - result['refund_sell_expend']))
        print( result['receivable_sell'],result['sell_profit'])


sql ='SELECT * FROM intbee_sell_bill_spread;'
cursor2.execute(sql)
results = cursor2.fetchall()
for result in results:
    if result['receivable_spread'] == result['spread_profit']  and  result['balance'] == result['receivable_spread'] - result['spread_profit']:
        pass
    else:
        print("数据不正确%s" %(result['spread_uuid']))
        print("id%s"%(result['id']))
        print(result['receivable_spread'],result['spread_profit'])
        print( result['balance'],result['receivable_spread'] - result['spread_profit'])


db.close()

