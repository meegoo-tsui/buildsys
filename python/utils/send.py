#! /usr/bin/python
#coding=utf-8

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    send.py
#  @brief   send mail via smtp
#  @author  meegoo.tsui@gmail.com
#  @date    2013/07/17
#  http://elinux.org/RPi_Email_IP_On_Boot_Debian
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import smtplib
from   email.mime.text import MIMEText

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## send mail.
class send:
    ## The constructor.
    def __init__(self):
        ## email address for send to
        self.to      = ""
        ## email address for from
        self.me      = ""
        ## password
        self.pwd     = ""
        ## smtp server name
        self.smtp    = ""
        ## smtp server port
        self.port    = 0
        ## mail subject
        self.subject = ""
        ## mail comment
        self.info    = ""

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    ## send
    def send(self):
        smtpserver = smtplib.SMTP(self.smtp, self.port)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(self.me, self.pwd)

        msg            = MIMEText(self.info)
        msg['Subject'] = self.subject
        msg['From']    = self.me
        msg['To']      = self.to

        smtpserver.sendmail(self.me, [self.to], msg.as_string())
        smtpserver.quit()

        return

## object of class path.
send = send()

#-------------------------------------------------------------------------------
