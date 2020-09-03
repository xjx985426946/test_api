from mysql.producedb import Pydb
import requests
import time
a = Pydb("intbee")
cursor = a.dodb()
sql = 'SELECT * FROM intbee_activity_cpm WHERE subcard_status>8  and manufacture_uuid="58a27a340006f99e7cb43086" and plan_open_group_url !="";'
cursor.execute(sql)
results = cursor.fetchall()
# print(results)
for re in results:

    # url = "https://merchant.intbee.com/fapi/v4/activity/openGroupMsg/49861/5c762e8546e0fb00062858a9/1"
    url =  "https://merchant.intbee.com/fapi/v4/activity/openGroupMsg/" + str(re['card_id']) + '/' + str(re['spread_uuid']) + '/1'
    payload = ""
    headers = {
        'access_token': "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOm51bGwsImF1ZCI6IjEwMSIsInN1YiI6IjU4YTI3YTM0MDAwNmY5OWU3Y2I0MzA4NiIsImFwcGlkIjoiMTAxIiwiZXhwIjoxNTc2MDM1OTYwLCJqdGkiOiJTbW5JdjVITXV5OEN3VEI3SDZ1YVN3IiwiaWF0IjoxNTc1NDMxMTYwLCJhdXRoX21vZGUiOiJtb2JpbGUiLCJhdXRoX2lkIjoiKzg2LTEzOTAyODcyODM2In0.833Qj45TiVchmCbYcikqCnxcx7InY4yB--Pz7jwYPiY",
        'Postman-Token': "2882ee32-35c8-4f0b-9851-8c1ef0c985b4"
    }

    response = requests.request("GET", url, data=payload, headers=headers)
    print(response.json())
    time.sleep(1)

print("cpm执行完成")


sql1 = 'SELECT * FROM intbee4_activity_plan_open_group WHERE  manufacture_uuid="58a27a340006f99e7cb43086"  and plan_open_group_url !="" ;'
cursor.execute(sql1)
results1 = cursor.fetchall()
for re1 in results1:

    # url = "https://merchant.intbee.com/fapi/v4/activity/openGroupMsg/49861/5c762e8546e0fb00062858a9/1"
    url1 =  "https://merchant.intbee.com/fapi/v4/activity/openGroupMsg/" + str(re1['card_id']) + '/' + str(re1['spread_uuid']) + '/1'
    payload = ""
    headers = {
        'access_token': "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOm51bGwsImF1ZCI6IjEwMSIsInN1YiI6IjU4YTI3YTM0MDAwNmY5OWU3Y2I0MzA4NiIsImFwcGlkIjoiMTAxIiwiZXhwIjoxNTc2MDM1OTYwLCJqdGkiOiJTbW5JdjVITXV5OEN3VEI3SDZ1YVN3IiwiaWF0IjoxNTc1NDMxMTYwLCJhdXRoX21vZGUiOiJtb2JpbGUiLCJhdXRoX2lkIjoiKzg2LTEzOTAyODcyODM2In0.833Qj45TiVchmCbYcikqCnxcx7InY4yB--Pz7jwYPiY",
        'Postman-Token': "2882ee32-35c8-4f0b-9851-8c1ef0c985b4"
    }

    response = requests.request("GET", url1, data=payload, headers=headers)
    print(response.json())
    time.sleep(1)



print("测品执行完成执行完成")



a.close()



