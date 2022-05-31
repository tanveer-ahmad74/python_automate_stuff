import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import keys
import pandas as pd

def get_crypto_rates(base_currency='PKR', assets='BTC,ETH,XRP'):
    url = 'https://api.nomics.com/v1/currencies/ticker'

    payload = {'key': keys.NOMICS_API_KEY, 'convert': base_currency, 'ids': assets, 'interval': '1d'}
    response = requests.get(url, params=payload)
    data = response.json()
    print(data)
    crypto_currency, crypto_price, crypto_timestamp = [], [], []

    for asset in data:
        crypto_currency.append(asset['currency'])
        crypto_price.append(asset['price'])
        crypto_timestamp.append(asset['price_timestamp'])

    raw_data = {
        "assets": crypto_currency,
        'rates': crypto_price,
        "timestamp": crypto_timestamp
    }

    df = pd.DataFrame(raw_data)
    return df

def set_alert(dataframe, asset, alert_high_price):
    crypto_value = float(dataframe[dataframe['assets'] == asset]['rates'].item())

    details = f'{asset}: {crypto_value}, Target Value Reached: {alert_high_price}'

    if crypto_value >= alert_high_price:
        print(details + '<< Target Value Reached..!')
        return details
    else:
        print(details)

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
mailPwd = 'vbhbrfadsfasdfp'    #APp_Passwprd_of_Gmail
fromEmail = 'usmaan.arsh908@gmail.com' #to send


df = get_crypto_rates()
value1 = set_alert(df, 'BTC', 607064190.50)
value2 = set_alert(df, 'ETH', 386128.92)
value3 = set_alert(df, 'XRP', 80.00)

# mail body, recepients, attachment files
mailSubject = "Test subject"
mailContentText = f"Hi...!?\n" \
                  f"BTC: {value1}\n" \
                  f"ETH: {value2}\n"  \
                  f"XRP: {value3}"

recepientsMailList = ["usmaan.arsh908@gmail.com"]
sendEmail(smtpHost, smtpPort, mailUname, mailPwd, fromEmail,
          mailSubject, mailContentHtml, recepientsMailList)

print("execution complete...")
