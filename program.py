# model.py
# from django.db import models

# class Course(models.Model):
#     code = models.CharField(max_length=10)
#     name = models.CharField(max_length=50)
#     credits = models.IntegerField()

#     def __str__(self):
#         return self.code


# class Student(models.Model):
#     usn = models.CharField(max_length=10)
#     name = models.CharField(max_length=50)
#     sem = models.IntegerField()

#     courses = models.ManyToManyField(Course)

#     def __str__(self):
#         return self.usn

# 

# views.py

# from django.shortcuts import render, redirect
# from .models import Student, Course


# def home(request):
#     return render(request, 'home.html')


# def studentlist(request):
#     students = Student.objects.all()
#     return render(request, 'studentlist.html', {'students': students})


# def courselist(request):
#     courses = Course.objects.all()
#     return render(request, 'courselist.html', {'courses': courses})


# def register(request):

#     if request.method == 'POST':

#         student_id = request.POST['student']
#         course_id = request.POST['course']

#         student = Student.objects.get(id=student_id)
#         course = Course.objects.get(id=course_id)

#         student.courses.add(course)

#         return redirect('enrolled')

#     students = Student.objects.all()
#     courses = Course.objects.all()

#     return render(request, 'register.html', {
#         'students': students,
#         'courses': courses
#     })


# def enrolled(request):

#     courses = Course.objects.all()

#     selected_course = None
#     students = None

#     if request.method == 'POST':

#         course_id = request.POST['course']

#         selected_course = Course.objects.get(id=course_id)

#         students = selected_course.student_set.all()

#     return render(request, 'enrolledlist.html', {
#         'courses': courses,
#         'students': students,
#         'selected_course': selected_course
#     })

# url.py app
# from django.urls import path
# from . import views

# urlpatterns = [

#     path('', views.home, name='home'),

#     path('students/', views.studentlist, name='students'),

#     path('courses/', views.courselist, name='courses'),

#     path('register/', views.register, name='register'),

#     path('enrolled/', views.enrolled, name='enrolled'),

# ]




