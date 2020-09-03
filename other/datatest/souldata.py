import requests
import os
import yaml
from os import path
import xlrd
def createdata(product_name ,category,tag,brand,custom_tags,token,attr_value):
    """

    :param product_name: 商品名称
    :param category:  商品品类id
    :param tag: 商品标签
    :param token:
    :param brand:
    :param custom_tags:
    :return:
    """

    headers = {
        'Content-Type': "application/json",
        'access_token': token,
    }

    url = "http://test-api.intbee.com/fapi/product"
    param = {
          "attributes": [
            {
              "name": "品质",
              "value": attr_value
            }
          ],
          "categories": category,
          "desc_video_url": "1222",
          "extension": {
            "additionalProp1": "123",
            "additionalProp2": "123",
            "additionalProp3": "123"
          },
          "image_video_url": "123",
          "images": "http://static.d.intbee.com/userid/FqYwUTGAEdoxj15vPnd7CVnVd97i.png",
          "product_desc": "商品描述",
          "brand_name": brand,
          "custom_tags":[custom_tags],
          "product_name": product_name,
          "product_no": "123",
          "product_species": 1,
          "product_tags": tag,
          "product_type": 0,
          "reward": 0.1,
          "rich_text": "123456",
          "shop_info": {
            "shop_id": "10179905",
            "shop_name": "智蜂深圳"
          },
          "stock": [
            {
              "delivery_price": 0.1,
              "image_url": "http://static.d.intbee.com/userid/FqYwUTGAEdoxj15vPnd7CVnVd97i.png",
              "market_price": 0.1,
              "quantity": 100,
              "selling_price": 0.1,
              "standards": [
                {
                  "name": "颜色",
                  "value": "红色"
                }
              ],
              "tax_rates": [
                0
              ]
            }
          ],
          "tax_free": True,
          "unit_weight": 10,
          "vip_reward": 0.01
    }

    print(param)
    response = requests.request("POST", url, json=param, headers=headers)
    print(response.json())

    id = response.json()['result']

    urls = 'http://test-api.intbee.com/fapi/card/create'
    params = {
      "card_type": 0,
      "product_id": id,
      "reward_amount": 0.01,
      "reward_vip_amount": 0.01,
      "plan_open_group": True,
      "flash_sale": {"begin_gmt": "2019-09-09 15:39:00", "end_gmt": "2019-09-29 15:49:00", "discount_amount": 0.01, "buy_limit": 5}
    }
    print(params)
    response = requests.request("POST", urls, json=params, headers=headers)

    print(response.json())



if __name__ == '__main__':

    token ="eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOm51bGwsImF1ZCI6IjEwMSIsInN1YiI6IjU5NDhjYmM4MzZkZDY3NzYyZTQyMDlhNyIsImFwcGlkIjoiMTAxIiwiZXhwIjoxNTY4MTgyMjEyLCJqdGkiOiJJcUV6U3M5ci00VmxWRUpyRUFhcTJnIiwiaWF0IjoxNTY3NTc3NDEyLCJhdXRoX21vZGUiOiJtb2JpbGUiLCJhdXRoX2lkIjoiKzg2LTE4OTAxNjY3NzY2In0.h1MOgeyvliloLM9V1PJsoGzX0sO4jBZPrBhv46PwVPc"

    import yaml

    d = open('product.yaml')
    datas = yaml.load(d)['param']
    for data in datas:
        createdata(product_name=data['product_name'],category=data['category'],tag=data['tag'],brand=data['brand'],custom_tags=data['custom_tags'],token=data['token'],attr_value=data['attr_value'])


# import yaml
# d = open('product.yaml')
# data =  yaml.load(d)['param']
# print(data)