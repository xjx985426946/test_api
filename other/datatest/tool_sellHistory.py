# intbee_sell_history 字段补全


from mysql.new import Mongodb,Pydb


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
#
#
a = Pydb("intbee")
cursor = a.dodb()



# 1、已收货的数据的结算状态修改  验证执行结果 ship_status=2（已确认收货）的状态  settle_status都置为1（可结算）
"""
sql ='SELECT * FROM intbee_sell_history where ship_status=2 and settle_status = 0;'
cursor.execute(sql)
results = cursor.fetchall()
for re in results:
    if re['settle_status'] == 1:
        pass
    else:
        print("已收货的数据的结算状态修改失败,卡号为%s" %(re['order_no']))

此数据测试通过
"""
# #  2、验证支付手续费  2019-02-01之前的阿里支付支付手续费为 buyer_pay_amount（实付金额） * 0.0055


# sql ='SELECT * from intbee_sell_history  where pay_channel like "alipay%" and pay_status>1 and pay_time < str_to_date("2019-02-01", "%Y-%m-%d %H");'
#
# cursor.execute(sql)
# results = cursor.fetchall()
# n = 0
# for re in results:
#     if float(re['pay_service_amount']) == round(float(re['buyer_pay_amount']) * 0.0055,2):
#         pass
#     else:
#         print("2019-02-01之前的阿里支付支付手续费修改失败,卡号为%s" %(re['order_no']))
#         print(float(re['pay_service_amount']), round(float(re['buyer_pay_amount']) * 0.0055,2))
#
#         n += 1
# print(n)

#此数据测试通过


#  3、验证支付手续费  2019-02-01之后的阿里支付支付手续费为 buyer_pay_amount（实付金额） * 0.006
"""
sql ='SELECT * from intbee_sell_history  where pay_channel like "alipay%" and pay_status>1 and pay_time > str_to_date("2019-02-01", "%Y-%m-%d %H");'

cursor.execute(sql)
results = cursor.fetchall()
for re in results:
    if float(re['pay_service_amount']) == round(float(re['buyer_pay_amount']) * 0.006,2):
        pass
    else:
        print("2019-02-01之后的阿里支付支付手续费修改失败,卡号为%s" %(re['order_no']))
        print(float(re['pay_service_amount']), round(float(re['buyer_pay_amount']) * 0.006,2))
此数据测试通过
"""


#  4、验证支付手续费  微信支付手续费为 buyer_pay_amount * 0.006
"""
sql ='SELECT * from intbee_sell_history where pay_channel like "wx%" and pay_status>1;'

cursor.execute(sql)
results = cursor.fetchall()
for re in results:
    if float(re['pay_service_amount']) == round(float(re['buyer_pay_amount']) * 0.006,2):
        pass
    else:
        print("2019-02-01之后的阿里支付支付手续费修改失败,卡号为%s" %(re['order_no']))
        print(float(re['pay_service_amount']),round(float(re['buyer_pay_amount']) * 0.006,2))
此数据测试通过
"""

# 5、 退款（微信退款 会退手续费，支付宝不会），验证微信退款中和已退款的数据 已退款完成状态才会有退手续费
"""
sql = 'SELECT * from intbee_sell_history where pay_channel like "wx%" and pay_status = 4 ;'
cursor.execute(sql)
results = cursor.fetchall()
for re in results:
    if re['refund_pay_service_amount'] == re['pay_service_amount']:
        pass
    else:
        print("微信退款手续费不正常,卡号为%s" %(re['order_no']))
        print(re['refund_pay_service_amount'],re['pay_service_amount'])

sql = 'SELECT * from intbee_sell_history where pay_channel not like "wx%" or pay_status != 4 ;'
cursor.execute(sql)
results = cursor.fetchall()
for re in results:
    if float(re['refund_pay_service_amount']) == 0.00:
        print(re['refund_pay_service_amount'])
        pass
    else:
        print("微信退款手续费不正常,卡号为%s" %(re['order_no']))
        print(re['refund_pay_service_amount'])
此数据测试通过
"""

# #支付渠道手续费实付
"""
sql = 'SELECT * from intbee_sell_history ;'
cursor.execute(sql)
results = cursor.fetchall()
for re in results:
    if re['pay_status'] == 2 or re['pay_status'] == 4:
        if float(re['real_pay_service_amount']) == float(re['pay_service_amount'] - re['refund_pay_service_amount']):
            pass
        else:
            print("支付渠道手续费实付不正常,卡号为%s" %(re['order_no']))
    else:
        if  float(re['real_pay_service_amount']) == 0.00:
            pass
        else:
            print("支付渠道手续费实付不正常,卡号为%s" % (re['order_no']))
此数据测试通过
"""

#退款字段设置改成0

"""
sql = 'SELECT * from intbee_sell_history  where pay_status in(2,3,5);'

cursor.execute(sql)
results = cursor.fetchall()
for re in results:
    if float(re['refund_income']) == 0.00 and float(re['refund_sell_fee']) == 0.00 and float(re['refund_sell_expend'])==0.00 and float(re['refund_spread_fee'])==0.00:
       pass
    else:

        print("退款字段设置改成0失败,卡号为%s" % (re['order_no']))
此数据测试通过
"""


# V、F 、平台实际收入 数据处理
"""
sql = 'SELECT * from intbee_sell_history where pay_status>1 ;'

cursor.execute(sql)
results = cursor.fetchall()
for re in results:
    if re['real_sell'] == re['sell_income']-re['sell_fee'] - re['sell_expend'] - re['refund_income'] + re['refund_sell_fee'] + re['refund_sell_expend'] \
            and re['real_spread'] == re['sell_expend'] - re['refund_sell_expend'] and re['real_platform'] == re['sell_fee'] - re['refund_sell_fee']:
       pass
    else:

        print("平台实际收入失败,卡号为%s" % (re['order_no']))
此数据测试通过      
"""

# #个税计算

'''
sql = 'SELECT * from intbee_sell_history ;'
cursor.execute(sql)
results = cursor.fetchall()
for re in results:
    if re['pay_status'] != 4:
        if float(re['individual_tax']) == round(float(re['sell_expend']) * 0.0466,2):

            pass
        else:
            print("个税计算失败,卡号为%s" % (re['order_no']))

    else:

        if float(re['individual_tax']) == 0.00:
            pass
        else:
            print("个税计算失败,卡号为%s" % (re['order_no']))
此数据测试通过
'''

# #个税计算

# sql = 'SELECT * from intbee_sell_history where pay_status>1;'
# cursor.execute(sql)
# results = cursor.fetchall()
# for re in results:
#     if re['real_spread'] == re['sell_expend'] - re['refund_sell_expend'] - re['individual_tax']:
#         pass
#     else:
#         print("个税计算失败,卡号为%s" % (re['order_no']))
# # 此数据测试通过
#
# a.close()




#1、测试点 购买商品时，信息individual_tax字段 根据规则算出值，退款时，要被还原为0
# 微信退款会生成 refund_pay_service_amount字段值，支付宝不会  成功退款的时候，申请中 或者退货中 不会生成这个值