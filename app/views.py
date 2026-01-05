from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

from django.shortcuts import render, redirect

from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils import timezone
from email.mime.image import MIMEImage
import os

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about-us.html')

def career(request):
    return render(request,'career.html')

def contact(request):
    return render(request,'contact-us.html')

def form_contact(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        subject = "Welcome to Our Company"

        logo_url = 'D:/Neminath/projectfolder/static/assets/images/NeminathLogo.png'
        html_content = render_to_string("contactemail.html", {
            'subject': subject,
            'name':name,
            'logo_url':logo_url,
            'year': timezone.now().year,

        })
        text_content = strip_tags(html_content)  # fallback for plain text email

        email = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
        email.attach_alternative(html_content, "text/html")
        logo_path = os.path.join(settings.BASE_DIR, 'static/assets/images/NeminathLogo.png')
        with open(logo_path, 'rb') as f:
            logo = MIMEImage(f.read())
            logo.add_header('Content-ID', '<companylogo>')
            logo.add_header('Content-Disposition', 'inline', filename="logo.png")
            email.attach(logo)
        email.send()
 
        # a = send_mail(
        #         subject='Enquire',
        #         message=message,
        #         from_email=settings.EMAIL_HOST_USER,
        #         recipient_list=[email]

        # )
        # print(a)
        return redirect('home')
    else:
        return redirect('home')




# def send_professional_email(to_email):
#     subject = "Welcome to Our Company"
#     message = "Thank you for joining us. We are excited to have you!"
#     logo_url = "static/assets/images/NeminathLogo.png" 
#     html_content = render_to_string("contactemail.html", {
#         'subject': subject,
#         'message': message,
#         'logo_url': logo_url,
#         'year': timezone.now().year,
#     })
#     text_content = strip_tags(html_content)  # fallback for plain text email

#     email = EmailMultiAlternatives(subject, text_content, 'Your Company <yourcompanyemail@gmail.com>', [to_email])
#     email.attach_alternative(html_content, "text/html")
#     email.send()



    
        

# Create your views here.
