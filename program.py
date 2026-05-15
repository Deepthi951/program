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
