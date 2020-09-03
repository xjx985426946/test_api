import  requests
import uuid,inspect
from  common import logger
class HttpRquest(object):
    log = logger.Log()
    res= {}
    def http_request(self,method,url,param,header,cookies):
        """
        :param method: 请求类型
        :param url:    请求地址
        :param param:  请求参数
        :param header:  请求头部
        :param cookies:
        :return:  请求结果
        """
        if method.upper() == 'GET':
            try:
                self.res = requests.get(url, params=param, headers=header,cookies=cookies)
            except Exception as e:
                self.log.error('报错啦：{0}'.format(e))
        elif method.upper() == 'POST':
            try:
                self.res = requests.post(url, json=param,  headers=header,cookies=cookies)
            except Exception as e:
                self.log.error('报错啦：{0}'.format(e))
        elif method.upper() == 'PUT':
            try:
                self.res = requests.put(url, json=param, headers=header, cookies=cookies)
            except Exception as e:
                self.log.error('报错啦：{0}'.format(e))
        elif method.upper() == 'DELETE':
            try:
                self.res = requests.delete(url, data=param, headers=header, cookies=cookies)
            except Exception as e:
                self.log.error('报错啦：{0}'.format(e))
        else:
            self.log.info('请求方式错误')

        return  self.res

    def __jsonpr(self, url, method ,*args, **kwags):
        '''测试执行http请求'''
        headers={'content-type':'application/json'}
        self.payload={
            "jsonprc":"2.0",
            "id":uuid.uuid4().hex,
            "method":method,
            "params":args if args else kwags

        }
        response=requests.post(url,json=self.payload,headers=headers)
        try:
            self.res = response.json()
        except Exception as e:
            self.res = None
        finally:
            # a=inspect.stack()[1][3]
            # self.description=cls.__class__.__dict__[a].__doc__
            # self.url = url
            # self.headers = headers
            return self.res