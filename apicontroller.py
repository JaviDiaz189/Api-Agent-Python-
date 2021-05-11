#Autor: Javier Diaz
#Fecha: 10/05/2021
#Proyecto: Challenge Mercado Libre
#Archivo: apicontroller.py
#Versión 2.0

from db import get_db

#Definimos la función para insertar  DB
def insert_info(ip, processor, procactiv, usuarios, os, osv):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO infoapi(ip, processor, procactiv, usuarios, os, osv) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [ip, processor, procactiv, usuarios, os, osv])
    db.commit()
    return True

#Definimos la función para consultar información de la DB
def get_info():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, ip, processor, procactiv, usuarios, os, osv FROM infoapi"
    cursor.execute(query)
    return cursor.fetchall()
