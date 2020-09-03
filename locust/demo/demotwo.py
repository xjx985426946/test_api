from locust import HttpLocust, TaskSet, task,events
from gevent._semaphore import Semaphore

all_locusts_spawned = Semaphore()
all_locusts_spawned.acquire()

def on_hatch_complete(**kwargs):
    all_locusts_spawned.release()

events.hatch_complete += on_hatch_complete

class UserBehavior(TaskSet):

    def login(self):
        mobile = "+86-13902879682"
        password = "e10adc3949ba59abbe56e057f20f883e"
        param = {"mobile":mobile,"password":password}
        headers = {"Content-Type": "application/json","app_id":"101"}
        with self.client.post('https://test-api.intbee.com/api/uc/auth/login',json =param,headers=headers) as response:
            if response.status_code == 200:
                self.token = response.json()["result"]["access_token"]

        mobile = "+86-13729542194"
        password = "e10adc3949ba59abbe56e057f20f883e"
        param = {"mobile": mobile, "password": password}
        headers = {"Content-Type": "application/json", "app_id": "101"}
        with self.client.post('https://test-api.intbee.com/api/uc/auth/login', json=param, headers=headers) as response:
            if response.status_code == 200:
                self.tokenc = response.json()["result"]["access_token"]

    def on_start(self):
        '''这里优先执行'''
        #来一个登录吧
        self.login()
        self.header = {
            "access_token": self.token
        }
        self.headerc = {
            "access_token": self.tokenc
        }
        all_locusts_spawned.wait()

    @task(1)
    def est1(self):
        url = 'https://test-www.intbee.com/fapi/card'

        param = {
            "limit":6,
            "cardStatus":0,
            "offset":0
        }
        with self.client.get(url,params=param,headers=self.header,catch_response = True) as response:
            if response.status_code == 200:
                response.success()

    @task(3)
    def est2(self):
        url = 'https://test-api.intbee.com/mapi/v3/common/spreaders/sales/rank'
        param = {
            "limit":10,
            "type":1,
            "offset":0
        }

        with self.client.get(url, params=param, headers=self.headerc, catch_response=True) as response:
            if response.status_code == 200:
                response.success()


class WebsiteUser(HttpLocust):
    host = 'https://test-www.intbee.com'
    task_set = UserBehavior
    min_wait = 2000
    max_wait = 3000





"""

#C 端  ：  单一接口  比如下单  性能测试
业务场景  ：  比如你先搜索 后才下单    业务场景的设计


丽华:app


F端  



F、C、V



"""



