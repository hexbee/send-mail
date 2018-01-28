'''
Title: send mail from QQ mail by python3
Date: 2017-01-28
'''

import requests
import time
import random


class QQMail(object):
    def __init__(self, sendmailname, sendname, sid, to, subject, content, cookie):
        self.to = to
        self.subject = subject
        self.content = content
        self.sid = sid
        self.sendmailname = sendmailname
        self.sendname = sendname
        self.url = 'https://mail.qq.com/cgi-bin/compose_send?sid={sid}'.format(sid=self.sid)
        self.header = {
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://mail.qq.com',
                'referer': 'https://mail.qq.com/zh_CN/htmledition/ajax_proxy.html?mail.qq.com&v=140521',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
        }
        self.cookie = cookie
        self.data = {
                    '922a39862ba3247977a6e4d4992ccad5':'8d60b8fd8fd5c62e500722201a71e662',
                    'sid':self.sid,
                    'from_s':'cnew',
                    'to':self.to,
                    'subject':self.subject,
                    'content__html':self.content,
                    'sendmailname':self.sendmailname,
                    'savesendbox':'1',
                    'actiontype':'send',
                    'sendname':self.sendname,
                    'acctid':'0',
                    'separatedcopy':'false',
                    's':'comm',
                    'hitaddrbook':'0',
                    'selfdefinestation':'-1',
                    'domaincheck':'0',
                    # 'cgitm':'1517147995170',
                    # 'clitm':'1517147995142',
                    # 'comtm':str(int(time.time() * 1000)),
                    'logattcnt':'0',
                    'logattsize':'0',
                    'cginame':'compose_send',
                    'ef':'js',
                    't':'compose_send.json',
                    'resp_charset':'UTF8'
    }

    
    def send(self):
        time.sleep(random.randint(1,5))
        html = requests.request('POST', self.url, data=self.data, headers=self.header, cookies=self.cookie)
        print(html.status_code)
        print(html.text)


def main():
    instance = QQMail(
        sendmailname = '******@qq.com',
        sendname = 'Robot-I',
        sid='*************',
        to='***@***.com',
        subject='*******',
        content='*******',
        cookie={
            'cookie': '***'
        }
    )
    instance.send()


if __name__ == '__main__':
    main()
