from flask import Flask
from routes import *
from flask_cors import CORS
from routes import app
CORS(app, resources={r"/*": {"origins": "*"}})
app.add_url_rule(user["login_user"], view_func=user["login_user_controllers"])
app.add_url_rule(user["Register_user"], view_func=user["login_register_controllers"])
app.add_url_rule(user["Productos_clients"],view_func=user["productos"])
