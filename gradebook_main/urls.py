from django.urls import path
from . import views

app_name = "gradebook_main"

urlpatterns = [
    path('', views.index, name="index"),
    path('courses/', views.courses, name="courses"),
    path('courses/<int:course_id>', views.course, name="course"),
]
