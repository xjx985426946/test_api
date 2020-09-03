from elasticsearch import Elasticsearch
from sshtunnel import SSHTunnelForwarder


class ElasticSearchClass(object):

    def connect(self):
        # 跳板参数 ssh
        ecs_host = '119.23.252.140'
        ecs_user = 'intbee'
        ecs_password = 'IntbeE2018'

        # 远程es服务配置
        es_host = 'elasticsearch.server.com'
        es_port = 9200

        self.server = SSHTunnelForwarder(
            (ecs_host, 22),  # B机器的配置
            ssh_password=ecs_password,
            ssh_pkey='intbee-test-intbee.key',
            ssh_username=ecs_user,
            remote_bind_address=(es_host, es_port))  # A机器的配置

        self.server.start()

        self.es = Elasticsearch(hosts=[{'host': '127.0.0.1', 'port': self.server.local_bind_port}],
                                http_auth=('elastic','zhuchao123'))
        return self.es

    # def count(self, indexname):
    #     """
    #     :param indexname:
    #     :return: 统计index总数
    #     """
    #     return self.es.count(index=indexname)
    #
    # def delete(self, indexname, doc_type, id):
    #     """
    #     :param indexname:
    #     :param doc_type:
    #     :param id:
    #     :return: 删除index中具体的一条
    #     """
    #     self.es.delete(index=indexname, doc_type=doc_type, id=id)
    #
    # def get(self, indexname, id):
    #     return self.es.get(index=indexname, id=id)

    # def search(self, indexname, size=10):
    #     try:
    #         return self.es.search(index=indexname, size=size, sort="@timestamp:desc")
    #     except Exception as err:b
    #         print(err)


a = ElasticSearchClass()
b =  a.connect()


res = b.search(index="intbee_action_trail",doc_type="event_tracking",body=None,size=1000)
# print(res)
L = []
for re in res['hits']['hits']:
    L.append(re['_source']['spreaderUuid'])
    L = list(set(L))

mt = '1556640000000'
day = '1557072000000'

for i in L:

    body = {
        "query": {
            "term": {
                "spreaderUuid": i
            },
            "range":{
                "createTime": {
                    "gte": 1556640000000,
                }
            }
        }
    }
    res = b.search(index="intbee_action_trail",doc_type="event_tracking",body=body,size=10000)
    print(res)


body = {
    "bool": {
        "must": [
                    { "term": { "spreaderUuid": '5cd26e8046e0fb000665472a'}},
                    { "range": { "createTime":{"gte": 1556640000000}}}
        ]
    }
}
res = b.search(index="intbee_action_trail",doc_type="event_tracking",body=body,size=10000)
print(res)