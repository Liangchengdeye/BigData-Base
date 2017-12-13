# -*- coding: utf-8 -*-
#!/usr/bin/env python
# 发送邮件模块
import smtplib
import os 
import sys
from email.mime.text import MIMEText
from email.header import Header
sys.path.append(os.path.dirname(os.getcwd()))
from config.conf import get_args


def sendmail(content, reciever, subject):
    email_alert = get_args("email_alert")
    mail_host = email_alert["mailhost"]
    mail_user = email_alert["username"]  
    mail_pass = email_alert["password"]   
    sender = email_alert["username"]
    receivers = reciever    
    message = MIMEText(content, 'html', 'utf-8')
    message['From'] = email_alert["from"]
    message['To'] = ','.join(receivers)
    message['Subject'] = Header(subject, 'utf-8')
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, email_alert["port"])
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())

# test
if __name__ == '__main__':
    # 调用方式
    # content = '''
    #     <p>大家好!</p>
    #     <p>这里是邮件正文</p>'''
    # reciever = ['xuhaifeng@nutfin.cn']
    # subject = '邮件标题'
    # sendMails.sendmail(content, reciever, subject)
    pass
