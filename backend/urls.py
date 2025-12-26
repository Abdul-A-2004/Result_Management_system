from django.urls import path
from backend.views import *

urlpatterns = [
    path("", home_fun, name="home_url_name"),
    path("login_url/", login_fun, name="login_url_name"),
    path("logout_url/", logout_fun, name="logout_url_name"),
    path("login_form_fun_url/", login_form_fun, name="login_form_fun_url_name"),

    path("admin_panel_url", admin_fun, name="admin_panel_url_name"),
    path("add_student_url/", add_student_fun, name="add_student_url_name"),
    path("delete_student_url/<int:id>", delete_student_fun, name="delete_student_url_name"),
    path("update_info_url/<int:id>", update_info_fun, name="update_info_url_name"),
    path("update_student_url/<int:id>", update_student_fun, name="update_student_url_name"),
]
