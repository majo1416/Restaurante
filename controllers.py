	
from flask.views import MethodView
from flask import Flask
from flask import jsonify, request
import time
from flask_mysqldb import MySQL
import bcrypt

#configurar de la app
app = Flask(__name__)
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="1234"
app.config["MYSQL_DB"]="restaurante"
mysql=MySQL(app)
app.secret_key='mysecretKey'
class LoginUserControllers(MethodView):
    """
        Example Login
    """
    def post(self):
        #donde almacenan los datod de la base de datos
        datos = ""
        #simulacion de espera en el back con 1.5 segundos
        time.sleep(3)
        #config de json
        content = request.get_json()
        #traigo el objeto
        correo = content.get("email")
        password = content.get("password")
        cur=mysql.connection.cursor()
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
        cur.execute("""select nombre,apellido,email,clave from usuarios where email = %s""",([correo]))
        datos = cur.fetchall()
        datos = datos[0]
        print(datos[2])
        #se pasan los atributos al email y clave
        email = datos[2]
        clave = datos[3]
        print(datos[3])
        #GUARDAR EN UN DICCIONARIO LOS DATOS EMAIL Y CLAVE
        user = {}
        user[email] = {"contraseña":clave}
        #VERIFICAR SI CORREO ES IGUAL AL EMAIL
        if user.get(correo):
            #print("fuciona")
            #LLAMAMOS AL DATOS EMAIL CON CORREO PARA NOS RETORNE LA CLAVE
            contrasenaUser= user[correo]["contraseña"]
            #print("CONTRASEÑA USUARIO ",contrasenaUser)
            if bcrypt.checkpw(bytes(str(password), encoding='utf-8'),contrasenaUser.encode('utf-8')):
                #return print("EXITOSO")
                return jsonify({"auth": True, "name": datos[0], "apellido":datos[1],"token": token}), 200
            else:
                print("NO FUNCIONO")
        else:    
            return jsonify({"auth": False}), 401
class RegisterUserControllers(MethodView):
    def post(self):
        time.sleep(3)
        content = request.get_json()
        email = content.get("email")
        name = content.get("name")
        password = content.get("password")
        lastname = content.get("lastname")
        print(password)
        #se acripta el password, se obtiene el hash
        salt = bcrypt.gensalt()
        hash_password = bcrypt.hashpw(bytes(str(password), encoding= 'utf-8'), salt)
        print("ENCRIPTADA: ",hash_password)
        cur=mysql.connection.cursor()
        cur.execute("""
        insert into usuarios
        (nombre,apellido,email,clave)
        values
        (%s,%s,%s,%s);
        """,(name,lastname,email,hash_password))
        mysql.connection.commit()
        cur.close()
        return jsonify({"Register ok": True}),200
class Productos(MethodView):
    def get(self):
        productos = [{"nombre": "Aceite", "precio": 4000},
            {"nombre": "Arroz", "precio": 2000}]
        
        return jsonify({"datos": productos}), 200
