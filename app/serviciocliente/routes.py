from flask import Flask, render_template, request, redirect, url_for, flash
from . import modelo_servicio
from flask_mysqldb import MySQL
import app

#Crear una instancia Flask
app = Flask(__name__)

# MYSQL Connection 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'post_sale'

# Settings
app.secret_key = 'mysecretkey'

mysql = MySQL(app)

#inicio de la ruta en donde se encuentra el menú de reseñas 

#inicio de la ruta en donde se encuentra el menú de reseñas 
@modelo_servicio.route("/insertar_reseña")
def insertar_reseña():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM reseñas')
    data = cur.fetchall()
    return render_template("serviciocliente.html", reseñas = data)

#Función para insertar pqrs
@modelo_servicio.route('/insertar_reseña', methods=['GET', 'POST'])
def agregar_reseña():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        comentario = request.form['comentario']
        calificacion = request.form['calificacion']
        if (calificacion == "deficiente"):
            return render_template('registrarpqr.html')
        if (calificacion == "pesimo"):
            return render_template('registrarpqr.html')
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO  reseñas (nombre, correo, comentarios, calificacion) VALUES (%s,%s,%s,%s)',
                    (nombre, correo, comentario, calificacion))
        mysql.connection.commit()
        flash("¡RESEÑA registrada exitosamente!")
    return redirect(url_for('modelo_servicio.insertar_reseña'))

#Función para eliminar las rese{as} por ID atra vez de la tabla
@modelo_servicio.route('/eliminar_reseña/<string:id>')
def eliminar_reseña(id):
    cur = mysql.connection.cursor()  
    cur.execute('DELETE FROM reseñas WHERE idReseña = {0}'.format(id))
    mysql.connection.commit() 
    flash('Garantía eliminado satisfactoriamente')
    return redirect(url_for('modelo_servicio.insertar_reseña'))

#Función para mostrar los pqrs ya hechos 
@modelo_servicio.route('/insertar')
def insertar():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM pqrs')
    data = cur.fetchall()   
    return render_template('registrarpqr.html' , servicios = data)

#Función para insertar pqrs
@modelo_servicio.route('/insertar', methods=['GET', 'POST'])
def agregar_pqrs():
    if request.method == 'POST':
        tipoPqrs = request.form['tipoPqrs']
        descripcionPqrs = request.form['descripcionPqrs']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO  pqrs (tipoPqrs, descripcionPqrs) VALUES (%s,%s)',
                    (tipoPqrs, descripcionPqrs))
        mysql.connection.commit()
        flash("¡PQR'S registrado exitosamente!")
    return redirect(url_for('modelo_servicio.insertar'))

#Función para eliminar los pqrs por ID atra vez de la tabla
@modelo_servicio.route('/eliminar_servicio/<string:id>')
def eliminar_pqrs(id):
    cur = mysql.connection.cursor()  
    cur.execute('DELETE FROM pqrs WHERE idPqrs = {0}'.format(id))
    mysql.connection.commit() 
    flash('Pqrs eliminado satisfactoriamente')
    return redirect(url_for('modelo_servicio.insertar'))

#Funcion para obtener los datos atraves del ID 
@modelo_servicio.route('/editar_servicio/<id>')
def obtener_pqrs(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM pqrs WHERE idPqrs = {0}".format(id))
    dataS = cur.fetchall()
    return render_template('editarpqr.html', servicio = dataS[0])

#funcion para actualizar los datos del pqrs
@modelo_servicio.route('/actualizar_servicio/<id>', methods = ['POST'])
def actualizar_pqrs(id):
    if request.method == 'POST':
        tipoPqrs = request.form['tipoPqrs']
        descripcionPqrs = request.form['descripcionPqrs']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE pqrs 
            SET tipoPqrs = %s,
                descripcionPqrs = %s
            WHERE idpqrs = %s
        """, (tipoPqrs, descripcionPqrs, id))
        flash('Garantía actualizada satisfactoriamente')
        cur.connection.commit()
        return redirect(url_for('modelo_servicio.insertar'))
