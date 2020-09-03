
#测试迁移测试
from mysql.pymysql_db import Connectmysql
con = Connectmysql("intbee")

sql = 'SELECT *  from intbee_card where create_time<= "2016-12-04 15:48:11"'
data = con.fetchall(sql)

for i in data:
    sql = 'SELECT * from intbee_task_info where id = {0}'.format(i['id'])
    data2 = con.fetchone(sql)


    if i['manufacture_uuid'] == data2['manufacture_uuid'] and i['card_no']== data2['task_no']\
        and i['card_type'] == data2['task_type'] and  i['product_id'] == data2['product_id'] and i['product_name'] == data2['name']\
        and i['create_time'] == data2['create_time'] and i['update_time'] ==  data2['update_time'] and i['terminate_category'] == data2['terminate_category'] \
        and i['terminate_reason'] == data2['terminate_reason'] and i['rsync_type'] == data2['rsync_type'] and i['status'] == data2['status']:
        pass
    else:
        print("数据有误%s"%(i['id']))

    if i['card_status'] == 0 and data2['mode_tags'] == 'cps':
        if i['task_status'] == 1:
            pass
        else:
            print("数据有误card_status%s" % (i['id']))
    else:
        assert i['card_status'] == data2['task_status']

    sql3 = 'select * from intbee4_card_plan_open_group where  card_id={0}'.format(i['id'])
    data3 = con.fetchone(sql3)

    sql4 = 'select * from intbee_card_cpm where  card_id={0}'.format(i['id'])
    data4 = con.fetchone(sql3)


    sql6 = 'select * from intbee_task_cpm where  task_id={0}'.format(i['id'])
    data6 = con.fetchone(sql6)


    if data3 == None and data4 == None:
        if data2['mode_tags'] == 'cps' and data2['end_time'] == None:
           pass
        else:
            print("mode_tags数据有误%s"%(i['id']))

    elif data3 != None and data4 == None:
        if data2['mode_tags'] == 'cps,cpp' and data2['end_time'] == data3['end_time'] and data6['user_limit'] == data3['user_limit'] and data6['reward_amount'] == data3['reward_amount']\
            and data6['create_time'] == data3['create_time'] and data3['card_status'] == data2['task_status']:
           pass
        else:
            print("mode_tags数据有误%s"%(i['id']))
    elif data3 == None and data4 != None:
        if data2['mode_tags'] == 'cps,cpm' and data2['end_time'] == data4['end_time'] and data6['user_limit'] == data4['user_limit'] and data6['reward_amount'] == data4['reward_amount']\
            and data6['create_time'] == data4['create_time'] and data4['card_status'] == data2['task_status']:
           pass
        else:
            print("mode_tags数据有误%s" % (i['id']))

    else:
        if data2['mode_tags'] == 'cps,cpp,cpm' and data2['end_time'] == data3['end_time'] and data6['user_limit'] == data4['user_limit'] and data6['reward_amount'] == data4['reward_amount']\
            and data6['create_time'] == data4['create_time'] and data4['card_status'] == data2['task_status']:
           pass
        else:
            print("mode_tags数据有误%s" % (i['id']))

    sql4 = 'select * from intbee_task_cps where task_id={0}'.format(i['id'])
    data4 = con.fetchone(sql4)
    if float(str(data4['reward_amount'])) == float(str(i['reward_amount'])) and  float(str(data4['reward_vip_amount'])) == float(str(i['reward_vip_amount'])) and \
        data4['status'] == i['status'] and data4['create_time'] == i['create_time']  and data4['update_time'] == data4['update_time']:
        pass
    else:
        print("intbee_task_cps数据有误%s" % (i['id']))

print("执行成功")



