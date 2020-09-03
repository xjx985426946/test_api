import flask,json

# 创建接口后台服务，方便请求接口
server = flask.Flask(__name__)  # 把app.python文件当做一个server

# 装饰器，将get_all_user()函数变为一个接口 127.0.0.1:9000/get_user

@server.route('/watch/address',methods=['get', 'post'])
def get_all_user():
    all_user = {
        'watch_id':1,
        'map_address': 5
    }
    res = json.dumps(all_user, ensure_ascii=False)  # 将list转换为json串，ensure_ascii为False时，可以包含non-ASCII字符
    return res

@server.route('/watch/check',methods=['get', 'post'])
def get_all_check():
    all_user = {
        'watch_id':1,
        'check': True
    }
    res1 = json.dumps(all_user, ensure_ascii=False)  # 将list转换为json串，ensure_ascii为False时，可以包含non-ASCII字符
    return res1
# 启动服务，debug=True表示修改代码后自动重启；
# 启动服务后接口才能访问，端口号为9000，默认ip地址为127.0.0.1
server.run(port=9000, debug=True)




"""



1、用户管理 （后台录入授权学生、家长、老师）、小程序前端权限控制，学生在线监管（学生来源毕业分布图+教学信息提醒）   叶国柱

2、考勤管理、教学管理（学生、家长、老师信息管理，教室课程分配情况）、设备管理   柯思欣

3、通知警报（检查学生是否离开区域发送短信、站内通知给老师家长）、采集数据  陈海镇

4、地图、监控、门禁  许占鳌

5、小程序   陈佳鸿

6、产品需求    许占鳌、邱伟佳



"""

