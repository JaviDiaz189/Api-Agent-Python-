#Autor: Javier Diaz
#Fecha: 10/05/2021
#Proyecto: Challenge Mercado Libre
#Archivo: db.py
#Versión 1.0

import sqlite3
DATABASE_NAME = "infoapi.db"

#Definimos función de conexión con DB
def get_db():
    connect = sqlite3.connect(DATABASE_NAME)
    return connect

#Si no existe, creamos la DB con los parámetros establecidos
def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS infoapi(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip TEXT NOT NULL,
                processor TEXT NOT NULL,
				procactiv TEXT NOT NULL,
                usuarios TEXT NOT NULL,
                os TEXT NOT NULL,
                osv TEXT NOT NULL				
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
