import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

def send_email():
    sender = 'deepanvinayagam1411@gmail.com'
    recipient = 'deepanvinayagam1411@gmail.com'
    subject = 'Pytest Selenium Report'
    app_password = 'bhxu nskk kmyx usyf'

    # Create email
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    body = MIMEText('Test execution completed. See attached report.', 'plain')
    msg.attach(body)

    # Attach the HTML report
    with open("report.html", "rb") as f:
        part = MIMEApplication(f.read(), _subtype="html")
        part.add_header('Content-Disposition', 'attachment', filename="report.html")
        msg.attach(part)

    # Send email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, app_password)
            server.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Email failed: {e}")

if __name__ == "__main__":
    send_email()
