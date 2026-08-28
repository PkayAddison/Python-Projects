import os
import requests
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()
'''
API_KEY = os.getenv("EXCHANGE_API_KEY")

url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

response = requests.get(url)

data = response.json()

ghs_rate = data['conversion_rates']['GHS']
euro=data['conversion_rates']['EUR']
british_pound = data['conversion_rates']['GBP']
print(f"1USD = {ghs_rate} GHS")
print(f"1USD = {euro} EUR")
print(f"1USD = {british_pound} GBP")
'''
'''
API_KEY = os.getenv("EXCHANGE_API_KEY")
sender_email=os.getenv("EMAIL_ADDRESS")
app_password=os.getenv("EMAIL_APP_PASSWORD")
msg = EmailMessage()
msg['Subject'] = 'Daily Exchange Rate Update'
msg['from'] = sender_email
msg['to'] = sender_email
msg.set_content("1 USD = 11.18 GHS (test message)")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(sender_email, app_password)
    smtp.send_message(msg)

print("Email sent!")
'''

API_KEY = os.getenv("EXCHANGE_API_KEY")
sender_email=os.getenv('EMAIL_ADDRESS')
app_password= os.getenv('EMAIL_APP_PASSWORD')

def get_exchange_rates():
    url =f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
    response =requests.get(url, timeout=10)
    response.raise_for_status()
    data=response.json()
    return data['conversion_rates']
def send_mail(body_text):
    msg=EmailMessage()
    msg['Subject'] = 'Daily Exchange Rate Update'
    msg['From'] = sender_email
    msg['To'] = sender_email
    msg.set_content(body_text)
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)
        
def main():
    try:
        rates = get_exchange_rates()
        body = (
            f"1 USD = {rates['GHS']} GHS\n"
            f"1 USD = {rates['EUR']} EUR\n"
            f"1 USD = {rates['GBP']} GBP"
        )
        send_mail(body)
        print("Success: email sent.")
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
    except (smtplib.SMTPException, OSError) as e:
        print(f"Email error: {e}")
        
if __name__ == "__main__":
    main()