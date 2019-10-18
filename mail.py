import smtplib
from email.mime.text import MIMEText

to = 'receiver@mail.com'
sender = 'sender@mail.com'
message = 'We\'re sending an email through Cron!'
subject = 'Cron Mail'

msg = MIMEText(message)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = to

s = smtplib.SMTP('mail-relay.mail.com')
s.ehlo()
s.starttls()
s.ehlo()
s.sendmail(sender, to, msg.as_string())
s.quit()
