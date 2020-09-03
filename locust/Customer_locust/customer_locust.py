from locust import HttpLocust, TaskSet, task,events

class UserBehavior(TaskSet):

    def login(self):
        mobile = "+86-13640993513"
        password = "e10adc3949ba59abbe56e057f20f883e"
        param = {"mobile": mobile, "password": password}
        headers = {"Content-Type": "application/json", "app_id": "101"}
        with self.client.post('https://test-item.intbee.com/api/uc/auth/login', json=param, headers=headers) as response:
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
    def product_detail(self):
        url = 'https://test-item.intbee.com/capi/card/product/106013'

        param = {
            "uuid":'5acec58aec68a84bc7c1b495'
        }
        with self.client.get(url, params=param, headers=self.header, catch_response=True) as response:
            if response.status_code == 200:
                response.success()

    @task(1)
    def order_list(self):
        url = 'https://test-item.intbee.com/capi/order/list'
        # url = 'https://test-www.intbee.com/fapi/postages'

        param = {
            "limit": 8,
            "status": '',
            "offset": 0
        }
        with self.client.get(url, params=param, headers=self.header, catch_response=True) as response:
            if response.status_code == 200:
                response.success()

class WebsiteUser(HttpLocust):
    host = 'https://test-item.intbee.com'
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 1000



