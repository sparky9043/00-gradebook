from django.urls import path
from . import views

app_name = "gradebook_main"

urlpatterns = [
    path('', views.index, name="index"),
    # courses links
    path('courses/', views.courses, name="courses"),
    path('courses/<int:course_id>', views.course, name="course"),
    
    # students links
    path('students/', views.students, name="students"),
    path('students/<int:student_id>', views.student, name="student"),
]
