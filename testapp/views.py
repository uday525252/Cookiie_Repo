from django.shortcuts import render

# Create your views here.

def name_view(request):
    return render(request,"name.html")


def age_view(request):
    name=request.GET['name']
    response=render(request,"age.html")
    response.set_cookie('name',name)
    return response

def course_view(request):
    age=request.GET['age']
    response=render(request,"course.html")
    response.set_cookie('age',age)
    return response

def results_view(request):
    course=request.GET['course']#web developer
    name=request.COOKIES.get('name')#raju
    age=request.COOKIES.get('age')#34
    my_dict={'name':name,'age':age,'course':course}
    response=render(request,"results.html",my_dict)
    response.set_cookie('course',course)
    course=request.COOKIES.get('course')
    return response
