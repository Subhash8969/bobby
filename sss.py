#'''import pandas as pd
#df = pd.read_excel(r'C:\Users\Bobby\Desktop\sample.xlsx')
#print(df)'''
#import smtplib
'''from email.message import EmailMessage

msg=EmailMessage()
msg["Subject"]="sending mails"
msg["From"]="bobbyganthala@gmail.com"
msg["To"]="naredladivyareddy@gmail.com"
msg.set_content("email from subhash")
smtplib.SMTP_SSL("smtp.gmail.com",587)
server.login("bobbyganthala@gmail.com","subhashganthala")
server.send_message(msg)'''

'''s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("bobbyganthala@gmail.com","Subhash@8969")
message="sample email"
s.sendmail("bobbyganthala@gmail.com","bobbyganthala@gmail.com",message)
s.quit()'''
'''import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from_add="bobbyganthala@gmail.com"
password="Subhash@8969"
too="bobbyganthala@gmail.com"
msg=MIMEMultipart()
msg["From"]=from_add
msg["To"]=too
msg["subject"]="sample mail"
body="body"
msg.attach(MIMEText(body))
filename="sample.xlsx"
attachment=open(filename,"rb")
p=MIMEBase("application","octet-stream")
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header("content-disposition","attachment; filename= %s"% filename)
msg.attach(p)
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(from_add,password)
text=msg.as_string()
server.send_message(msg)
server.quit()'''



a=5
b=6
sum= a+b
print("sum of a and b %s", %sum)













