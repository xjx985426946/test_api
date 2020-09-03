from locust import HttpLocust, TaskSet, task,events


class UserBehavior(TaskSet):


    def login(self):

        list = ["13902879682","13729542194"]
        mobile = "+86-13902879682"
        password = "e10adc3949ba59abbe56e057f20f883e"
        param = {"mobile":mobile,"password":password}
        headers = {"Content-Type": "application/json","app_id":"101"}
        with self.client.post('https://test-api.intbee.com/api/uc/auth/login',json =param,headers=headers) as response:
            if response.status_code == 200:
                self.token = response.json()["result"]["access_token"]


    def on_start(self):
        '''这里优先执行'''
        #来一个登录吧
        self.login()
        self.header = {
            "access_token": self.token
        }

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


class WebsiteUser(HttpLocust):
    host = 'https://test-www.intbee.com'
    task_set = UserBehavior
    stop_timeout = 60
    min_wait = 1000
    max_wait = 1000




