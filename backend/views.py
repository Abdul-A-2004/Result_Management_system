from django.shortcuts import render, redirect
from backend.models import *


# Create your views here.

def login_fun(request):
    return render(request,"login.html")
def home_fun(request):
    return render(request,"home.html")
def admin_panel_fun(request):
    return render("admin_panel.html")

def login_form_fun(request):
    if request.method == "POST":
        
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")

        try:
            user = User.objects.filter(username_field = username,password_field=password, role_field = role).first()        

            if user is not None:
                if role == "staff":
                    return render(request, "staff_dashboard.html")
                else:
                    return render(request, "student_dashboard.html")

        except User.DoesNotExist:
            return render(request,"login.html",{"error":"Invalid username or password"})

    return render(request,"home.html")

def staff_dashboard_fun(request):
    data = Student_info.objects.all()
    return render(request, 'admin-panel.html', {'data': data})


# def login_fun(request):
#     return render(request,"login.html")