import time
import os
import requests
from bs4 import BeautifulSoup
from exchangelib import DELEGATE, Account, Credentials, Configuration, NTLM, Message, Mailbox, HTMLBody
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
import sys

#This sentence is used to eliminate errors in SSL certificates
#BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter

# input your account such as \lemon
cred = Credentials(r'lemon.1.lin@nokia-sbell.com', 'Qazwsx_2')

config = Configuration(server='mail.int.nokia-sbell.com', credentials=cred, auth_type=NTLM)
account = Account(
    primary_smtp_address='lemon.1.lin@nokia-sbell.com', config=config, autodiscover=False, access_type=DELEGATE
)

# Here is the file path used to send HTML mail
localtime = time.localtime(time.time())
month = str(localtime[1])
day = str(localtime[2])
releaseNum = sys.argv[1]
if localtime[1] < 10:
    month = "0" + str(localtime[1])

if localtime[2] < 10:
    day = "0" + str(localtime[2])
datePath = str(localtime[0])+"/"+ month+"/"+ day


def sendMailByType(niddType):
    webPath = "http://10.159.215.152/NIDD-extractions/"+ niddType +"/release-"+ releaseNum + "/" + datePath +"/finalResult.html"
    #webPage = urllib.request.urlopen(webPath) #open link
    #htmlContent = webPage.read() #Get page content

    response = requests.get(webPath)
    htmlContent = response.text
    # send email
    message = Message(
        account=account,
        folder=account.sent,
        subject=niddType + u' definitions - Daily extraction from NIDD',
        body=HTMLBody(htmlContent),
        to_recipients=[Mailbox(email_address='lemon.1.lin@nokia-sbell.com'),
                       Mailbox(email_address='jinghuan.liu@nokia-sbell.com'),
                       Mailbox(email_address='hui.6.li@nokia-sbell.com'),
                       Mailbox(email_address='yujuan.gao@nokia-sbell.com'),
                       Mailbox(email_address='mengna.huang@nokia-sbell.com')]
    )
    message.send_and_save()

sendMailByType("PM")
