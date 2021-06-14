from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    context = {
        'all_courses': Course.objects.all(),
    }
    return render(request, 'index.html', context)

def create(request):
    errors = Course.objects.course_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/')
    else: 
        desc = Description.objects.create(content=request.POST['description'])
        Course.objects.create(name=request.POST['name'], description=desc)
        return redirect('/')

def destroy(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id)
    }
    return render(request, 'delete.html', context)

def delete(request):
    if request.method == 'POST':
        course = Course.objects.get(id=request.POST['secret'])
        course.delete()
        return redirect('/')