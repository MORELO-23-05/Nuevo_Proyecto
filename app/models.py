# Modelo para los roles de usuario
from . import db #El punto se reconoce como el archivo "__init__.py" igual el app

#dependencia para fecha y hora
from datetime import datetime


#crear los modelos 
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Text, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Crear una instancia de Base


# Modelo para los roles de usuario
class Rol(db.Model):
    __tablename__ = 'Rol'
    id = Column(Integer, primary_key= True)
    tipoRol = Column(String(45), nullable = False)
    nombreRol = Column(String(45), nullable = False)

class Usuario(db.Model):
    __tablename__ = 'Usuario'
    idUsu = Column(Integer, primary_key = True)
    apellidoUsu = Column(String(45), nullable = False)
    telefonoUsu = Column(String(45), nullable = False)
    emailUsu= Column(String(45), nullable = False)
    direccionUsu = Column(String(45), nullable = False)
    contrasenaUsu = Column(String(45), nullable = False)
    idRolFk = Column(Integer, ForeignKey('Rol.id'))

class Garantias(db.Model):
    __tablename__ = 'Garantia'
    idGarantia = Column(Integer, primary_key = True)
    fechaGarantia = Column(Date, nullable = False)
    descripcionGarantia = Column(Text, nullable = False)
    tipoGarantia = Column(String(255), nullable = False)
    idUsuFk = Column(Integer, ForeignKey('Usuario.idUsu'))

class Contrato(db.Model):
    __tablename__ = 'Contrato'
    idContrato = Column(String(20), primary_key = True)
    tipoContrato = Column(String(50), nullable = False)
    descripcionContrato = Column(Text, nullable = False)
    idGarantiaFk = Column(Integer, ForeignKey('Garantia.idGarantia'))
    idUsuFk = Column(Integer, ForeignKey('Usuario.idUsu'))

class Pqrs(db.Model):
    __tablename__='Pqrs'
    idPqrs = Column(Integer, primary_key = True)
    tipoPqrs = Column(String(255), nullable = False)
    descripcionPqrs = Column(Text, nullable = False)
    idGarantiaFk = Column(Integer, ForeignKey('Garantia.idGarantia'))
    idContratoFk = Column(String(20), ForeignKey('Contrato.idContrato'))
