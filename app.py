from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = 'dsadwe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.db'
app.config['UPLOAD_FOLDER'] = './static/imagenes'
db = SQLAlchemy(app)
from controlador import *

            

if __name__ == '__main__':
    app.run( host='127.0.0.1', port = 443, ssl_context=('micertificado.pem', 'llaveprivada.pem')  )


