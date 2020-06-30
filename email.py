#!/usr/bin/env python
# encoding: utf-8

import os
import time
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


log_file = '/var/log/mysql/mysql_slow_query.log'
local_tmp_file = '/var/log/mysql/mysql_slow_query_tmp.log'

Receivers = ['zhoukun@ehousechina.com']


def send_email():
    html = """
    <!DOCTYPE html>
       <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>yun慢sql日志</title>
            <h1>复制到编辑器中查看结构数据</h1>
        </head>
        <body>
        </body
    </html>"""
    mail_host = 'smtp.ehousechina.com'
    mail_user = 'cyjz@ehousechina.com'
    mail_pass = 'jqXxNGyatvDnfE1C'
    mail_port = 994

    sender = 'cyjz@ehousechina.com'
    receivers = Receivers

    message = MIMEMultipart()
    message['From'] = Header('cyjz@ehousechina.com', 'utf-8')
    message['To'] = Header(','.join(receivers), 'utf-8')
    subject = 'yun慢sql日志'
    message['Subject'] = Header(subject, 'utf-8')
    message.attach(MIMEText(html, 'html', 'utf-8'))

    att = MIMEText(open(local_tmp_file, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="mysql_slow_query.log"'
    message.attach(att)

    smtp = smtplib.SMTP_SSL(mail_host, mail_port)
    smtp.set_debuglevel(True)
    smtp.login(mail_user, mail_pass)
    smtp.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"


def main():
    if os.path.exists(local_tmp_file):
        os.remove(local_tmp_file)
    now = int(time.time()) - 3000
    time_compile = re.compile("SET timestamp=(\d+);")
    tag = False
    ff = open(local_tmp_file, 'a')
    with open(log_file, 'r') as f:
        for line in f.readlines():
            if not tag:
                if re.search(time_compile, line):
                    line_time = re.search(time_compile, line).group(1)
                    if now < int(line_time):
                        tag = True
            if tag:
                ff.write(line)
    ff.close()

    if tag:
        send_email()


if __name__ == '__main__':
    main()


