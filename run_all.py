import sys
__author__ = 'hetchine'
import unittest
import sys,time,os,datetime
# #import allcase_list
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# from email.mime.image import MIMEImage
from common.send_email import SendMail
from HTMLTestRunnerNew import HTMLTestRunner
sys.path.append('./test_new')



def creattestsuit():
    testunit=unittest.TestSuite()
    test_dir='./test_new'     #运行时修改为指定测试目录
    print(test_dir)
    discover=unittest.defaultTestLoader.discover(test_dir,
        pattern ='test_*.py',
        top_level_dir=None)

    for testsuit in discover:
        for test_case in testsuit:
            testunit.addTest(test_case)
            print('case',test_case)
        print(testsuit)
    return testunit

alltestnames=creattestsuit()

if __name__=='__main__':
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    file='./report/'+now+'_result.html'
    fp = open(file,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='筑巢科技  接口  Test Report',
                            description='Implementation Example with: ')
    runner.run(alltestnames)
    fp.close()

    content = "接口自动化报告"
    subject = "接口自动化报告"
    from_addr = '13729542194@163.com'
    to_addr = ['957071779@qq.com','1220237603@qq.com']  #列表形式填写收件人，发送给单个人也以列表形势传送
    host = "smtp.163.com"
    pwd = "123456hzs"
    file_name = file
    SendMail(content,subject,from_addr,to_addr,host,pwd,file_name).send_mail()
