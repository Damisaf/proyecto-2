'''
Flask [Python]
Proyecto Administracion de turnos de consultorio Medico

Autor: Damian Safdie

Descripcion:
Se utiliza Flask para crear un WebServer que levanta los datos de
los turnos de un consultorio medico

Ingresar a la siguiente URL para ver los endpoints disponibles
http://127.0.0.1:5000/
'''


#from datetime import datetime
import traceback
from flask import Flask, request, jsonify, render_template, Response, redirect, url_for
import turnos

# Crear el server Flask
app = Flask(__name__)

# Indicamos al sistema (app) de donde leer la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///turnos.db"
# Asociamos nuestro controlador de la base de datos con la aplicacion
#turnos.db.init_app(app)

# Ruta que se ingresa por la ULR 127.0.0.1:5000
@app.route("/")
def index():
    try:
        print("Renderizar index.html")
        return render_template('index.html')
    except:
        return jsonify({'trace': traceback.format_exc()})


@app.route("/registro", methods=['GET', 'POST'])
def registro():
    if request.method == 'GET':
        try:                                            
            data = turnos.consultar()
            return render_template('registro.html', data=data)            
        except:
            return jsonify({'trace': traceback.format_exc()})

    if request.method == 'POST':
        try:
            nombre = str(request.form.get('name')).lower()
            data = turnos.consultar()
            turno = request.form.get('turno')
    
            if(nombre == ""):
                # Datos ingresados incorrectos
                return render_template('no_asignado.html', nombre=nombre, turno=turno)  
            else:
                turnos.reservar(turno, nombre)
                return render_template('asignado.html', nombre=nombre, turno=turno)  
        except:
            return jsonify({'trace': traceback.format_exc()})



if __name__ == '__main__':
    # Lanzar server
    app.run(host="127.0.0.1", port=5000)
    