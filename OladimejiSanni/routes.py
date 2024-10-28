from flask import Blueprint
from flask import render_template, request, flash, jsonify
from .models import Contact
from .models import db
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

bp = Blueprint('bp', __name__)


def send_mail(name, email, subject):
    # Email credentials
    sender_email = "oladimejisanni@ymail.com"
    receiver_email = email
    password = "vimsxyjiegytieur"

    username = 'OladimejiSanni-ePortfolio'

    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = f"RE: {subject}"

    body = f"Hi {name},\n\nThanks so much for reaching out! This auto-reply is just to let you know that I have " \
           f"received your email and will get back to you as soon as possible.\n\nIf you have any additional " \
           f"information that you think will facilitate collaboration " \
           "between us, please feel free to reply to this email.\n\nWe look forward to working with you.\n\nCheers," \
           "\n\nOladimeji Sanni"
    msg.attach(MIMEText(body, 'plain'))

    # Connect to Yahoo's SMTP server
    server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    server.starttls()
    server.login(sender_email, password)

    # Send the email
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)

    # Disconnect from the server
    server.quit()

    return "Email sent successfully!"


@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        existing_email = Contact.query.all()
        email_list = []
        for item in existing_email:
            check_email = item.email
            email_list.append(check_email)
        if email in email_list:
            msg = f"The Email {email} have earlier contacted us"
            flash(f"{msg}", "error")
        else:
            new_contact = Contact(name, email, subject, message)
            db.session.add(new_contact)
            db.session.commit()
            msg = 'Thank you for contacting us. Your message has been received'
            flash(f"{msg}", "success")
            mail_service = send_mail(name, email, subject)
            print(mail_service)
    return render_template('index.html')


@bp.route('/fetch_all_contacts/', methods=['GET', 'POST'])
def fetch_all_contacts():
    contacts = Contact.query.all()
    contact_list = []
    for contact in contacts:
        dic = {'name': contact.name, 'email': contact.email, 'subject': contact.subject, 'message': contact.message}
        contact_list.append(dic)
    return jsonify(contact_list)
