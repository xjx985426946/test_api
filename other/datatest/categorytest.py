import requests
import  urllib.parse
from mysql.pymongo_db import Mongodb
from common.logger import Log

d = Mongodb("intbee_product")
client = d.get_mongodb_client()
db = client.intbee_product
collection = db.intbee_store_product


def catgory():
    print("开始测试品类".center(66,"-"))
    url = "https://test-api.intbee.com/store/public/category"
    headers = {
        'Cache-Control': "no-cache",
        'Postman-Token': "d4c87efd-ca52-4ae2-8dee-9c0172efbc2b"
    }
    response = requests.request("GET", url, headers=headers)
    results = response.json()
    print("页面查询总共有" + str(len(results['result'])) + "种一级品类--------------------")
    print("\n")
    num = 1
    for result in results['result']:
        print("第%s个品类为:" %(num) + result['name'],)
        print( result['name'] + "品类下有" + str(len(result['child_category'])) + "种二级品类----------")
        print("\n")
        num2 = 1
        for result_two in result['child_category']:
            print( result['name'] + "的第%s个二级品类为："%(num2) + str(result_two['name']))
            print(str(result_two['name']) + "的品类下有" + str(len(result_two['child_category'])) + "种三级品类-----")
            num3 = 1
            for result_three in result_two['child_category']:
                print(result_two['name'] + "的第%s个三级品类为："%(num3) + str(result_three['name']))
                print("三级品类" + result_three['name'] + "的category_id为" + str(result_three['id']))
                # Log().info("三级品类" + result_three['name'] + "的category_id为" + str(result_three['id']) + "该品类下的商品的category_id应该要满足等于%s" %(str(result_three['id'])))
                print("页面点击" + result_three['name'] + "查询" + result_three['name'] + "下的50个商品")
                print("开始查询....")

                url = "https://test-api.intbee.com/api/v2/common/intbee-escards"
                text= str(result['name']) + "0" + str(result_two['name']) + "0" + str(result_three['name']) + "0"
                # searchText = urllib.parse.unquote(result_three['name'])
                searchText = urllib.parse.unquote(text)
                querystring = {"searchText":searchText,"order":"desc","sortby":"creationTime","searchBy":"category","limit":"10","offset":"0"}
                headers = {
                    'Cache-Control': "no-cache",
                    'Postman-Token': "2b60b515-49a8-4737-adde-6ad96134e300"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                pd = response.json()
                print("查询成功")
                print("一共查询出" + str(len(pd['result']['cards'])) + "条商品")
                # print(pd['result']['cards'])
                num4 = 1

                for result_four in pd['result']['cards']:
                    print("第%s个商品名称为" %(num4) + str(result_four['product_name']) + "商品id为：" + str(result_four['product_id']))
                    dbresult = collection.find({'_id': int(result_four['product_id'])}).sort("_id", -1)
                    # print(type(result_four['product_id']))
                    categry_id = dbresult[0]['categories'][-1]

                    print("开始判断查询出的商品是否属于%s" %( result_three['name']) + "品类下")
                    if categry_id == result_three['id']:
                        print("商品的category_id为:%s与三级品类category_id: %s 对应，测试通过" %(categry_id,result_three['id']))
                    else:
                        print("商品的category_id为:%s与三级品类category_id: %s 不相等，测试不通过" % (categry_id, result_three['id']))
                        print("错误数据为第%s一级品类:%s的第%s个二级品类:%s的第%s个三级品类%s的%s个商品%s " %(num,result['name'],num2,str(result_two['name']),num3,result_three['name'],num4,result_four['product_name']))
                        Log().error("商品的category_id为:%s与三级品类category_id: %s 不相等，测试不通过" % (categry_id, result_three['id']))
                        Log().error("错误数据为第%s一级品类:%s的第%s个二级品类:%s的第%s个三级品类%s的%s个商品%s " %(num,result['name'],num2,str(result_two['name']),num3,result_three['name'],num4,result_four['product_name']))
                        print("\n")
                    num4 += 1
                num3 += 1
            print("\n")
            num2 += 1
        num = num + 1
    d.close()

catgory()
# d.close()