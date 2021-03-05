	
from flask.views import MethodView
from flask import jsonify, request
import time
class LoginUserControllers(MethodView):
    """
        Example Login
    """
    def post(self):
        #simulacion de espera en el back con 1.5 segundos
        time.sleep(3)
        return jsonify({"login ok": True}), 200
class RegisterUserControllers(MethodView):
    def post(self):
        time.sleep(3)
        return jsonify({"Register ok": True}),200
class Productos(MethodView):
    def get(self):
        productos = [{"nombre": "Aceite", "precio": 4000},
            {"nombre": "Arroz", "precio": 2000}]
        
        return jsonify({"datos": productos}), 200
