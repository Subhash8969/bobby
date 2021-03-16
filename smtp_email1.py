#sending email using smtp library


import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)

s. starttls()

s.login("bobbyganthala@gmail.com","Subhash@8969")

message = "Subject:ringraziandoti per la tua ospitalita"

s.sendmail("bobbyganthala@gmail.com","naredladivyareddy@gmail.com",message)

s.quit()
