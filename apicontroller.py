#Autor: Javier Diaz
#Fecha: 10/05/2021
#Proyecto: Challenge Mercado Libre
#Archivo: apicontroller.py
#Versión 1.0

from db import get_db

#Definimos la función para insertar  DB
def insert_info(processor, procactiv, usuarios, os, osv):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO infoapi(processor, procactiv, usuarios, os, osv) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(statement, [processor, procactiv, usuarios, os, osv])
    db.commit()
    return True

#Definimos la función para consultar información de la DB
def get_info():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, processor, procactiv, usuarios, os, osv FROM infoapi"
    cursor.execute(query)
    return cursor.fetchall()
