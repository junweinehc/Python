Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import smtplib

sender_email = ""
rec_email = ""

password = input(str("Enter your password: "))
message = "HI m python"

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email, password)
print("Correct logins")
server.sendmail(sender_email, rec_email, message)
print("Email has been sent to: ",rec_email)


