import os
import smtplib
import ssl
from email.mime.text import MIMEText

def send_notification():
    recipient = os.getenv("NOTIFY_EMAIL")
    sender_email = os.getenv("SMTP_USER")
    password = os.getenv("SMTP_PASS")

    if not all([recipient, sender_email, password]):
        raise ValueError("Variáveis de ambiente NOTIFY_EMAIL, SMTP_USER ou SMTP_PASS não definidas!")

    msg = MIMEText("Pipeline executado com sucesso! ✅")
    msg["Subject"] = "Status do Pipeline"
    msg["From"] = sender_email
    msg["To"] = recipient

    smtp_server = "smtp.gmail.com"
    port = 587
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.sendmail(sender_email, recipient, msg.as_string())
    except Exception as e:
        # não derruba o pipeline em caso de falha
        exit(0)

if __name__ == "__main__":
    send_notification()
