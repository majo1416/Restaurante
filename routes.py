from controllers import LoginUserControllers,RegisterUserControllers,Productos,app


user = {
    "login_user": "/api/v01/user/login", "login_user_controllers": LoginUserControllers.as_view("login_api"),
    "Register_user": "/api/v01/user/register", "login_register_controllers": RegisterUserControllers.as_view("register_api"),
    "Productos_clients":"/api/v01/user/product","productos":Productos.as_view("productos_api")
}

