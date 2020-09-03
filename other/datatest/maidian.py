from common.excle import Excel
from mysql.pymongo_db import Mongodb
ex = Excel("maidian.xlsx")
datas = ex.getData(sheetName="Sheet1")

d = Mongodb("zc_thirdparty")
client = d.get_mongodb_client()

db = client.zc_thirdparty
collection = db.center_event_buried_point

for data in datas:

    results = collection.find({"user_uuid":"5d89fa89df8b0700065a0655","event_dec":data['ecent_dec']}).count()
    if results == 0:
        print("没有成功埋点的数据:", data['event_id'], data['ecent_dec'],data['page_title'])

d.close()

#5d89fa89df8b0700065a0655