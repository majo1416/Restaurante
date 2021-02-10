
from flask.views import MethodView
from flask import jsonify, request
import time



class LoginUserControllers(MethodView):
    """
        Example Login
    """
    def post(self):
        #simulacion de espera en el back con 1.5 segundos
        time.sleep(1)
        content = request.get_json()
        email = content.get("email")
        password = content.get("password")
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
        if (email == "test@gmail.com" and password == "12345"):
            return jsonify({"auth": True, "name": "Pepe Perez", "token": token}), 200
        return jsonify({"auth": False}), 401
