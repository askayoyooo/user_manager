from django.urls import path
from . import views

'''注意尖括号'''
app_name = 'app01'
urlpatterns = [
    path('login.html', views.Login.as_view()),
    path('index.html', views.index),
    path('logout.html', views.logout),
    path('classes.html', views.handle_classes),
    path('student.html', views.handle_student),
    path('teacher.html', views.handle_teacher),
]