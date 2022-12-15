import csv
import sqlite3
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Crear el motor (engine) de la base de datos
engine = sqlalchemy.create_engine("sqlite:///turnos.db")
base = declarative_base()

class Turnos(base):
    __tablename__ = "turnos"
    id = Column(Integer, primary_key=True)
    fecha_y_hora = Column(String)
    paciente = Column(String)
    doctor = Column(String)
    dispo = Column(String)

    def __repr__(self):
        return f"Turnos: {self.fecha_y_hora}"


def create_schema():
    # Borrar todos las tablas existentes en la base de datos    
    base.metadata.drop_all(engine)
    # Crear las tablas
    base.metadata.create_all(engine)


def reservar(turno, paciente):
    engine = sqlalchemy.create_engine("sqlite:///turnos.db")
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Turnos).filter(Turnos.fecha_y_hora == turno)
    elturno = result.first()   
    elturno.dispo = "N"
    elturno.paciente = paciente   
    session.add(elturno)
    session.commit()

def consultar():
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(Turnos).filter(Turnos.dispo == "S")   
    json_result_list = []
    for turno in query:    
        json_result = {'fecha': turno.fecha_y_hora, 'paciente': turno.paciente, 'doctor': turno.doctor}
        json_result_list.append(json_result)
    return json_result_list

   
def fill():       
    Session = sessionmaker(bind=engine)
    session = Session()
    archivo = open('turnos.csv', 'r')
    lalista = list(csv.DictReader(archivo))
    archivo.close()

    for i in lalista:        
        lista = Turnos(fecha_y_hora = i['fecha']+" "+i['hora'], paciente =i['paciente'], doctor =i['doctor'], dispo = "S")
        session.add(lista)
        print(lista)
    session.commit()
        
if __name__ == '__main__':
    create_schema()
    fill()
