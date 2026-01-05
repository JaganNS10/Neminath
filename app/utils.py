from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from email.mime.image import MIMEImage

def send_contact_email(name, email, message):
    subject = f'New Contact Form Submission from {name}'
    from_email = settings.EMAIL_HOST_USER
    to_email = email  # where you want to receive messages

    # Render HTML email template
    html_content = render_to_string('templatescontact_email.html', {
        'name': name,
        'email': email,
        'message': message
    })

    msg = EmailMultiAlternatives(subject, '', from_email, [to_email])
    msg.attach_alternative(html_content, "text/html")

    # Attach logo
    with open('static/assets/images/NeminathLogo.png', 'rb') as f:
        logo = MIMEImage(f.read())
        logo.add_header('Content-ID', '<logo_image>')
        logo.add_header('Content-Disposition', 'inline', filename='logo.png')
        msg.attach(logo)

    msg.send()