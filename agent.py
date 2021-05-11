#Autor: Javier Diaz
#Fecha: 10/05/2021
#Proyecto: Challenge Mercado Libre
#Archivo: agent.py
#Versión 2.0

import requests, platform, psutil, os, json
import socket, uuid
ls =[]
STATE = "running"


ip = str(socket.gethostbyname(socket.gethostname()))
print(ip)

# Definimos usuarios activos del sistema
usuarios = str(psutil.users())

# Identificamos los procesos activos
for proc in psutil.process_iter():
        if proc.status() == STATE:
                procname = proc.name()
                ls.append(procname)
print(ls)

# Identificamos procesador      
processor = platform.processor()

# Identificamos sistema operativo
so = platform.uname()[0]

# Identificamos versión del sistema Operativo
osv = platform.uname()[3]

# Enviamos la petición
payload = {"ip": ip, "processor" : processor, "procactiv" : str(ls), "usuarios": usuarios, "os" : so, "osv" : osv}
r = requests.post('http://localhost:8000/guardar', json=payload)
print(r.text.encode('utf8'))
