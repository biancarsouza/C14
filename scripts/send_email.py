import os
import smtplib
from email.mime.text import MIMEText

def send_notification():
    # Lê o e-mail do ambiente
    recipient = os.getenv("NOTIFY_EMAIL")
    if not recipient:
        raise ValueError("Variável de ambiente NOTIFY_EMAIL não definida!")

    # Cria a mensagem
    msg = MIMEText("Pipeline executado com sucesso!")
    msg["Subject"] = "Status do Pipeline"
    msg["From"] = "ci-cd@example.com"
    msg["To"] = recipient

    # Aqui usamos localhost como exemplo. No mundo real, configure SMTP.
    try:
        with smtplib.SMTP("localhost") as server:
            server.sendmail("ci-cd@example.com", [recipient], msg.as_string())
        print("Notificação enviada com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

if __name__ == "__main__":
    send_notification()
