import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    from_email = "inserir email"
    password = "inserir senha"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

if __name__ == "__main__":
    subject = "Notificação de apoio social"
    body = "Prezada família, estamos oferecendo suporte emergencial. Entre em contato conosco para mais informações."
    send_email(subject, body, "email@gmail.com")
