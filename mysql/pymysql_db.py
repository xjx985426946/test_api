from pymysql import connect,cursors
from sshtunnel import SSHTunnelForwarder
import os
from conf import dbConfig

class Connectmysql(object):

    def __init__(self,data_db):

        #数据库名称
        self.data_db = data_db
        self.server = None
        self.cursor = None

    def connectDatabase(self):
        try:
            # 跳板参数 ssh
            ecs_host = dbConfig.ecs_host
            ecs_user = dbConfig.ecs_user
            ecs_password = dbConfig.ecs_password
            ecs_port = dbConfig.ecs_port

            # 远程mysql服务配置
            mysql_host =  dbConfig.mysql_host
            mysql_database = self.data_db
            mysql_user = dbConfig.mysql_user
            mysql_password = dbConfig.mysql_password


            # 连接ssh

            self.server = SSHTunnelForwarder(
                (ecs_host, ecs_port),  # B机器的配置
                ssh_password=ecs_password,
                ssh_username=ecs_user,
                ssh_pkey=os.path.dirname(__file__) + '/intbee-test-intbee.key',
                remote_bind_address=(mysql_host, 3306))  # A机器的配置

            self.server.start()

            self.conn = connect(host='127.0.0.1',
                                port=self.server.local_bind_port,
                                user=mysql_user,
                                passwd=mysql_password,
                                db=mysql_database,
                                cursorclass=cursors.DictCursor)

            self.cursor = self.conn.cursor()
            return True
        except:
            # logger.error("connectDatabase failed")
            print("连接失败")
            return False


    def close(self):
        if self.conn:
            self.conn.close()
        if self.cursor:
            self.cursor.close()
        if self.server:
            self.server.close()

    #查询一条数据
    def fetchone(self, sql, params=None):
        '''
        根据sql和参数获取一行数据
        :param sql: sql语句
        :param params: sql语句对象的参数元组，默认值为None
        :return: 查询的一行数据
        '''
        dataOne = None
        self.connectDatabase()
        try:
            count = self.cursor.execute(sql, params)
            if count != 0:
                dataOne = self.cursor.fetchone()
        except Exception as ex:
            print(ex)
        finally:
            self.close()
        return dataOne


    #查询多条数据
    def fetchall(self, sql, params=None):
        '''
        根据sql和参数获取一行数据
        :param sql: sql语句
        :param params: sql语句对象的参数列表，默认值为None
        :return: 查询的一行数据
        '''
        dataall = None
        self.connectDatabase()
        try:
            count = self.cursor.execute(sql, params)
            if count != 0:
                dataall = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            self.close()
        return dataall

    def __item(self, sql, params=None):
        '''
        执行增删改
        :param sql: sql语句
        :param params: sql语句对象的参数列表，默认值为None
        :return: 受影响的行数
        '''
        self.connectDatabase()
        count = 0
        try:
            count = self.cursor.execute(sql, params)
            self.conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            self.close()
        return count

    def update(self, sql, params=None):
        '''
        执行修改
        :param sql: sql语句
        :param params: sql语句对象的参数列表，默认值为None
        :return: 受影响的行数
        '''
        return self.__item(sql, params)

    # def insert(self, sql, params=None):
    #     '''
    #     执行新增
    #     :param sql: sql语句
    #     :param params: sql语句对象的参数列表，默认值为None
    #     :return: 受影响的行数
    #     '''
    #     return self.__item(sql, params)

    # def delete(self, sql, params=None):
    #     '''
    #     执行删除
    #     :param sql: sql语句
    #     :param params: sql语句对象的参数列表，默认值为None
    #     :return: 受影响的行数
    #     '''
    #     return self.__item(sql, params)

if __name__ == '__main__':

    c =  Connectmysql("intbee")
    sql = 'SELECT * FROM intbee_card limit 0,1;'
    # params = [176508]
    data = c.fetchall(sql)
    print(data)
    if not data:
        print(11)

    # con = Connectmysql("intbee")
    # # sql = 'SELECT * FROM intbee_card WHERE product_id= %s;'
    # # params = [618]
    # # data = con.fetchone(sql, params)
    # # print(data['id'])
    # sql = 'update intbee_card set card_status =%s  where  product_id= %s;'
    # params = [2, 23]
    # count = con.update(sql, params)
    # # 判断
    # if count:
    #     print('操作成功.')
    # else:  # None,False,0
    #     print('操作失败.')

    # import datetime
    #
    # utime = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d %H:%M:%S")
    # con = Connectmysql("intbee")
    # sql = 'UPDATE intbee_sell_history set settle_time=str_to_date(%s,"%%Y-%%m-%%d %%H:%%i:%%S") WHERE order_no=%s;'
    # params = [utime, str(10110011564639834364569)]
    # count = con.update(sql, params)
    # if count:
    #     print('操作成功.')
    # else:  # None,False,0
    #     print(count)

    # sql = 'update intbee_sell_history set product_amount=%s WHERE order_no=%s;'
    # params = [utime,str(10110011564639834364569)]
    # count = con.update(sql,params)
    # if count:
    #     print('操作成功.')
    # else:  # None,False,0
    #     print(count)