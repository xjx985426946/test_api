import  threading,time

# class MyThread(threading.Thread):
#
#     def __init__(self,name,):
#
#         super(MyThread,self).__init__()
#
#         self.name=name
#
#     def run(self):
#
#         print(self.name)
#
#         time.sleep(2)
#
#         t1=MyThread("哈哈")
#
#         t2=MyThread("恩恩")
#
#         t1.start()
#
#         t2.start()
#
#
# a = MyThread("gou")
# a.run()


# import threading,time,requests
#
# class MyThread(object):
#     def __init__(self):
#         self.url = "https://test-www.intbee.com/fapi/bank/cash"
#         self.payload = "{\n  \"payed_money\": 89.61,\n  \"sign\": \"intbee-order-notify-b1c7bc32-4b7a-11e9-8646-d663bd873d93\"\n}"
#         self.headers =  {
#             'Content-Type': "application/json",
#             'access_token': "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOm51bGwsImF1ZCI6IjEwMSIsInN1YiI6IjU4MWMwMGUxMmE1MGYwZmYwNzVlNGYyOSIsImFwcGlkIjoiMTAxIiwiZXhwIjoxNTU0OTY4MTcxLCJqdGkiOiJiTEJGSERnNEx0aUc0bF9MWERabVVRIiwiaWF0IjoxNTU0MzYzMzcxfQ.4NgCJAd3irnm6X36xSgqE3oUe1GUiqIjw7mPfCBkDjw",
#             'Postman-Token': "0cb4e58c-e7e6-4807-83de-67c7c93c57f3"
#         }
#     def run(self):
#
#         response = requests.request("POST", self.url, data=self.payload, headers=self.headers)
#
#         print(response.text)
#
# if __name__ == '__main__':
#
#     for i in range(1000):
#         a = MyThread()
#         t = threading.Thread(target=a.run())
#         t.start()
#
#         b = MyThread()
#         t2 = threading.Thread(target=b.run())
#         t2.start()


#测试提现时，并发测试，不能产生两笔提现

import threading,time,requests

class MyThread(object):
    def __init__(self):
        self.url = "https://test-api.intbee.com/auth/signup/customer"
        self.payload = "{\n  \"mobile\": \"13729542194\"\n}"
        self.headers = {
    'access_token': "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOm51bGwsImF1ZCI6IjEwMSIsInN1YiI6IjViZWEyY2RmNzY2MzgzMDAwNmYxNDBjMiIsImFwcGlkIjoiMTAxIiwiZXhwIjoxNTU1MzA5NDg1LCJqdGkiOiJ0Q3ItR1FwLURzU1ZQZExvWmEtajFRIiwiaWF0IjoxNTU0NzA0Njg1fQ.RUOh631Za5lvmnH4K7hYyJwzBEq-j5wtDEmx7qtaaWc",
    'Content-Type': "application/json",
    'Postman-Token': "78726451-4bb3-4a71-874c-f4e04be74333"
    }
    def run(self):

        response = requests.request("POST", self.url, data=self.payload, headers=self.headers)

        print(response.text)


if __name__ == '__main__':

    for i in range(1000):
        a = MyThread()
        t = threading.Thread(target=a.run())
        t.start()

        b = MyThread()
        t2 = threading.Thread(target=b.run())
        t2.start()

        c = MyThread()
        t3 = threading.Thread(target=c.run())
        t3.start()



# import  threading,time
#
# class MyThread(threading.Thread):
#
#     def __init__(self,name,):
#
#         super(MyThread,self).__init__()
#
#         self.name=name
#
#     def run(self):
#
#         print(self.name)
#
#
# for i in range(0,10):
#     time.sleep(3)
#     t1=MyThread("哈哈")
#
#     t2=MyThread("恩恩")
#
#     t1.start()
#
#     t2.start()