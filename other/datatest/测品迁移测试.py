from mysql.pymysql_db import Connectmysql

con = Connectmysql("intbee")

sql = 'select * from intbee_card_plan_open_group'
datas = con.fetchall(sql)
for data in datas:
    sql1 = 'select * from intbee4_card_plan_open_group where card_id=%s'
    param =  [data['card_id']]
    re = con.fetchone(sql1,param)
    # print(data)
    # print(re)
    if data['card_no'] == re['card_no'] and data['create_time'] == re['create_time'] and data['update_time'] == re['update_time'] and data['status'] == re['status'] and re['user_limit'] == 0 \
            and float(str(re['deposit_amount'])) == 0.00 and re['begin_time'] == None and re['end_time'] == None:
        pass
    else:
        print("数据有误： ",data['id'])
    if data['used'] == 1:
        if re['card_status'] == 2:
            pass
        else:
            print("数据有误： ", data['id'])

    if data['used'] == 0:
        if re['card_status'] == 0:
            pass
        else:
            print("数据有误： ", data['id'])

print("验证完成")



# sql3 = 'SELECT * FROM intbee_activity_plan_open_group;'
# datas2 = con.fetchall(sql3)
# for data in datas2:
#     sql4 = 'select * from intbee4_activity_plan_open_group where card_id=%s'
#     param =  [data['card_id']]
#     re = con.fetchone(sql4,param)
#     print(data)
#     print(re)
#     if data['manufacture_id'] == re['manufacture_id'] and data['manufacture_uuid'] == re['manufacture_uuid'] and data['spread_id'] == re['spread_id'] and data['spread_uuid'] == re['spread_uuid']\
#         and data['card_no'] == re['card_no'] and data['plan_open_group_time'] == re['plan_open_group_time'] and data['plan_open_group_url'] == re['plan_open_group_url'] \
#         and data['platform_name'] == re['platform_name'] and data['platform_fans_count'] == re['platform_fans_count'] and data['apply_remark'] == re['apply_remark'] and data['name'] == re['name']\
#         and data['mobile'] == re['mobile'] and data['state'] == re['state'] and data['city'] == re['city'] and data['district'] == re['district']  and data['address'] == re['address'] \
#         and data['carrier_company'] == re['carrier_company'] and data['carrier_company_no'] == re['carrier_company_no'] and data['carrier_no'] == re['carrier_no'] \
#         and data['refuse_reason'] == re['refuse_reason']:
#         pass
#     else:
#         print("数据有误 " ,data['id'])
#
# SELECT
# g. *
# from intbee_card_plan_open_group as g
#
# JOIN
# intbee_card as c
# on
# g.card_no = c.card_no
# WHERE
# c.manufacture_uuid = "5b2a1535b0bcdf00088d7cea";
#
# SELECT * FROM
# intbee4_card_plan_open_group
# WHERE
# card_id in (167084, 167085);
# SELECT * FROM
# intbee_card
# WHERE
# card_no = "19-10000045-557";
#
# SELECT * FROM
# intbee_activity_plan_open_group
# WHERE
# card_id = 167084;
# SELECT * FROM
# intbee_activity_plan_open_group
# WHERE
# id = 105;
# SELECT * FROM
# intbee4_activity_plan_open_group
# WHERE
# card_id = 167092;
# SELECT *
# from intbee_card WHERE
#
# id = 167085;
# SELECT * FROM
# intbee_card_cpm
# WHERE
# card_id = 167085;
# SELECT *
# from intbee_activity_cpm WHERE
#
# card_id = 167085;
# SELECT * FROM
# intbee4_card_plan_open_group
# WHERE
# card_id = 167085;
# SELECT * FROM
# intbee4_activity_plan_open_group
# WHERE
# card_id = 167084;
# SELECT * FROM
# intbee_activity_deposit_order
# WHERE
# card_id = 167085;
# SELECT * FROM
# intbee_activity_deposit_order_refund
# WHERE
# card_id = 167085;
#
# SELECT * FROM
# intbee_bank_corporate
# WHERE
# uuid = "5b2a1535b0bcdf00088d7cea";
# SELECT * FROM
# intbee_bank_available_corporate_history
# WHERE
# uuid = '5b2a1535b0bcdf00088d7cea';
# SELECT * FROM
# intbee_bank_spread
# WHERE
# uuid = "5bea2cdf7663830006f140c2";
# SELECT * FROM
# intbee_bank_available_spread_history
# WHERE
# uuid = "5bea2cdf7663830006f140c2";
#
# --  apply_status = 1 and mobile != '' and carrier_no = ''
# then
# 5  # 提交地址，待发货
# SELECT * FROM
# intbee_activity_plan_open_group
# WHERE
# apply_status = 1 and mobile != '' and carrier_no = '';
# SELECT * FROM
# intbee4_activity_plan_open_group
# WHERE
# card_id = 167084;
#
# SELECT *
# from intbee_card WHERE
#
# id = 172252;
# SELECT * FROM
# intb
# SELECT *
# from intbee_card WHERE
#
# product_id = 181007;
# SELECT * FROM
# intbee_subcard
# WHERE
# card_id = 172252;
#
# SELECT * FROM
# intbee_card_cpm
# WHERE
# card_id = 172252;
# SELECT *
# from intbee_activity_cpm WHERE
#
# card_id = 172252;
# SELECT * FROM
# intbee4_card_plan_open_group
# WHERE
# card_id = 172252;
# SELECT * FROM
# intbee4_activity_plan_open_group
# WHERE
# card_id = 172252;
# SELECT * FROM
# intbee_activity_deposit_order
# WHERE
# card_id = 172252;
# SELECT * FROM
# intbee_activity_deposit_order_refund
# WHERE
# card_id = 172252;
#
# --  apply_status = 0
# then
# 3  # 待审核
# SELECT * FROM
# intbee_activity_plan_open_group
# WHERE
# card_id = 167086 and apply_status = 0;
# SELECT * FROM
# intbee4_activity_plan_open_group
# WHERE
# card_id = 167086;
#
# -- apply_status = 2
# then
# 20  # 审核不通过
# SELECT * FROM
# intbee_activity_plan_open_group
# WHERE
# apply_status = 2 and card_id = 167084;
# SELECT * FROM
# intbee4_activity_plan_open_group
# WHERE
# card_id = 167084;
#
# -- when
# apply_status = 1 and mobile = ''
# then
# 4  # 待提交地址
# SELECT * FROM
# intbee_activity_plan_open_group
# WHERE
# apply_status = 1 and mobile = '' and card_id = 167092;
# SELECT * FROM
# intbee4_activity_plan_open_group
# WHERE
# card_id = 167092;
#
# --  apply_status = 1 and mobile != '' and carrier_no = ''
# then
# 5  # 提交地址，待发货
# SELECT * FROM
# intbee_activity_plan_open_group
# WHERE
# apply_status = 1 and mobile != '' and carrier_no = '';
# SELECT * FROM
# intbee4_activity_plan_open_group
# WHERE
# card_id = 167084;
#
# -- apply_status = 1 and mobile != '' and carrier_no != '' and plan_open_group_url != ''
# then
# 8
# 提交开团地址，待验收
# SELECT * FROM
# intbee_activity_plan_open_group
# WHERE
# apply_status = 1 and mobile != '' and carrier_no != '' and plan_open_group_url != '' and card_id = 167092;
# SELECT * FROM
# intbee4_activity_plan_open_group
# WHERE
# card_id = 167092;
#
# -- apply_status = 1 and mobile != '' and carrier_no != '' and plan_open_group_url = '' and carrier_status = 0
# then
# 6  # 已发货，待确认收货
# SELECT * FROM
# intbee_activity_plan_open_group
# WHERE
# apply_status = 1 and mobile != '' and carrier_no != '' and plan_open_group_url = '' and carrier_status = 0 and card_id = 167085;
# SELECT * FROM
# intbee4_activity_plan_open_group
# WHERE
# card_id = 167085;
#
# -- apply_status = 1 and mobile != '' and carrier_no != '' and plan_open_group_url = '' and carrier_status = 3
# then
# 7
# SELECT * FROM
# intbee_activity_plan_open_group
# WHERE
# apply_status = 1 and mobile != '' and carrier_no != '' and plan_open_group_url = '' and carrier_status = 3 and card_id = 168853;
# SELECT * FROM
# intbee4_activity_plan_open_group
# WHERE
# card_id = 168853;