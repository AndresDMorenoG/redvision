from flask import Flask, request,render_template,redirect,url_for,session,flash,jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
app = Flask(__name__)
app.secret_key = 'dsadwe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.db'
db = SQLAlchemy(app)
from modelos import Usuarios,Imagenes


#-------------------------------------------------------------------- 

@app.route('/')
def index():
    """Funcion principal muestra index.html

       Contiene los formularios de registro y login.
    """ 
    if 'nombreUsuario' in session:
        return redirect(url_for('dashboard'))
    else:
        return render_template('index.html')

#-------------------------------------------------------------------- 

@app.route('/crearusuario',methods=['POST'] )
def create():
    
    """ Se encarga de crear la sessiones si existe el usuario.

        .Verfica que el correo y la contraseña coincidan,
        si coinciden envia un mensaje de 'correcto', si no
        envia un mensaje de error.
    """
    
  
    u = Usuarios.query.filter_by(nombreUsuario=request.form["nombreUsuario"]).first()
    if u != None:
        return jsonify({'error': '1'}) 
    else:
        u = Usuarios.query.filter_by(correo=request.form["correo"]).first()
        if u != None:
            return jsonify({'error': '2'})
        else:
            contraseña_cifrada = generate_password_hash(request.form['contraseña'])
            usuarios = Usuarios(nombre=request.form['nombre'],apellido=request.form['apellido'],correo=request.form['correo'],contraseña=contraseña_cifrada,fecha=request.form['fecha'],nombreUsuario=request.form['nombreUsuario'])
            db.session.add(usuarios)
            db.session.commit() 
            return jsonify({'creado': 'usuario creado'})
    
#-------------------------------------------------------------------- 

@app.route('/login',methods=['POST'])
def login():  
    """ Se encarga de crear la sessiones si existe el usuario.

        .Verfica que el correo y la contraseña coincidan,
        si coinciden envia un mensaje de 'correcto', si no
        envia un mensaje de error.
    """
    
    usuario = Usuarios.query.filter_by(correo=request.form["correo"]).first()
    print(usuario.correo)
    print(usuario != None)
    if usuario != None:
        if  check_password_hash(usuario.contraseña,request.form['contraseña']):
            session['id'] = usuario.id
            session['nombreUsuario'] = usuario.nombreUsuario
            session['correo'] = usuario.correo
            print('usuario correcto')
            return jsonify({'correcto': 'correcto'})
        else:
            return jsonify({'error': '2'})
    else:  
        print('error')        
        return jsonify({'error': '1'})
   
#-------------------------------------------------------------------- 

@app.route('/dashboard/',methods=['GET','POST'])
def dashboard():
    """
         muestra el dashboard cuando el usuario esta logeado

    """
    if 'nombreUsuario' in session:         
        return render_template('dashboard.html')
        
    else:
        return redirect(url_for('index'))

#-------------------------------------------------------------------- 

@app.route('/exit',methods=['GET'])
def exit():
    """ 
        Elimina la Session y redireciona a 'index'

    """
    session.clear()
    return redirect(url_for('index'))

#-------------------------------------------------------------------- 

@app.route('/uploadImg/',methods=['POST'] )
def uploadImg():
    """ 
        Sube imagenes del usuario

    """
    return ''

#-------------------------------------------------------------------- 

@app.route('/perfil/',methods=['GET'])
def perfil():
    """ 
        Muestra perfil del usuario

    """

    if 'correo' in session: 
        return render_template('perfil.html')

    else:
        return redirect(url_for('index'))

#-------------------------------------------------------------------- 

@app.route('/configuracion/')
def configuracion():
    if 'correo' in session: 
        return render_template('configuracion.html')

    else:
        return redirect(url_for('index'))


#-------------------------------------------------------------------- 

@app.route('/CorreoRecuperar/',methods=['POST'])
def correoRecuperacion():
    """ 
        Envia Correo de recuperacion

    """
    return ''

#-------------------------------------------------------------------- 

@app.route('/CorreoValidar/',methods=['POST'])
def correoValidacion():
    """ 
        Envia Correo de validacion del usuario

    """
    return ''

#-------------------------------------------------------------------- 

@app.route('/recuperar/')
def cambiarContraseña():
    """ 
        Muestra template para cambiar contraseña

    """
    return render_template('configuracion.html')

#-------------------------------------------------------------------- 

@app.route('/cambiocontraseña/')
def envioContraseña():
    """ 
        Guarda la nueva contraseña

    """
    return ''









