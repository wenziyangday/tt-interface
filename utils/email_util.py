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
        # attachs = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
        # attachs['Content-Type'] = 'application/octet-stream'
        # attachs['Content-Disposition'] = 'attachment; filename="test.txt"'
        try:
            msg = MIMEText('这是衣蛾试试', 'plain', 'utf-8')
            msg['from'] = formataddr(['张三', self.sender])
            msg['to'] = formataddr(['李四', self.receiver])
            # msg.attach(attachs)
            server = smtplib.SMTP_SSL('smtp.qq.com', 465)
            server.login(self.sender, self.password)
            server.sendmail(self.sender, [self.receiver, ], msg.as_string())
            server.quit()
        except Exception:
            ret = False
        return ret


if __name__ == '__main__':
    EmailUtil('1483319587@qq.com', 'aafmaklpjfcjhiif', 'Vincent.wen@wayz.ai').send_mail()