# urls.py proj
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [

#     path('admin/', admin.site.urls),

#     path('', include('regapp.urls')),

# ]




# base.html
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Django App</title>
# </head>

# <body>

#     <h1>Student Course Registration</h1>

#     <a href="/">Home</a> |
#     <a href="/students/">Student List</a> |
#     <a href="/courses/">Course List</a> |
#     <a href="/register/">Register</a> |
#     <a href="/enrolled/">Enrolled List</a>

#     <hr>

#     {% block content %}
#     {% endblock %}

# </body>
# </html>




# home.html

# {% extends 'base.html' %}

# {% block content %}

# <h2>Home Page</h2>

# <p>Student Course Registration System</p>

# {% endblock %}






# studentlist.html

# {% extends 'base.html' %}

# {% block content %}

# <h2>Student List</h2>

# <table border="1">

# <tr>
#     <th>USN</th>
#     <th>Name</th>
#     <th>Sem</th>
# </tr>

# {% for s in students %}

# <tr>
#     <td>{{ s.usn }}</td>
#     <td>{{ s.name }}</td>
#     <td>{{ s.sem }}</td>
# </tr>

# {% endfor %}

# </table>

# {% endblock %}





# courselist.html

# {% extends 'base.html' %}

# {% block content %}

# <h2>Course List</h2>

# <table border="1">

# <tr>
#     <th>Code</th>
#     <th>Name</th>
#     <th>Credits</th>
# </tr>

# {% for c in courses %}

# <tr>
#     <td>{{ c.code }}</td>
#     <td>{{ c.name }}</td>
#     <td>{{ c.credits }}</td>
# </tr>

# {% endfor %}

# </table>

# {% endblock %}





# register.html
# {% extends 'base.html' %}

# {% block content %}

# <h2>Register Student</h2>

# <form method="POST">

#     {% csrf_token %}

#     Select Student:

#     <select name="student">

#         {% for s in students %}

#         <option value="{{ s.id }}">
#             {{ s.usn }}
#         </option>

#         {% endfor %}

#     </select>

#     <br><br>

#     Select Course:

#     <select name="course">

#         {% for c in courses %}

#         <option value="{{ c.id }}">
#             {{ c.code }}
#         </option>

#         {% endfor %}

#     </select>

#     <br><br>

#     <input type="submit" value="Register">

# </form>

# {% endblock %}




# enrolledlist.html

# {% extends 'base.html' %}

# {% block content %}

# <h2>Enrolled Students</h2>

# <form method="POST">

#     {% csrf_token %}

#     Select Course:

#     <select name="course">

#         {% for c in courses %}

#         <option value="{{ c.id }}">
#             {{ c.code }}
#         </option>

#         {% endfor %}

#     </select>

#     <input type="submit" value="Show">

# </form>

# <br>

# {% if students %}

# <h3>Students Registered</h3>

# <table border="1">

# <tr>
#     <th>USN</th>
#     <th>Name</th>
#     <th>Sem</th>
# </tr>

# {% for s in students %}

# <tr>
#     <td>{{ s.usn }}</td>
#     <td>{{ s.name }}</td>
#     <td>{{ s.sem }}</td>
# </tr>

# {% endfor %}

# </table>

# {% endif %}

# {% endblock %}


# 6) models.py
# from django.db import models

# class Project(models.Model):

#     topic = models.CharField(max_length=100)

#     languages_used = models.TextField()

#     duration = models.PositiveIntegerField()

#     def __str__(self):

#         return self.topic



# forms.py
# from django import forms

# from .models import Project


# class ProjectForm(forms.ModelForm):

#     class Meta:

#         model = Project

#         fields = ['topic', 'languages_used', 'duration']


# views.py
# from django.shortcuts import render

# from .forms import ProjectForm


# def project_view(request):

#     if request.method == 'POST':

#         form = ProjectForm(request.POST)

#         if form.is_valid():

#             form.save()

#             return render(request, 'project_success.html')

#     else:

#         form = ProjectForm()

#     return render(request, 'project_form.html', {'form': form})


# urls.py
# from django.urls import path

# from . import views


# urlpatterns = [

#     path('project/', views.project_view, name='project'),

# ]


# project_form.html
# <!DOCTYPE html>

# <html>

# <head>
#     <title>Project Form</title>
# </head>

# <body>

# <h1>Project Submission Form</h1>

# <form method="POST">

#     {% csrf_token %}

#     {{ form.as_p }}

#     <button type="submit">Submit</button>

# </form>

# </body>
# </html>

# project_success.html
# <!DOCTYPE html>

# <html>

# <head>
#     <title>Success</title>
# </head>

# <body>

# <h1>Project Submitted Successfully</h1>

# <a href="/project/">Go Back</a>

# </body>
# </html>

# 7) views.py
# from django.shortcuts import render,redirect
# from app.models import course,student
# from django.views import generic
# def home(request):
#     return render(request,'home.html')
# def studentlist(request):
#     students=student.objects.all()
#     return render(request,'studentlist.html',{'student':students})
# def courselist(request):
#     courses=course.objects.all()
#     return render(request,'courselist.html',{'course':courses})
# def register(request):
#     if request.method=='POST':
#         sid=request.POST.get('student')
#         cid=request.POST.get('course')
#         students=student.objects.get(id=sid)
#         courses=course.objects.get(id=cid)
#         students.courses.add(courses)
#         return redirect('enrolled')
#     students=student.objects.all()
#     courses=course.objects.all()
#     return render(request,'register.html',{'student':students,'course':courses})
# def enroll(request):
#     courses=course.objects.all()
#     selected_course=None
#     student=None
#     if request.method=='POST':
#         cid= request.POST.get('course')
#         selected_course=course.objects.get(id=cid)
#         student=selected_course.student_set.all()
#     return render(request,'enrolled.html',{'course':courses,'selected_course':selected_course,'student':student})
# class studentlistview(generic.ListView):
#     model=student
#     template_name='genericlistview.html'
# class studentdetailview(generic.DetailView):
#     model=student
#     template_name='genericdetailview.html'

# Create your views here.


# urls.py
# from django.contrib import admin
# from django.urls import path
# from app import views
# from .views import studentlistview,studentdetailview

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.home,name='home'),
#     path('studentslist',views.studentlist,name='studentlist'),
#     path('courselist',views.courselist,name='courselist'),
#     path('register',views.register,name='register'),
#     path('enrolled',views.enroll,name='enrolled'),
#     path('genericlistview',studentlistview.as_view(),name='listview'),
#     path('genericdetailview/<int:pk>',studentdetailview.as_view(),name='detailview')
# ]


