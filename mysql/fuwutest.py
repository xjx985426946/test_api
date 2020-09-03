from sshtunnel import SSHTunnelForwarder

class HC():
    def connect(self):
        # 跳板参数 ssh
        ecs_host = '119.23.252.140'
        ecs_user = 'intbee'
        # ecs_password = 'IntbeE2018'

        '''  写个配置文件
             local_port自定义本地映射的端口号
        '''
        conf = [
            {'host':'elasticsearch.server.com','port':9200,'local_port':65535}, #远程es服务地址
            {'host': '192.168.1.53', 'port': 3306, 'local_port': 6968}, #远程mysql服务地址
            {'host': 'mongo.server.com', 'port': 27017, 'local_port': 6967},  #远程mongo服务地址

            ]

        # 连接SSH
        for c in conf:
            self.server = SSHTunnelForwarder(
                (ecs_host, 22),  # B机器的配置
                # ssh_password=ecs_password,
                ssh_pkey='intbee-test-intbee.key',
                ssh_username=ecs_user,
                remote_bind_address=(c['host'], c['port']), # A机器的配置
                local_bind_address=('127.0.0.1', c['local_port']))
            self.server.start()
        print("远程服务连接成功")

hc = HC()
hc.connect()



class HC_produce():
    def connect(self):
        # 跳板参数 ssh
        ecs_host = '119.23.252.140'
        ecs_user = 'intbee'
        ecs_password = 'IntbeE2018'

        '''  写个配置文件
             local_port自定义本地映射的端口号
        '''
        conf = [
            {'host': '10.0.1.38', 'port': 3306, 'local_port': 7070}, #远程mysql服务地址
            ]

        # 连接SSH
        for c in conf:
            self.server = SSHTunnelForwarder(
                (ecs_host, 20039),  # B机器的配置
                ssh_password=ecs_password,
                ssh_username=ecs_user,
                remote_bind_address=(c['host'], c['port']), # A机器的配置
                local_bind_address=('127.0.0.1', c['local_port']))
            self.server.start()
        print("远程服务连接成功")


class HC_demo():
    def connect(self):
        # 跳板参数 ssh
        ecs_host = '119.23.252.140'
        ecs_user = 'intbee'
        ecs_password = 'IntbeE2018'

        '''  写个配置文件
             local_port自定义本地映射的端口号
        '''
        conf = [
            {'host': '10.0.1.193', 'port': 3306, 'local_port': 7071}, #远程mysql服务地址
            ]

        # 连接SSH
        for c in conf:
            self.server = SSHTunnelForwarder(
                (ecs_host, 20039),  # B机器的配置
                ssh_password=ecs_password,
                ssh_username=ecs_user,
                remote_bind_address=(c['host'], c['port']), # A机器的配置
                local_bind_address=('127.0.0.1', c['local_port']))
            self.server.start()
        print("远程服务连接成功")


hc = HC()
hc.connect()


