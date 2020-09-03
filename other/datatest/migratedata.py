import pymongo
from sshtunnel import SSHTunnelForwarder
import sys


#这是个同步测试环境的数据到开发环境的脚本
## 通过跳板 链接服务器mongo
copy_db = 'intbee_miniprogram'
if len(sys.argv) > 1:
	copy_db = sys.argv[1]

ssh_host = '119.23.252.140'
ssh_port = 22
ssh_user = 'intbee' #intbee
ssh_pwd = 'IntbeE2018' #IntbeE2018

ignore = [] ##配置忽略复制表

# 主库连接配置
db_host = 'mongo.server.com'
db_port = 27017
db_user = 'intbee'
db_pwd = 'mongo_test2016'
db_name = copy_db

# 复制到库连接配置
dev_db_host = '10.0.1.193'
dev_db_port = 27017
dev_db_user = 'intbee'
dev_db_pwd = 'mongo_test2016'
dev_db_name = copy_db

# 查询一页数据限制
find_limit = 1000

server = SSHTunnelForwarder(
    ssh_address_or_host=(ssh_host, ssh_port),  # 指定ssh登录的跳转机的address
    ssh_username=ssh_user,  # 跳转机的用户
    ssh_password=ssh_pwd,  # 跳转机的密码
    remote_bind_address=(db_host, db_port))
server.start()

## 数据库连接
t_client = pymongo.MongoClient('127.0.0.1', server.local_bind_port)
t_db_ = t_client[db_name]
t_db_.authenticate(db_user, db_pwd)

## 数据库连接
d_client = pymongo.MongoClient('mongodb://%s:%s@%s:%s' % (dev_db_user,dev_db_pwd,dev_db_host,dev_db_port))
# d_client = pymongo.MongoClient(dev_db_host,dev_db_port)
d_db = d_client[dev_db_name]
# d_db.authenticate(dev_db_user, dev_db_pwd)


## 数据库同步
collectionNames = t_db_.collection_names()
index = 0
print('start ...')
for collectionName in collectionNames:
	index = index + 1
	print('copy table %s:%10.8s%s \n'%(collectionName,str(index*100/len(collectionNames)),'%'))
	##判断忽略
	if collectionName in ignore:
		continue
	
	collection = t_db_[collectionName]
	d_collection = d_db[collectionName]
	offset = 0
	count = collection.count()
	##复制前先删除之前数据
	del_count = d_collection.delete_many({})
	print('delete old data total: %d'%(del_count.deleted_count))
	##循环复制数据
	print('copy data from %s,curent:%d,total:%d'%(collectionName,offset,count),end='\r')
	while offset < count:
		try:
			data = collection.find().limit(find_limit).skip(offset)
			x = d_collection.insert_many(data)
		except (Exception):
			print('copy data error at %d'%(offset),end='\r')
		offset = find_limit + offset
		if offset > count:
			offset = count;
		print('copy data from %s,curent:%d,total:%d'%(collectionName,offset,count),end='\r')
	

t_client.close()
d_client.close()
server.stop()
print('\nFINISH!!!')
