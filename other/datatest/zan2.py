from mysql.producedb import Pydb
import requests
a = Pydb("intbee")
cursor = a.dodb()
sql = 'SELECT * FROM intbee_activity_cpm WHERE  manufacture_uuid !="58a27a340006f99e7cb43086" and plan_open_group_url !="";'
cursor.execute(sql)
results = cursor.fetchall()

for re in results:

    sql1 = 'SELECT * FROM intbee_user WHERE uuid="%s";' % re['manufacture_uuid']
    cursor.execute(sql1)
    us = cursor.fetchone()
    mobile = us['mobile']

    url = "https://api.intbee.com/api/uc/auth/login"

    payload = {"mobile":mobile,"verify_code":"6666a"}
    headers = {
        'Content-Type': "application/json",
        'app_id': "101"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    access_token = response.json()['result']['access_token']
    print(access_token)

    url =  "https://merchant.intbee.com/fapi/v4/activity/openGroupMsg/" + str(re['card_id']) + '/' + str(re['spread_uuid']) + '/1'
    payload = ""
    headers = {
        'access_token': access_token,
        'Postman-Token': "2882ee32-35c8-4f0b-9851-8c1ef0c985b4"
    }

    response = requests.request("GET", url, data=payload, headers=headers)
    print(response.json())


print("cpm执行完成")




sql = 'SELECT * FROM intbee4_activity_plan_open_group WHERE manufacture_uuid !="58a27a340006f99e7cb43086"  and plan_open_group_url !="";'
cursor.execute(sql)
results = cursor.fetchall()

for re in results:

    sql1 = 'SELECT * FROM intbee_user WHERE uuid="%s";' % re['manufacture_uuid']
    cursor.execute(sql1)
    us = cursor.fetchone()
    mobile = us['mobile']

    url = "https://api.intbee.com/api/uc/auth/login"

    payload = {"mobile":mobile,"verify_code":"6666a"}
    headers = {
        'Content-Type': "application/json",
        'app_id': "101",
        'Postman-Token': "0a448adb-fc0b-4d0f-9960-315ecb75d634"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    access_token = response.json()['result']['access_token']
    print(access_token)

    url =  "https://merchant.intbee.com/fapi/v4/activity/openGroupMsg/" + str(re['card_id']) + '/' + str(re['spread_uuid']) + '/1'
    payload = ""
    headers = {
        'access_token': access_token,
        'Postman-Token': "2882ee32-35c8-4f0b-9851-8c1ef0c985b4"
    }

    response = requests.request("GET", url, data=payload, headers=headers)
    print(response.json())


print("测品执行完成")

a.close()



