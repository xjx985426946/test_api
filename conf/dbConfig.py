import sys
path = str(sys.argv[0]).split('/')[-1]

#测试环境配置
ecs_host = '119.23.252.140'
ecs_user = 'intbee'
ecs_password = 'IntbeE2018'
ecs_port = 22

# 远程mongo服务配置
mongo_host = 'mongo.server.com'
mongo_user = 'intbee'
mongo_password = 'mongo_test2016'

# 远程mysql服务配置
mysql_host = 'mysql.server.com'
mysql_user = 'intbee'
mysql_password = 'intbee@mysql'

#demo环境配置
if path == 'run_demo.py':
    # 跳板参数 ssh
    ecs_host = '119.23.252.140'
    ecs_user = 'intbee'
    ecs_password = 'IntbeE2018'
    ecs_port = 20039

    #远程mongo服务配置
    mongo_host = '10.0.1.193'
    mongo_user = 'intbee'
    mongo_password = 'mongo_test2016'

    #  远程mysql服务配置
    mysql_host = '10.0.1.193'
    mysql_user = 'intbee'
    mysql_password = 'intbee@mysql'

    print("执行demo环境脚本")