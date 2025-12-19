from django.shortcuts import render, redirect
from django.contrib import messages
from backend.models import User, Student_info, Department

def home_fun(request):
    return render(request, "home.html")

def login_fun(request):
    return render(request, "login.html")



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
                student_gender_field = request.POST.get("gender-input"),
                department_name_field = department_id,
                student_phone_field = request.POST.get("phone-no-input"),
                student_address_field = request.POST.get("address-input")
            )

            messages.success(request, "Student added successfully")
            return redirect("admin_panel_url_name")

        except Exception as e:
            print(e)
            messages.error(request, "Student not added")
            return redirect("admin_panel_url_name")
def admin_panel_fun(request):
    department_data = Department.objects.all()
    student_data = Student_info.objects.all()

    return render(
        request,
        "admin-panel.html",
        {
            "data": student_data,
            "department_data": department_data
        }
    )