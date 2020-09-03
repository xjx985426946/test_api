import requests
import urllib.parse
url = "https://api.intbee.com/store/public/category"

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "d4c87efd-ca52-4ae2-8dee-9c0172efbc2b"
    }

response = requests.request("GET", url, headers=headers)

results = response.json()

L = []
L2 = []
for result in results['result']:
    for i in result['child_category']:
        for j in i['child_category']:
            L.append(str(j['id']))
            L2.append(j['name'])

#取出所有三级品类的category_id 和name
m = dict(zip(L,L2))

# for i in m:
#     print(m[i])

url = "https://api.intbee.com/api/v2/common/intbee-escards"

for k in m:
    searchText = urllib.parse.unquote(m[k])
    querystring = {"limit":"10","offset":"0","order":"desc","searchText":searchText,"sortby":"creationTime"}

    headers = {
        'Cache-Control': "no-cache",
        'Postman-Token': "2b60b515-49a8-4737-adde-6ad96134e300"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    results = response.json()
    for i in results['result']['cards']:

        #输出查询的product_id
        print(i['product_id'])
