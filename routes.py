from controllers import LoginUserControllers,RegisterUserControllers


user = {
    "login_user": "/api/v01/user/login", "login_user_controllers": LoginUserControllers.as_view("login_api"),
    "Register_user": "/api/v01/user/register", "login_register_controllers": RegisterUserControllers.as_view("register_api")
}

