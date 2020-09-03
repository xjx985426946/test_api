from locust import HttpLocust, TaskSet, task,events
from gevent._semaphore import Semaphore

# all_locusts_spawned = Semaphore()
# all_locusts_spawned.acquire()
#
# def on_hatch_complete(**kwargs):
#     all_locusts_spawned.release()
#
# events.hatch_complete += on_hatch_complete

class UserBehavior(TaskSet):

    # def login(self):
    #     mobile = "+86-13902879682"
    #     password = "e10adc3949ba59abbe56e057f20f883e"
    #     param = {"mobile":mobile,"password":password}
    #     headers = {"Content-Type": "application/json","app_id":"101"}
    #     with self.client.post('https://test-api.intbee.com/api/uc/auth/login',json =param,headers=headers) as response:
    #         if response.status_code == 200:
    #             self.token = response.json()["result"]["access_token"]


    def on_start(self):
        '''这里优先执行'''
        #来一个登录吧
        # self.login()
        self.header = {
            "access_token": 'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOm51bGwsImF1ZCI6IjEwMSIsInN1YiI6IjViZWEyY2RmNzY2MzgzMDAwNmYxNDBjMiIsImFwcGlkIjoiMTAxIiwiZXhwIjoxNTY3NzUwNTI4LCJqdGkiOiItaGJlRFhObm15RDY5WFRxbzdWcExBIiwiaWF0IjoxNTY3MTQ1NzI4LCJhdXRoX21vZGUiOiJtb2JpbGUiLCJhdXRoX2lkIjoiKzg2LTEzNzI5NTQyMTk0In0.NBP8uIYZ8zHc9sNzOH2W2grWnWUuNhLoSj01igUdvyA'
        }
        # all_locusts_spawned.wait()


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

        with self.client.get(url,json=param,headers=self.header,catch_response = True) as response:
            if response.status_code == 200:
                response.success()


class WebsiteUser(HttpLocust):from locust import HttpLocust, TaskSet, task,events
from gevent._semaphore import Semaphore

# all_locusts_spawned = Semaphore()
# all_locusts_spawned.acquire()
#
# def on_hatch_complete(**kwargs):
#     all_locusts_spawned.release()
#
# events.hatch_complete += on_hatch_complete

# class UserBehavior(TaskSet):
#
#     # def login(self):
#     #     mobile = "+86-13902879682"
#     #     password = "e10adc3949ba59abbe56e057f20f883e"
#     #     param = {"mobile":mobile,"password":password}
#     #     headers = {"Content-Type": "application/json","app_id":"101"}
#     #     with self.client.post('https://test-api.intbee.com/api/uc/auth/login',json =param,headers=headers) as response:
#     #         if response.status_code == 200:
#     #             self.token = response.json()["result"]["access_token"]
#
#
#     def on_start(self):
#         '''这里优先执行'''
#         #来一个登录吧
#         # self.login()
#         self.header = {
#             "access_token": 'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOm51bGwsImF1ZCI6IjEwMSIsInN1YiI6IjViZWEyY2RmNzY2MzgzMDAwNmYxNDBjMiIsImFwcGlkIjoiMTAxIiwiZXhwIjoxNTY3NzUwNTI4LCJqdGkiOiItaGJlRFhObm15RDY5WFRxbzdWcExBIiwiaWF0IjoxNTY3MTQ1NzI4LCJhdXRoX21vZGUiOiJtb2JpbGUiLCJhdXRoX2lkIjoiKzg2LTEzNzI5NTQyMTk0In0.NBP8uIYZ8zHc9sNzOH2W2grWnWUuNhLoSj01igUdvyA'
#         }
#         # all_locusts_spawned.wait()
#
#
#     @task(1)
#     def est1(self):
#         url = 'http://test-kaola.intbee.com/v1/sfbest/product/stock'
#         param = {
#           "district": "南山区",
#           "city": "深圳市",
#           "province": "广东省",
#           "quantity": 1,
#           "thirdProductId": "1500005439"
#         }
#
#         with self.client.get(url,json=param,headers=self.header,catch_response = True) as response:
#             if response.status_code == 200:
#                 response.success()
#
#
# class WebsiteUser(HttpLocust):
#     host = 'https://test-www.intbee.com'
#     task_set = UserBehavior
#     min_wait = 1000
#     max_wait = 1000



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

    # host = 'https://test-www.intbee.com'
    # task_set = UserBehavior
    # min_wait = 1000
    # max_wait = 1000



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
