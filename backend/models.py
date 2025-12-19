from django.db import models

class Department(models.Model):
    department_name_field = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.department_name_field


class Student_info(models.Model):
    student_name_field = models.CharField(max_length=100, null=True)
    student_roll_num_field = models.CharField(max_length=100, null=True,unique=True)
    academic_year_field = models.IntegerField(null= True)
    student_dob_field = models.DateField(null=True)    
    student_gender_field = models.CharField( max_length=10 , null= True)
    department_name_field = models.ForeignKey(Department, on_delete=models.CASCADE)
    student_phone_field = models.CharField(max_length=100, null=True,unique=True)
    student_address_field = models.TextField(null=True)
    
    def __str__(self):
        return  f"{self.student_name_field , self.department_name_field}"



class Subject(models.Model):
    subject_field = models.CharField(max_length=100, null=True)
    department_name_field = models.ForeignKey(Department, on_delete=models.CASCADE)

class Result(models.Model):
    student_name_field = models.ForeignKey(Student_info, on_delete=models.CASCADE)
    subject_field = models.ForeignKey(Subject, on_delete=models.CASCADE)
    mark_field = models.IntegerField( null= True)
    maximum_mark_field = models.IntegerField(null=True)
    exam_type_field = models.CharField(max_length=50, null=True)
    grade_field = models.CharField(max_length=50, null = True)
    status = models.CharField(max_length=1, null=True)

    def __str__(self):
        return self.student_name_field

class User(models.Model):
    username_field = models.CharField( max_length=50, null=True)
    password_field = models.CharField(max_length=50, null=True)
    role_field = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f"{self.username_field, self.role_field}"
    
class Exam(models.Model):
    exam_name_field = models.CharField(max_length=50, null=True)
    exam_date_field = models.DateField(null=True)

    def __str__(self):
        return f"{self.exam_name_field, self.exam_date_field}"
    