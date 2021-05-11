#Autor: Javier Diaz
#Fecha: 10/05/2021
#Proyecto: Challenge Mercado Libre
#Archivo: api.py
#Versión 2.0

from flask import Flask, jsonify, request
import apicontroller
import json
from db import create_tables

#Creamos app web
app = Flask(__name__)

#Definimos el método GET para consulta
@app.route('/consultar', methods=["GET"])
def get_info():
    info = apicontroller.get_info()
    return jsonify(info)

#Definimos el método GET para descarga
@app.route('/descargar', methods=["GET"])
def down_info():
    info = apicontroller.get_info()
    with open('datos.json', 'w') as file:
        json.dump(info, file)
    return "Archivo descargado"

# Definimos el método POST para agregar datos
@app.route("/guardar", methods=["POST"])
def insert_info():
    info_details = request.get_json()
    ip = info_details["ip"]
    processor = info_details["processor"]
    procactiv = info_details["procactiv"]
    usuarios = info_details["usuarios"]
    os = info_details["os"]
    osv = info_details["osv"]
    result = apicontroller.insert_info(ip, processor, procactiv, usuarios, os, osv)
    return jsonify(result)

"""@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response"""

# Inicializamos el API al ejecutar este código
if __name__ == "__main__":
    create_tables()
    app.run(host='0.0.0.0', port=8000, debug=False)
