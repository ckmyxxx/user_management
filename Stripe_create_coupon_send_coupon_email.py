# Stripe-affiliate

import stripe

import pandas as pd

from datetime import datetime

# need to connect ot AWS private key management or Vault to retrieve this API key

stripe.api_key = ""

def get_stripe_customer_email():

    # this get all the email

    customer_dict = stripe.Customer.list(limit=1)

    customer_email = []

    for i in range(len(customer_dict)):
        customer_email.append(customer_dict.data[i]['email'])

    return customer_email


def get_stripe_customer_id():

    # this get all the email

    customer_dict = stripe.Customer.list(limit=2)

    customer_id = []

    for i in range(len(customer_dict)):

        customer_id.append(customer_dict.data[i]['id'])

    return customer_id

def create_coupon_for_each_stripe_customer():

# manually put the customer_id like 'cus_xxxxxxx' into the following list

# need to figure out a way to get all the active customer IDs and convert them into the lost below

    customer_id =['cus_xxxxxxx']

    for customer in customer_id:

        try:

            print(customer)

            customer_dict = stripe.Customer.retrieve(customer)

            # print(customer_dict)

            customer_email = customer_dict['email']

            print(customer_email)

            id = customer_dict['id']

            coupon_code = id

            stripe.Coupon.create(
                id=id,
                currency="usd",
                duration="once",
                name=id,
                percent_off=10
            )

            send_affiliate_coupon_email_html(customer_email, coupon_code)

        except Exception:

            pass

    return


def send_affiliate_coupon_email_html(email, coupon):

    # email tutorial: https://realpython.com/python-send-email/

    import smtplib, ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    sender_email = "moneypig001@gmail.com"
    receiver_email = email

    # need to connect ot AWS private key management or Vault to retrieve this API key
    
    password = '' #'#input("Type your password and press enter:")

    message = MIMEMultipart("alternative")
    message["Subject"] = "Welcome to Moneypig Trading Affiliate Program"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
Dear valued customer,
Thank you for supporting Moneypig Trading! 

Refer your friends to Moneypig Trading and we'll reward you both. Start referring by sharing your affiliate coupon code:

{}
""".format(coupon)
    html = """\
<html>

  <body>
    <p>Dear valued customer,<br>
    
    <p></p>    
       
       Thank you for supporting Moneypig Trading! <br>
       
    <p></p>
       
       Refer your friends to Moneypig Trading and we'll reward you both. <br>

    <p></p>

       Start referring by sharing your affiliate coupon code <br>

    <p></p>
    <p></p>

       {}
       
    <p></p>
    <p></p>
    
    Your friend will get a one-time 10% off using the coupon code above. Eligible for the first-time order only. 
         
    <p></p>
       
       Once your friend becomes a paid member using your referral coupon code after the free trial period (equal to the word "successful" below), you can get <br>
       
       <p></p> 
       
       $60 for each successful daytrading referral 
       
       <p></p> 
       
       $30 for each successful swing trading referral 
       <p></p> 
       
       $10 for each successful long term investment referral 
    
        <p></p>   
    
       The payment will be issued by Paypal or Zelle at the end of each calendar quarter
       
       <p></p>
       
       Please make sure you have a Paypal or Zelle account with the email you registered to MoneypigTrading. Thank you!
    
        <p></p>
       
       By joining the Moneypig Trading affiliate program, you agree to our Terms listed in https://www.moneypigtrading.com/affiliate-policy <p></p>

       <p></p>
       
       Best,
       <p></p>
       Moneypig

  </body>
</html>
""".format(coupon)

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

    print('successfully send out emails')

    return


create_coupon_for_each_stripe_customer()
