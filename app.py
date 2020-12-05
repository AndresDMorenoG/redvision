from flask import Flask, request,render_template,redirect,url_for,session,flash

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash

app = Flask(__name__)
app.secret_key = 'dsadwe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.db'
db = SQLAlchemy(app)

class Usuarios(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    nombre = db.Column(db.String())
    apellido = db.Column(db.String())
    correo = db.Column(db.String())
    contraseña = db.Column(db.String())
    fecha = db.Column(db.String())
class Imagenes(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    id_usuario = db.Column(db.Integer())
    nombre = db.Column(db.String())
    descripcion = db.Column(db.String())
    
    imagen = db.Column(db.LargeBinary)

    
@app.route('/')
def index():
    if 'correo' in session:
        return redirect(url_for('dashboard'))
    else:
        return render_template('index.html')


@app.route('/crear-usuario',methods=['POST'] )
def create():
    if request.method == 'POST':
        if request.form['nombre'] == '':
            print('entro')
            flash('*Faltan rellenar Campos',category='registrar')
        else:
            u = Usuarios.query.filter_by(correo=request.form["correo"]).first()
            if u != None:
                flash('El usuario ya existe',category='registrar')
            else:
                contraseña_cifrada = generate_password_hash(request.form['contraseña'])
                usuarios = Usuarios(nombre=request.form['nombre'],apellido=request.form['apellido'],correo=request.form['correo'],contraseña=contraseña_cifrada,fecha=request.form['fecha'])
                
                db.session.add(usuarios)
                db.session.commit()
                falsh = 'usuario creado'
                return 'save'
    return redirect(url_for('index'))

@app.route('/login',methods=['GET','POST'])
def login():  
    if request.method == "POST":
        
        usuario = Usuarios.query.filter_by(correo=request.form["correo"]).first()
        print = request.form['contraseña']
        if usuario and check_password_hash(usuario.contraseña,request.form['contraseña']):
            session['id'] = usuario.id
            session['nombre'] = usuario.nombre
            session['correo'] = usuario.correo
            return redirect(url_for('dashboard'))
        else:
            flash('Contraseña o usuario incorrecto',category='login')
            return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
    if 'correo' in session:         
        return render_template('dashboard.html')
        
    else:
        return redirect(url_for('index'))

@app.route('/exit')
def exit():
    session.clear()
    return redirect(url_for('index'))


@app.route('/uploadImg',methods=['POST'] )
def uploadImg():
    img = request.files['imagen']
    
    imagenes = Imagenes(id_usuario=session['id'],nombre=request.form['nombre'],descripcion=request.form['descripcion'],imagen=img.read())
    
    
    db.session.add(imagenes)
    db.session.commit()
    return 'save'
    
@app.route('/perfil')
def perfil():
    if 'correo' in session: 
        return render_template('perfil.html')

    else:
        return redirect(url_for('index'))