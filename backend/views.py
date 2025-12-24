from django.shortcuts import render, redirect
from django.contrib import messages
from backend.models import *

def home_fun(request):
    return render(request, "home.html")

def login_fun(request):
    return render(request, "login.html")

def logout_fun(request):
    request.session.flush()
    return redirect("login_url_name")

def admin_fun(request):
    if request.session.get("role") != "admin":
        return redirect("login_url_name")

    department_data = Department.objects.all()
    student_data = Student_info.objects.filter(activate_field=0)

    return render(request,"admin-panel.html",{"data": student_data,"department_data": department_data})

def login_form_fun(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")

        user = User.objects.filter(
            username_field=username,
            password_field=password,
            role_field=role
        ).first()

        if user is not None:
            request.session['user_id'] = user.id
            request.session['username'] = user.username_field
            request.session["role"] = user.role_field

            if role == "staff":
                return render(request, "staff_dashboard.html")

            elif role == "admin" and username.startswith("admin"):
                return redirect("admin_panel_url_name")

            else:
                return render(request, "student_dashboard.html")

        else:
            return render(
                request,
                "login.html",
                {"error": "Invalid username or password"}
            )

    return render(request, "login.html")


def add_student_fun(request):
    if request.method == "POST":
        try:
            department_name = request.POST.get("department-input")
            department_id = Department.objects.get (id= department_name)
            Student_info.objects.create(
                student_name_field = request.POST.get("name-input"),
                student_roll_num_field = request.POST.get("roll-no-input"),
                academic_year_field = request.POST.get("academic-year-input"),
                student_dob_field = request.POST.get("dob-input"),
                student_email_field = request.POST.get("email-input"),
                student_gender_field = request.POST.get("gender-input"),
                department_name_field = department_id,
                student_phone_field = request.POST.get("phone-no-input"),
                student_address_field = request.POST.get("address-input")
            )

            messages.success(request, "Student added successfully")
            return redirect("admin_panel_url_name")

        except Exception as e:  
            messages.error(request, "Student not added")
            return redirect("admin_panel_url_name")


def delete_student_fun(request,id):
    activate = Student_info.objects.get(id = id)
    activate.activate_field = -1
    activate.save()
    return redirect("admin_panel_url_name")

def update_student_fun(request,id):
    update = Student_info.objects.get(id = id)
    if request.method == "POST":
        try:
            department_name = request.POST.get("department-input")
            department_id = Department.objects.get (id= department_name)
            update = Student_info.objects.update(
                student_name_field = request.POST.get("name-input"),
                student_roll_num_field = request.POST.get("roll-no-input"),
                academic_year_field = request.POST.get("academic-year-input"),
                student_dob_field = request.POST.get("dob-input"),
                student_email_field = request.POST.get("email-input"),
                student_gender_field = request.POST.get("gender-input"),
                department_name_field = department_id,
                student_phone_field = request.POST.get("phone-no-input"),
                student_address_field = request.POST.get("address-input")
            )
            update.save()

            messages.success(request, "Student Updated successfully")
            return redirect("admin_panel_url_name")
        

        except Exception as e:  
            messages.error(request, "Student not Updated")
            return redirect("admin_panel_url_name")

    