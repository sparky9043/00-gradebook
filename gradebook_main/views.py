from django.shortcuts import render

from .models import Course

# Create your views here.
def index(request):
    return render(request, 'gradebook_main/index.html')


def courses(request):
    courses = Course.objects.all()
    context = { 'courses': courses }
    return render(request, 'gradebook_main/courses.html', context)