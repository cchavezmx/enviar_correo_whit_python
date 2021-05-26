import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Iniciamos los parámetros del script
datos = sys.argv[1:]


remitente = 'cchavez@grupointecsa.com'
destinatario = datos[0]
mensajeBody = datos[1]

# Creamos el objeto mensaje
mensaje = MIMEMultipart()

# Establecemos los atributos del mensaje
mensaje['From'] = remitente
mensaje['To'] = destinatario
mensaje['Subject'] = '[RPI] Correo de prueba Number 8'

# Creamos el cuerpo del mensaje

header = '''\
<html>
  <head></head>
  <body>
    <p>Bievenidos a Grupo Intecsa<br><br>
    </p>
  </body>
</html>
'''

footer = '''\
  </p>
  </body>
</html>
  '''

cuerpo = header + str(mensajeBody) + footer
# Y lo agregamos al objeto mensaje como objeto MIME de tipo texto
mensaje.attach(MIMEText(cuerpo, 'html'))

# Creamos la conexión con el servidor
sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
  
# Ciframos la conexión
sesion_smtp.starttls()
  
# Iniciamos sesión en el servidor
sesion_smtp.login()

# Convertimos el objeto mensaje a texto
texto = mensaje.as_string()

# Enviamos el mensaje
sesion_smtp.sendmail(remitente, destinatario, texto)

# Cerramos la conexión
sesion_smtp.quit()
