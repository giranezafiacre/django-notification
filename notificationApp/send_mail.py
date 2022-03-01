import smtplib, ssl

def send_mail(receiver_email):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "fiacregiraneza@gmail.com"
    password = "jumongo1@"
    message = """From: From Fiacre <"""+sender_email +""">
To: To """+ sender_email +"""  <"""+ sender_email +""">
Subject: NOTIFICATION

    this is notification message"""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
