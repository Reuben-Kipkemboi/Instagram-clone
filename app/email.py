from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(user,receiver):
    # Creating message subject and sender
    subject = 'Welcome to Instagram by Reuby'
    sender = 'kipkemboireuben866@gmail.com'

    #passing in the context variables
    text_content = render_to_string('email/email.txt',{"name": user})
    html_content = render_to_string('email/email.html',{"name": user})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()