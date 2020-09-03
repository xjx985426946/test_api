from locust import HttpLocust, TaskSet, task,events


#顺丰项目并发获取地址的测试
class UserBehavior(TaskSet):

    def on_start(self):
        '''这里优先执行'''
        self.header = {
            "access_token": 'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOm51bGwsImF1ZCI6IjEwMSIsInN1YiI6IjViZWEyY2RmNzY2MzgzMDAwNmYxNDBjMiIsImFwcGlkIjoiMTAxIiwiZXhwIjoxNTY3NzUwNTI4LCJqdGkiOiItaGJlRFhObm15RDY5WFRxbzdWcExBIiwiaWF0IjoxNTY3MTQ1NzI4LCJhdXRoX21vZGUiOiJtb2JpbGUiLCJhdXRoX2lkIjoiKzg2LTEzNzI5NTQyMTk0In0.NBP8uIYZ8zHc9sNzOH2W2grWnWUuNhLoSj01igUdvyA'
        }


    @task(1)
    def est1(self):
        url = 'http://test-kaola.intbee.com/v1/sfbest/product/stock'
        param = {
          "district": "南山区",
          "city": "深圳市",
          "province": "广东省",
          "quantity": 1,
          "thirdProductId": "1500005439"
        }

        with self.client.post(url,json=param,headers=self.header,catch_response = True) as response:
            if response.json()['code'] == 0:
                response.success()
            else:
                response.failure('Failed!')
            print(response.json())


class WebsiteUser(HttpLocust):
    host = 'https://test-www.intbee.com'
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 1000


