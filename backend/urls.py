from django.urls import path
from backend.views import *

urlpatterns = [
    path("login_url",login_fun, name="login_url_name"),
    path("login_fun_url", login_form_fun , name="login_fun_name"),
    path("home_url",home_fun, name="home_url_name"),
    path("admin_panel_url", admin_panel_fun, name = "admin_panel_url_name"),
    path("staff_dashboard_fun",staff_dashboard_fun)
]
