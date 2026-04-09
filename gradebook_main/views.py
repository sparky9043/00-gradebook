from django.shortcuts import render

from .models import Course

# Create your views here.
def index(request):
    return render(request, 'gradebook_main/index.html')


def courses(request):
    courses = Course.objects.all()
    context = { 'courses': courses }
    return render(request, 'gradebook_main/courses.html', context)


def course(request, course_id):
    course = Course.objects.get(id=course_id)
    students = course.student_set.all()
    context = { 'course': course, 'students': students }
    return render(request, 'gradebook_main/course.html', context)