# list.html
# {% extends 'basic.html' %}
# {% block title %}
# home page
# {% endblock %}
# {% block content %}
# {% if object_list %}
# <table border="1">
#     <tr>
#     <th>USN</th>
#     <th>Student Name</th>
#     <th>Courses Enrolled</th>
# </tr>
# {% for student in object_list %}

# <tr>

#     <td>{{student.usn}}</td>

#     <td>{{student.Sname}}</td>

#     <td>

#         {% for c in student.courses.all %}

#             {{c.Cname}} <br>

#         {% endfor %}

#     </td>
#     </tr>
#     {% endfor %}
# </table>
# {% endif %}
# {% endblock %}


# detail.html
# {% extends 'basic.html' %}
# {% block title %}
# detailview page
# {% endblock %}
# {% block content %}
# <h1>Student Name: {{object.Sname}}</h1>

# <h1>Student USN: {{object.usn}}</h1>

# <h1>Student Semester: {{object.semester}}</h1>

# {% endblock %}


# basic.html
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
#     <header>
#         <nav>
#             <a href="{% url 'home' %}">home</a>
#             <a href="{% url 'studentlist' %}">studentlist</a>
#             <a href="{% url 'courselist' %}">ccourselist</a>
#             <a href="{% url 'register' %}">register</a>
#             <a href="{% url 'enrolled' %}">enrolled</a>
#             <a href="{% url 'listview' %}">listview</a>
#             <a href="{% url 'detailview' 1 %}">detailview</a>
#         </nav>
#     </header>
#     <main>
#         {% block content %}
#         {% endblock %}
#     </main>
#     <footer>
#         &copy; Developed by deepthi
#     </footer>
# </body>
</html>


# 7) pdf and csv
# models.py
# from django.db import models

# class course(models.Model):

#     code = models.CharField(max_length=10)

#     cname = models.CharField(max_length=30)

#     credits = models.IntegerField()

#     def __str__(self):

#         return self.code


# admin.py
# from django.contrib import admin
# from app.models import course

# admin.site.register(course)


# views.py
# from django.shortcuts import render
# from django.http import HttpResponse
# from app.models import course

# import csv

# # Course list page
# def courselist(request):

#     courses = course.objects.all()

#     return render(request,'courselist.html',{'courses':courses})


# # CSV generation
# def generateCSV(request):

#     courses = course.objects.all()

#     response = HttpResponse(content_type='text/csv')

#     response['Content-Disposition'] = 'attachment; filename=courses.csv'

#     writer = csv.writer(response)

#     writer.writerow(['Code','Course Name','Credits'])

#     for c in courses:

#         writer.writerow([c.code,c.cname,c.credits])

#     return response


# # PDF generation
# from reportlab.platypus import SimpleDocTemplate, Table
# from reportlab.lib.pagesizes import A4

# def generatePDF(request):

#     courses = course.objects.all()

#     response = HttpResponse(content_type='application/pdf')

#     response['Content-Disposition'] = 'attachment; filename=courses.pdf'

#     pdf = SimpleDocTemplate(response,pagesize=A4)

#     data = [['Code','Course Name','Credits']]

#     for c in courses:

#         data.append([c.code,c.cname,c.credits])

#     table = Table(data)

#     pdf.build([table])

#     return response


# urls.py
# from django.urls import path
# from . import views

# urlpatterns = [

#     path('courselist/',views.courselist,name='courselist'),

#     path('generateCSV/',views.generateCSV,name='generateCSV'),

#     path('generatePDF/',views.generatePDF,name='generatePDF'),

# ]


# basic.html
# <!DOCTYPE html>
# <html>
# <head>

#     <title>
#         {% block title %}
#         {% endblock %}
#     </title>

# </head>

# <body>

# <h1>Student Course Registration Portal</h1>

# <a href="{% url 'courselist' %}">Course List</a>

# <a href="{% url 'generateCSV' %}">Download CSV</a>

# <a href="{% url 'generatePDF' %}">Download PDF</a>

# <hr>

# {% block content %}
# {% endblock %}

# </body>
# </html>


#  courselist.html
#  {% extends 'basic.html' %}

# {% block title %}
# Course List
# {% endblock %}

# {% block content %}

# <table border="1">

# <tr>
#     <th>Code</th>
#     <th>Course Name</th>
#     <th>Credits</th>
# </tr>

# {% for c in courses %}

# <tr>

#     <td>{{c.code}}</td>

#     <td>{{c.cname}}</td>

#     <td>{{c.credits}}</td>

# </tr>

# {% endfor %}

# </table>

# {% endblock %}
 
