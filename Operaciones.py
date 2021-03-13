import smtplib
from email.mime.text import MIMEText

def envioCorreo (desde, para, msg):
	#desde = 'tucorreo@gmail.com'
	#para  = 'destino@gmail.com'
	#msg = 'Correo enviado utilizano Python + smtplib en www.pythondiario.com'
	mime_message = MIMEText(msg, "html", _charset="utf-8")
 	mime_message["From"] = desde
	mime_message["To"] = para
	mime_message["Subject"] = "Industrias Astivik S.A. -- Informacion Pagos Realizados."  # Asunto

 
	# Datos
	username = 'info@astivik.com.co'
	password = 'Astivik01546Sistemas'
 
	# Enviando el correo
	server = smtplib.SMTP('webmail.astivik.com.co:587')
	#server.starttls()
	server.login(username,password)
	server.sendmail(desde, para, mime_message.as_string())
	#server.sendmail(desde, para, msg))
	server.quit()