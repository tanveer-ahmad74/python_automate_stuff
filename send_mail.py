import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail(smtpHost, smtpPort, mailUname, mailPwd, fromEmail, mailSubject, mailContentHtml, recepientsMailList):
    msg = MIMEMultipart()
    msg['From'] = fromEmail
    msg['To'] = ','.join(recepientsMailList)
    msg['Subject'] = mailSubject
    msg.attach(MIMEText(mailContentHtml, 'html'))


    # Send message object as email using smptplib
    s = smtplib.SMTP(smtpHost, smtpPort)
    s.starttls()
    s.login(mailUname, mailPwd)
    msgText = msg.as_string()
    sendErrs = s.sendmail(fromEmail, recepientsMailList, msgText)
    s.quit()

    # check if errors occured and handle them accordingly
    if not len(sendErrs.keys()) == 0:
        raise Exception("Errors occurred while sending email", sendErrs)


# mail server parameters
smtpHost = "smtp.gmail.com"
smtpPort = 587
mailUname = 'ta551682@gmail.com' #From 
mailPwd = 'vbhbrlafebiosbsp'    
fromEmail = 'usmaan.arsh908@gmail.com' #to send


# mail body, recepients, attachment files
mailSubject = "Test subject"
mailContentHtml = "Hi, Hope u are fine. <br/> This is a <b>test</b>" \
                  "mail from python script using an awesome library called" \
                  " <b>smtplib</b>"

recepientsMailList = ["usmaan.arsh908@gmail.com"]
sendEmail(smtpHost, smtpPort, mailUname, mailPwd, fromEmail,
          mailSubject, mailContentHtml, recepientsMailList)

print("execution complete...")
