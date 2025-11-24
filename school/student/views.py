# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import Student


def student(request):
    students = Student.objects.all().values()
    template = loader.get_template('all_students.html')
    context = {
        'students': students
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    student = Student.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'student': student
    }
    return HttpResponse(template.render(context, request))


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

# def student(request):
#     return render(request, 'first.html')
    # template = loader.get_template('first.html')
    # return HttpResponse(template.render())
