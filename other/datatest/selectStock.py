#帮助运营查询顺丰商品的口罩哪些地区有库存

# import requests
#
# url = "https://item.intbee.com/capi/product/74198/sfbest/stock"
#
# querystring = {"province":"广东省","city":"深圳市","district":"南山区","quantity":"1"}
#
# headers = {
#     'content-type': "application/json",
#     'access_token': "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOm51bGwsImF1ZCI6IjEwMSIsInN1YiI6IjViZWEyY2RmNzY2MzgzMDAwNmYxNDBjMiIsImFwcGlkIjoiMTAxIiwiZXhwIjoxNTgyODA4NDY0LCJqdGkiOiJ6QjAzcDZCNmtVU3VKbTlXa1dVNVZBIiwiaWF0IjoxNTgyMjAzNjY0LCJhdXRoX21vZGUiOiJtb2JpbGUiLCJhdXRoX2lkIjoiKzg2LTEzNzI5NTQyMTk0In0.FkD2fVXzXnJKTFIZ2sCRNLVdBy2_amABNir8cn0z38o",
#     }
#
# response = requests.request("GET", url,  headers=headers, params=querystring)
#
# print(response.text)


import requests

url = "https://qiniu-static.intbee.com/assets/json/districts-logistics.json"

headers = {
    'content-type': "application/json",
    'access_token': "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOm51bGwsImF1ZCI6IjEwMSIsInN1YiI6IjViZWEyY2RmNzY2MzgzMDAwNmYxNDBjMiIsImFwcGlkIjoiMTAxIiwiZXhwIjoxNTgyODA4NDY0LCJqdGkiOiJ6QjAzcDZCNmtVU3VKbTlXa1dVNVZBIiwiaWF0IjoxNTgyMjAzNjY0LCJhdXRoX21vZGUiOiJtb2JpbGUiLCJhdXRoX2lkIjoiKzg2LTEzNzI5NTQyMTk0In0.FkD2fVXzXnJKTFIZ2sCRNLVdBy2_amABNir8cn0z38o",
}

response = requests.request("GET", url, headers=headers)

country = response.json()

url2 = "https://item.intbee.com/capi/product/74198/sfbest/stock"
for area in country:
    for state in area['states']:
        for city in state['city']:
            for name in city['district']:

                querystring = {"province":state['state'],"city":city['city'],"district":name['name'],"quantity":"1"}


                response = requests.request("GET", url2,  headers=headers, params=querystring)

                re = response.json()

                # try:
                #     if re['result']['stock_status'] != 0 or re['result']['stock_status'] != 4 or re['result']['stock_status'] != 1:
                #         print("省：", state['state'], "市：", city['city'], "区：", name['name'])
                # except:
                #     re = response.json()
                if re['code']==50000:
                    # print(re)
                    pass
                else:
                    if re['result']['stock_status'] != 0 and re['result']['stock_status'] != 4 and  re['result']['stock_status'] != 1:
                        print(re['result']['stock_status'])
                        print("省：", state['state'], "市：", city['city'], "区：", name['name'])
                        break
                    else:
                        # print("省：", state['state'], "市：", city['city'], "区：", name['name'])
                        break


print("执行完毕")