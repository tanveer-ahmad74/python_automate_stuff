import smtplib, ssl

def send_email():
    port = 465
    smtp_server = 'smtp.gmail.com'
    sender_email = '@gmail.com'
    receiver_email = '@gmail.com'
    password = 'Google_APP_PASSWORD_HERE'
    message= 'this is the message for rana handsome guy'

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            print('email sent!')
        except:
            print("could not login or send the mail.")

if __name__ == '__main__':
        send_email()

#Email that send from here probably find in SPAM folder
