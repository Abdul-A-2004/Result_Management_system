from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from django.core.mail import send_mail
from django.views import View
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
    student_data = Student_info.objects.filter(is_active=0)

    return render(request,"admin-panel.html",{"data": student_data,"department_data": department_data})
def update_info_fun(request, id):

    update_student = Student_info.objects.get(id=id)
    department_data = Department.objects.all()
    users = update_student.username_field     
    if request.method == "POST":
        try:
            phone_no = request.POST.get("phone-no-input", "").strip()
            name = request.POST.get("name-input", "").strip()
            roll_no = request.POST.get("roll-no-input")
            dob = request.POST.get("dob-input")
            email = request.POST.get("email-input")
            
            first_name = name.split()[0]

            dob_date = datetime.strptime(dob, "%Y-%m-%d").date()
            dob_year = str(dob_date.year)
            roll_no_last_six = roll_no[-6:]
            phone_last_six = phone_no[-6:]
            username = f"{first_name}@{roll_no_last_six}"
            password = f"{phone_last_six}@{dob_year}"

            users.username_field = username
            users.password_field = password

            users.save()

            department_name = request.POST.get("department-input")
            department_id = Department.objects.get (id = department_name)

            update_student.student_name_field = name
            update_student.student_roll_num_field = roll_no
            update_student.academic_year_field = request.POST.get("academic-year-input") 
            update_student.student_dob_field = dob
            update_student.student_email_field = email 
            update_student.student_gender_field = request.POST.get("gender-input") 
            update_student.department_name_field = department_id 
            update_student.student_phone_field = phone_no
            update_student.student_address_field = request.POST.get("address-input")
            
            update_student.save()
            send_mail(
            subject="Update to Your Student Portal Details",
            message= f"""
        
Dear Student,

Greetings from AH College of Arts and Science.

This is to inform you that your details in the Student Result Management System have been successfully updated.

Please find your updated login credentials below:

Username: {username}
Password: {password}

🔐 Important Instructions:

1. Please keep your login credentials confidential.

2. Do not share your username or password with anyone.

3. If you did not request or expect this update, kindly contact the college administration immediately.

4. We strongly recommend changing your password after logging in.

🌐 Student Portal Access:

If you face any issues while accessing your account, feel free to reach out to the administration or IT support team.

Thank you for your cooperation.

Warm regards,
Abdul Harish
Administrator
AH College of Arts and Science""",recipient_list=[email],from_email="harishabdul908729@gmail.com", fail_silently = False
    )

            messages.success(request, f"Student Updated successfully | Username: {username} | Password: {password}")
            return redirect("admin_panel_url_name")
        
        except Exception as e: 
            print(e)
            messages.error(request, "Student not Updated")
            return redirect("admin_panel_url_name")

    return render(
        request,
        "update-form.html",
        {
            "department_data": department_data,
            "update": update_student,  
        }
    )


def login_form_fun(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")
        active = 0
        user = User.objects.filter(
            username_field=username,
            password_field=password,
            role_field=role,
            is_active = active 
        ).first()

        if user is not None:
            request.session['user_id'] = user.id
            request.session['username'] = user.username_field
            request.session['role'] = user.role_field
            request.session['active'] = user.is_active

            if role == "admin" and username.startswith("admin") and active == 0:
                return redirect("admin_panel_url_name")

            elif active == 0 :
                return render(request, "student_dashboard.html")

        else:
            return render(
                request,
                "login.html",
                {"error": "Invalid username or password"}
            )

    return redirect("login_url_name")

def add_student_fun(request):
    phone_no = request.POST.get("phone-no-input", "").strip()
    name = request.POST.get("name-input", "").strip()
    roll_no = request.POST.get("roll-no-input")
    dob = request.POST.get("dob-input")
    email = request.POST.get("email-input")
    department_id = request.POST.get("department-input")
    department = Department.objects.get(id=department_id)
    
    first_name = name.split()[0]

    dob_date = datetime.strptime(dob, "%Y-%m-%d").date()
    dob_year = str(dob_date.year)
    roll_no_last_six = roll_no[-6:]
    phone_last_six = phone_no[-6:]
    username = f"{first_name}@{roll_no_last_six}"
    password = f"{phone_last_six}@{dob_year}"


    
    if request.method == "POST":
        try:
            if not phone_no.isdigit() or len(phone_no) != 10:
                messages.error(request, "Invalid phone number")
                return redirect("admin_panel_url_name")

            if not name:
                messages.error(request, "Name is required")
                return redirect("admin_panel_url_name")

            if User.objects.filter(username_field=username).exists():
                messages.error(request, "Username already exists")
                return redirect("admin_panel_url_name")

            user = User.objects.create(
                username_field=username,
                password_field=password,
                role_field="student"
            )

            Student_info.objects.create(
                student_name_field=name,
                username_field=user,
                student_roll_num_field=roll_no,
                academic_year_field=request.POST.get("academic-year-input"),
                student_dob_field=dob_date,
                student_email_field = email,
                student_gender_field=request.POST.get("gender-input"),
                department_name_field=department,
                student_phone_field=phone_no,
                student_address_field=request.POST.get("address-input")
            )
            send_mail(
            subject="Student Portal Login Credentials",
            message= f"""
        
Dear Student,

Greetings from AH College of Arts and Science.

Your account for the Student Result Management System has been successfully created.
Please find your login credentials below:

Username: {username} 
Password: {password}

🔐 Important Instructions:

1. Please keep your login credentials confidential.

2. Do not share your username or password with anyone.

3. We recommend changing your password after your first login.

🌐 Login Portal:


If you face any issues while logging in, kindly contact the college administration or IT support team.

We wish you all the best in your academic journey.

Warm regards,
Abdul Harish
Administrator
AH College of Arts and Science""",recipient_list=[email],from_email="harishabdul908729@gmail.com", fail_silently = False
    )

            messages.success(
                request,
                f"Student added successfully | Username: {username} | Password: {password}"
            )
            return redirect("admin_panel_url_name")

        except Exception as e:
            print("ADD STUDENT ERROR:", e)
            messages.error(request, "Student not added")
            return redirect("admin_panel_url_name")

def delete_student_fun(request,id):
    student_active = Student_info.objects.get(id = id)
    user_active = student_active.username_field
    student_active.is_active = -1
    user_active.is_active = -1
    student_active.save()
    user_active.save()
    return redirect("admin_panel_url_name")


