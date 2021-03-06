from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from admin.models import Course
from student.models import StudentInfo,EnrolCourse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def saveStudent(request):
    name = request.POST.get('name')
    contact = request.POST.get('contact')
    email = request.POST.get('email')
    password = request.POST.get('password')
    print(name,contact,email,password)
    StudentInfo(name=name,contact=contact,email=email,password=password).save()
    messages.success(request,"Student Registered Successfully")
    return redirect('student_register')

@method_decorator(csrf_exempt,name='dispatch')
def checkEmail(request):
    email = request.POST['value']
    try:
        StudentInfo.objects.get(email=email)
        res = {'error':'Email Id Already Taken'}
    except StudentInfo.DoesNotExist:
        res = {'message':'Email Id is Available'}
    return JsonResponse(res)

@method_decorator(csrf_exempt,name='dispatch')
def checkContact(request):
    contact = request.POST['value']
    try:
        StudentInfo.objects.get(contact=contact)
        res = {'error': 'Contact Number Already Taken'}
    except StudentInfo.DoesNotExist:
        res = {'message': 'Contact Number is Available'}
    return JsonResponse(res)

def loginCheck(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
        # res = StudentInfo.objects.get(Q(email=username, password=password) | Q(contact=username,password=password))
        res = StudentInfo.objects.get(email=username,password=password)
        request.session['data'] = res.contact
        return render(request,'student/student_home.html',{'data':res.name})
    except StudentInfo.DoesNotExist:
        try:
            res = StudentInfo.objects.get(contact=username, password=password)
            request.session['data'] = res.contact
            return render(request, 'student/student_home.html', {'data': res.name})
        except ValueError:
            messages.error(request, "Enter EmailId or Contact Number to Login")
            return redirect('student_login')
        except StudentInfo.DoesNotExist:
            messages.error(request, "Invalid Login Details")
            return redirect('student_login')

def studentLogout(request):
    del request.session['data']
    return redirect('student_main')

def enrolCourse(request):
    cno = request.POST.get('cno')
    contact = request.POST.get('contact')
    try:
        EnrolCourse.objects.get(student_id=contact, course_id=cno)
        return render(request, 'student/enrol_course.html', {'object_list':Course.objects.all(),'message': "Course Already Enrolled"})
    except EnrolCourse.DoesNotExist:
        EnrolCourse.objects.create(student_id=contact, course_id=cno)
        return render(request, 'student/enrol_course.html', {'object_list':Course.objects.all(),'message': "Course Enrolled"})

def view_enrolled_courses(request):
    contact = request.GET.get('contact')
    res = EnrolCourse.objects.filter(student_id=contact)
    data = [Course.objects.get(no=x.course_id) for x in res]
    return render(request,'student/view_enrolled_courses.html',{'data':data})

def cancel_enrolled_courses(request):
    contact = request.GET.get('contact')
    res = EnrolCourse.objects.filter(student_id=contact)
    data = [Course.objects.get(no=x.course_id) for x in res]
    return render(request,'student/cancel_enrolled_courses.html',{'data':data})

def confirmCancel(request):
    cno = request.POST.get('cno')
    contact = request.POST.get('contact')
    EnrolCourse.objects.get(student_id=contact,course_id=cno).delete()
    res = EnrolCourse.objects.filter(student_id=contact)
    data = [Course.objects.get(no=x.course_id) for x in res]
    return render(request,'student/cancel_enrolled_courses.html',{'data':data})