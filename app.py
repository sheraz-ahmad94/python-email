from ast import Return
from email.message import EmailMessage
from multiprocessing import context
from optparse import Option
from pickle import TRUE
import ssl
import smtplib
import re


regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def email_checker(email):
    if (re.fullmatch(regex, email)):
        return 'VALID'
    else:
        return 'INVALID'


email_sender = 'SENDER_EMAIL_HERE'
email_password = 'GMAIL_APP_PASSWORD'

option = 0
validity = 'none'

while option != '2':

    print('-- Menu --')
    print('1: Send a New Email\n2: Exit\n\nSelect: ')
    option = input()
    
    if option == '1':
        

        email_receiver = input ("Please Enter Receiver's Email: ")

        validity = email_checker(email_receiver)

        while validity == 'INVALID':
            print('The Email is Invalid. \nPlease Enter correct Email Address.\n\n(Press 2 to Exit)')
            email_receiver = input ("\nPlease Enter Receiver's Email: ")
            if email_receiver == '2':
                quit()
            validity = email_checker(email_receiver)

        subject = input('Enter Subject: ')

        body = input('Email Content: ')

        em = EmailMessage()

        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

        print('Email Sent Successfully!')


    elif option == '2':
        option = '2'

    else:
        print('Input Error. Select Correct Option')