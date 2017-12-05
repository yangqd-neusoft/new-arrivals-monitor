#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
  
HOST = "smtp.163.com"
SUBJECT = "%s" % time.asctime(time.localtime(time.time()))
TO = "glqliqian@163.com"
FROM = "YangqdFight@163.com"

class sendMail(object):
    """docstring for sendMail"""
    def __init__(self, dirList=[]):
        self.dirList = dirList
        self.msg = None

    def buildMSG(self):
        imgCount = 1
        self.msg = MIMEMultipart('related')
        self.msg['Subject'] = SUBJECT
        self.msg['From']=FROM
        self.msg['To']=TO

        for fileDir in dirList:
            dataCount = str(imgCount)+'.'
            msgText = MIMEText(dataCount+open("xiaomianao\\%s\\info.txt" % fileDir, "rb").read(), "plain", "utf-8")
            msgText["Content-Type"] = "application/octet-stream"
            msgAddImage = MIMEImage(open("xiaomianao\\%s\\photo.jpg" % fileDir, 'rb').read())
            msgAddImage.add_header('Content-ID', "image%s" % str(imgCount))
            msgImage = MIMEText("<br><img src=\"cid:image%s\"><br>" % str(imgCount),"html","utf-8")
            self.msg.attach(msgText)
            self.msg.attach(msgAddImage)
            self.msg.attach(msgImage)
            imgCount = imgCount+1

    def sendMail(self):
        try:
            server = smtplib.SMTP()
            server.connect(HOST, '25')
            server.starttls()
            server.login("YangqdFight@163.com","19941122yang")
            server.sendmail(FROM, TO, self.msg.as_string())
            server.quit()
            fo = open("log.txt", "a")
            fo.write( time.asctime(time.localtime(time.time())) + 'send mail success' + '\n' )
            fo.close()
        except Exception, e:
            fo = open("log.txt", "a")
            fo.write( time.asctime(time.localtime(time.time())) + str(e) + '\n' )
            fo.close()
