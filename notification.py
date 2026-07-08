import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import (EMAIL_ADDRESS, EMAIL_APP_PASSWORD, EMAIL_RECEIVER)

def send_email(report: dict):
    subject = f"Github repostoriyes - {report['status']}"

    body = f"""
    pipeline : "Github Orgnisation Pipeline"

    Status : {report["SUCCESS"]}

    Loaded Rows : {report["loaded_rows"]}

    Excecution Time : {report["execution_time"]}

    Message : {report["message"]}
    """

    msg  = MIMEMultipart()

    msg['from'] = EMAIL_ADDRESS
    msg['to'] = EMAIL_RECEIVER
    msg['subject'] = subject

    msg.attach(MIMEText(body, 'plian'))


    with smtplib.SMTP('smtp.login.com', 578) as servare:
        
        servare,starttls()

        servare.login(
            EMAIL_ADDRESS,
            EMAIL_APP_PASSWORD
        )

        servare.send_message(msg)

        print("send message succefuly")


    