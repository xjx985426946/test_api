from locust import HttpLocust, TaskSet, task,events

class UserBehavior(TaskSet):


    def on_start(self):
        '''这里优先执行'''
        #来一个登录吧

        self.header = {
            "access_token": 'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOm51bGwsImF1ZCI6IjEwMSIsInN1YiI6IjViZWEyY2RmNzY2MzgzMDAwNmYxNDBjMiIsImFwcGlkIjoiMTAxIiwiZXhwIjoxNTY4MzU2NDIyLCJqdGkiOiJVNTY0ZWhnTDhWT2lIQ09QY2hGSDVBIiwiaWF0IjoxNTY3NzUxNjIyLCJhdXRoX21vZGUiOiJtb2JpbGUiLCJhdXRoX2lkIjoiKzg2LTEzNzI5NTQyMTk0In0.T8qjnpoQqK9keqhh1duP9SLUAmaAZhodTDm9cHh9wfA'
        }


    @task(1)
    def test1(self):
        url = 'https://test-item.intbee.com/capi/order/postage/money?product_id=180109&quantity=1&sku=5200322435=1&province_code=%E6%B5%99%E6%B1%9F%E7%9C%81&province=%E6%B5%99%E6%B1%9F%E7%9C%81&district=%E7%93%AF%E6%B5%B7%E5%8C%BA&city=%E6%B8%A9%E5%B7%9E%E5%B8%82'
        with self.client.get(url,params=None,headers=self.header,catch_response = True) as response:
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



# from locust import TaskSet, task, HttpLocust,events
# from gevent._semaphore import Semaphore
#
# all_locusts_spawned = Semaphore()
# all_locusts_spawned.acquire()
#
# def on_hatch_complete(**kwargs):
#     all_locusts_spawned.release()
#
# events.hatch_complete += on_hatch_complete
#
# class UserBehavior(TaskSet):
#
#     def on_start(self):
#
#         # self.index = 0
#         #
#         # self.loginData = ['lm', 'liuchan', 'dy', 'wangwu', 'admin','hh']
#         # print("=========验证执行了多少次1")
#
#         mobile = "+86-13902879682"
#         password = "e10adc3949ba59abbe56e057f20f883e"
#         param = {"mobile":mobile,"password":password}
#         headers = {"Content-Type": "application/json","app_id":"101"}
#         with self.client.post('https://test-www.intbee.com/api/uc/auth/login',json =param,headers=headers) as response:
#             if response.status_code == 200:
#                 self.token = response.json()["result"]["access_token"]
#
#         print("=========验证执行了多少次1")
#         all_locusts_spawned.wait()
#
#     @task
#     def testUser(self):
#
#         # print("---- index :" + str(self.index))
#         #
#         # print("---- data :" + self.loginData[self.index])
#         #
#         # self.index = (self.index + 1) % len(self.loginData)
#         print(self.token)
#
# class WebsiteUser(HttpLocust):
#
#     task_set = UserBehavior
#
#     min_wait = 1000
#
#     max_wait = 3000
