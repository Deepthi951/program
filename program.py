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