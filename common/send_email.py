#send_mail.py
#构造邮件内容 MIMETEXT
#发送邮件：登录smtp服务器(账号、密码)--发送--关闭链接 smtplib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# 发送邮件类
class SendMail:
    def __init__(self,content,subject,from_addr,to_addr,host,pwd,file_name=''):
        self.content = content
        self.subject = subject
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.host = host
        self.pwd = pwd
        self.file_name = file_name

    def make_multi(self):#构造附件邮件
        msg = MIMEMultipart()
        msg['Subject'] = self.subject
        msg['From'] = self.from_addr
        msg['To'] = ", ".join(self.to_addr)
        #添加文本内容
        msg_1 = MIMEText(self.content)
        msg.attach(msg_1)
        #添加附件
        msg_2 = MIMEApplication(open(self.file_name,'rb').read())
        msg_2.add_header('Content-Disposition','attachment',filename=self.file_name)
        msg.attach(msg_2)
        return msg

    def make_text(self):#构造纯文本邮件
        msg = MIMEText(self.content)
        msg['Subject'] = self.subject
        msg['From'] = self.from_addr
        msg['To'] = ", ".join(self.to_addr)
        return msg

    def send_mail(self):
        #判断file_name如果为空，则发送纯文本邮件，不为空则发送附件邮件
        if self.file_name == '':
            msg = self.make_text()
        else:
            msg = self.make_multi()
        s = smtplib.SMTP_SSL(self.host)
        s.login(self.from_addr,self.pwd)
        s.sendmail(self.from_addr,self.to_addr,msg.as_string())
        s.close()
