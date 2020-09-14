# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


# 发送邮件
# TODO 发送邮件服务
class EmailUtil:
    def __init__(self, sender, password, receiver):
        self.sender = sender
        self.password = password
        self.receiver = receiver

    def send_mail(self):
        ret = True
        try:
            msg = MIMEText('邮件内容', 'plain', 'utf-8')
            msg['from'] = formataddr(['fromwen', self.sender])
            msg['to'] = formataddr(['fk', self.receiver])
            server = smtplib.SMTP_SSL('smtp.qq.com', 465)
            server.login(self.sender, self.password)
            server.sendmail(self.sender, [self.receiver, ], msg.as_string())
            server.quit()
        except Exception:
            ret = False
        return ret


if __name__ == '__main__':
    EmailUtil('2660670981@qq.com', '', '1483319587@qq.com').send_mail()
