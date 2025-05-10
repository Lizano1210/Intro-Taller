#
#
#
#

# Importación de librerias.
import pickle
import smtplib

def determinarReposicion():
    # Importación de base de datos e inicialización de variables.
    with open('baseDatosDinamica.pkl', 'rb') as archivobD:
            bD = pickle.load(archivobD)
    listaReposicion = []
    # --------------------------------------------------------- #        
    for i in bD:
        notaFinal = i[4][4]
        if notaFinal >= 70:
            continue
        elif notaFinal >= 60:
            listaReposicion.append(i)
        elif notaFinal < 60:
            continue
    return enviarCorreos(listaReposicion)

def enviarCorreos(listaReposicion):
     # Importación de funciones e inicialización de variables.
     from email.mime.text import MIMEText   
     from email.mime.multipart import MIMEMultipart
     mail = 'testlv@lizano.live'
     pswrd = 'Testlv123.'
     # ----------------------------------------------------- # 
     with smtplib.SMTP_SSL('smtp.hostinger.com', 465) as server:
           server.login(mail, pswrd)
            # Construcción del correo.
           for i in listaReposicion:
                correoEST = i[3]
                nombre = f'{i[0][0]} {i[0][1]} {i[0][2]}'
                # Un objeto Mime es un tipo de objeto que contiene varias partes de un mensaje, asunto, destino, origen etc...
                correo = MIMEMultipart() # Se le aplica a las variable las propiedades de un objeto MIME
                correo['Subject'] = 'Examen de Reposición'
                correo['From'] = mail
                correo['To'] = correoEST
                cuerpo = f'''
Estimado/a estudiante, {nombre}.

Se le informa que debido a que su nota final fue {i[4][4]}, usted se encuentra en estado de reposición.
Debe presentarse el día 12 de Octubre a las 3:00p.m con identificación personal y su material de trabajo.

Saludos coordiales,
Coordinación Académica
'''
                correo.attach(MIMEText(cuerpo, 'plain', 'utf-8')) # ERROR CORREGIDO: Agregamos utf-8 para evitar problemas con caracteres especiales.
                msg = correo.as_string()
                # Conexión al servidor 
                server.sendmail(mail, correoEST, msg)
     return 'Correos enviados satisfactoriamente.'



          
    
