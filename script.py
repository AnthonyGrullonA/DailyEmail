import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Configuración de la cuenta de correo
email_address = "correo_emisor@gmail.com"
password = "password"
recipient_email = "correo_destino@gmail.com"
subject = (
    "Solicitud de vacantes TI - Perfil Profesional en TI: Experiencia y Conocimientos"
)


# Función para enviar correo con cuerpo y documento adjunto
def send_email(body):
    # Configuración del correo
    msg = MIMEMultipart()
    msg["From"] = email_address
    msg["To"] = recipient_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "html"))  # Cambio a HTML

    # Adjuntar documento PDF
    filename = "ANTHONY GRULLON - INFRAESTRUCTURA .pdf"
    attachment = open(filename, "rb")
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= {filename}")
    msg.attach(part)

    # Configuración del servidor SMTP de Gmail
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Iniciar el cifrado TLS
    server.login(email_address, password)  # Autenticar con el correo y la contraseña

    # Enviar correo
    server.sendmail(email_address, recipient_email, msg.as_string())
    server.quit()


# Obtener contenido del archivo de texto para el cuerpo del correo
def get_email_body():
    with open(
        "cuerpo_correo.txt", "r", encoding="utf-8"
    ) as file:  # Asegurar la codificación UTF-8
        body = file.read()
    return body


# Ciclo para enviar correo cada 24 horas
while True:
    body = get_email_body()
    send_email(body)
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    next_time = time.time() + 24 * 60 * 60
    next_time_formatted = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(next_time))
    print(
        f"Correo enviado exitosamente a las {current_time}. Próximo envío programado para {next_time_formatted}."
    )
    # Esperar 24 horas antes de enviar el siguiente correo
    time.sleep(24 * 60 * 60)
