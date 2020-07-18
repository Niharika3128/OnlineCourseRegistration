"""OnlineCourseRegistration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.views.generic import TemplateView, ListView

from admin.models import Course
from        student import views

urlpatterns = [
    path('',TemplateView.as_view(template_name='student/main_page.html'),name='student_main'),
    path('student_register/',TemplateView.as_view(template_name='student/student_registration.html'),name='student_register'),
    path('student_login/',TemplateView.as_view(template_name='student/student_login.html'),name='student_login'),
    path('login_check/',views.loginCheck,name='login_check'),
    path('save_student/',views.saveStudent,name='save_student'),
    path('student_logout/',views.studentLogout,name='student_logout'),
    path('view_all_courses/',ListView.as_view(model=Course,template_name='student/enrol_course.html'),name='view_all_courses'),
    path('enrol_course/',views.enrolCourse,name='enrol_course'),
    path('view_enrolled_courses/',views.view_enrolled_courses,name='view_enrolled_courses'),
    path('cancel_enrolled_courses/',views.cancel_enrolled_courses,name='cancel_enrolled_courses'),
    path('confirm_cancel/',views.confirmCancel,name='confirm_cancel'),

]
