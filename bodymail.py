import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

from_add="bobbyganthala@gmail.com"
password="Subhash@8969"
too="bobbyganthala@gmail.com"
msg=MIMEMultipart()
msg["From"]=from_add
msg["To"]=too
msg["subject"]="sample mail"
body="s1text"
msg.attach(MIMEText(body))
filename="s1.txt"
attach=open(filename,"rb")
msg.attach(MIMEBase(filename,attach))
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(from_add,password)
server.send_message(msg)
server.quit()
