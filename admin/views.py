import datetime

from django.shortcuts import render, redirect
from admin.models import Course

def adminCheck(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == 'admin' and password == 'admin':
        return render(request,'admin/admin_home.html',{'name':username})
    else:
        return render(request,'admin/admin_login.html',{'message':"Invalid Login Details"})

def saveCourse(request):
    name = request.POST.get('name')
    faculty = request.POST.get('faculty')
    date = request.POST.get('date')
    time = request.POST.get('time')
    fee = request.POST.get('fee')
    duration = request.POST.get('duration')
    try:
        Course.objects.get(name=name,faculty=faculty,time=time)
        return render(request, 'admin/schedule_new_class.html', {'message': "Class Already Scheduled"})
    except Course.DoesNotExist:
        Course(name=name,faculty=faculty,date=date,time=time,fee=fee,duration=duration).save()
        return render(request,'admin/schedule_new_class.html',{'message':"Class Scheduled"})


def updateClass(request):
    cid = request.GET.get('cid')

    res = Course.objects.get(no=cid)
    return render(request,'admin/schedule_new_class.html', {'course_data': res})


def saveUpdate(request):
    no = request.POST.get('no')
    print(no)
    name = request.POST.get('name')
    faculty = request.POST.get('faculty')
    date = request.POST.get('date')
    time = request.POST.get('time')
    fee = request.POST.get('fee')
    duration = request.POST.get('duration')
    try:
        Course.objects.get(name=name, faculty=faculty, time=time)
        return render(request, 'admin/schedule_new_class.html', {'message': "Class Already Scheduled"})
    except Course.DoesNotExist:
        Course.objects.filter(no=no).update(name=name, faculty=faculty, date=date, time=time, fee=fee, duration=duration)
        return render(request, 'admin/viewall_scheduled_classes.html',{'object_list':Course.objects.all()})


def deleteClass(request):
    no = request.GET.get('cid')
    print(no)
    Course.objects.get(no=no).delete()
    return redirect('view_scheduled_classes')


def adminLogout(request):
    return redirect('admin_login')