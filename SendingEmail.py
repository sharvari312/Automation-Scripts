import time
import yagmail
import os

sender="sender@gmail.com"
receiver="receiver@gmail.com"
subject="This is the subject"
contents="HI, There !"
yag=yagmail.SMTP(user=sender,password=os.getenv('PASSWORD'))
yag.send(to=receiver,subject=subject,contents=contents)
print("Email Send")
    
