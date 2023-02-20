from django.shortcuts import render
from Registration.models import Course, Student
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    return render (request,"index.html")


def new_course(request):
    if request.method == 'POST':
        c_code = request.POST['code']
        c_desc = request.POST['description']
        data=Course(code=c_code, description=c_desc)
        data.save()
        dict = {
            'message':'Data Save'
        }
    else:
        dict = {
            'message':''
        }
    
    return render(request, 'new_course.html', dict)

def course(request):
    allcourse=Course.objects.all()
    dict={
        'allcourse': allcourse
    }
    return render (request, "course.html", dict)
    
def search_course(request):
    if request.method == 'GET':
        data = Course.objects.filter(code = request.GET.get('c_code'))
        dict = {
                'data': data
            }
        return render (request, "search_course.html", dict)
    else:
        return render (request, "search_course.html")

def search_by_course(request):
    allcourse = Course.objects.all()
    if request.method=='GET':
        datacourse = Student.objects.filter(course_code=request.GET.get('course_code'))
        dict = {
            'data' : datacourse,
            'allcourse' : allcourse,
            'course' : request.GET.get('course_code')
        }
    else :
        dict = {
            'allcourse' : allcourse
        }
    return render(request,"search_by_course.html",dict)


