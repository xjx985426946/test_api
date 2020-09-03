#测试封神榜出现重复数据的问题

import requests
from collections import Counter
url = "https://api.intbee.com/mapi/v3/common/spreaders/sales/rank"

querystring = {"limit":"1000","offset":"0"}

headers = {'Postman-Token': '86a8b611-8011-4da3-992c-63f391f5ef48'}

response = requests.request("GET", url, headers=headers, params=querystring)

result = response.json()
L = []
for i in result['result']:
    L.append(i['spreader_uuid'])
print(len(L))

if len(L) != len(set(L)):

    print('出现重复数据!!!')
else:

    print('没有出现重复数据!!')

print("出现重复的数据有V端uuid有")
print([item for item, count in Counter(L).items() if count > 1])



