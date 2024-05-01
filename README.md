# Script de Envío de Correos con Python

Este script en Python utiliza la biblioteca `smtplib` para enviar correos electrónicos a través de un servidor SMTP. El objetivo principal de este proyecto es automatizar el envío periódico de correos electrónicos que incluyen un cuerpo de texto en formato HTML y un documento adjunto, específicamente un archivo PDF.

## Requisitos

- Python: Debes tener Python instalado en tu sistema.
- Cuenta de correo: Necesitas una cuenta de correo electrónico configurada para permitir el envío a través de SMTP.

## Configuración

Realiza los siguientes pasos antes de ejecutar el script:

1. **Variables de Configuración:** Modifica las variables `email_address`, `password`, `recipient_email`, `subject` en el script con los datos de tu cuenta de correo electrónico y del destinatario.
2. **Adjunto PDF:** Coloca el archivo PDF que deseas enviar en el mismo directorio que el script con el nombre `documento.pdf`.
3. **Cuerpo del Correo:** Crea un archivo de texto llamado `cuerpo_correo.txt` en el mismo directorio que el script. Este archivo debe contener el cuerpo del correo en formato HTML.

## Ejecución

Para ejecutar el script, abre una terminal en el directorio donde se encuentra el script y ejecuta el siguiente comando:

```python
python script_envio_correos.py
```

El script está configurado para enviar el correo cada 24 horas. Durante la ejecución, imprimirá la hora en que se envió el correo y la próxima hora programada para el siguiente envío.

## Seguridad

- **Credenciales Seguras:** Asegúrate de mantener tus credenciales de correo electrónico seguras y nunca las compartas en código que sea accesible públicamente.
- **Uso de TLS:** El script utiliza TLS para asegurar la conexión con el servidor SMTP.

## Servidor SMTP

- **Servidor de Gmail:** El script utiliza el servidor SMTP de Gmail (`smtp.gmail.com`) para enviar los correos.

## Personalización

Puedes modificar el archivo `cuerpo_correo.txt` para cambiar el contenido del cuerpo del correo según tus necesidades.

## Contribuir

Si deseas contribuir a este proyecto, por favor hazlo a través de pull requests o abriendo un issue para discutir los cambios propuestos.

## Licencia

Este proyecto está bajo una licencia libre para uso no comercial. Para usos comerciales, por favor contacta al autor.
