import smtplib


content = "whatever"

mail = smtplib.SMTP("smtp.gmail.com" , 587)
mail.ehlo()
mail.starttls()
emailAddress = "blank@gmail.com"
password = "blank"
mail.login(emailAddress , password)
mail.sendmail("from_Email@gmail.com" , "to_Email@gmail.com", content )






