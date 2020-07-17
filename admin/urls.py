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
from django.views.generic import TemplateView,ListView
from admin import views
from admin.models import Course

urlpatterns = [
    path('',TemplateView.as_view(template_name='admin/admin_login.html'),name='admin_login'),
    path('admin_check/',views.adminCheck,name='admin_check'),
    path('schedule_new_class/',TemplateView.as_view(template_name='admin/schedule_new_class.html'),name='schedule_new_class'),
    path('save_course/',views.saveCourse,name='save_course'),
    path('view_scheduled_classes/',ListView.as_view(model=Course,template_name='admin/viewall_scheduled_classes.html'),name='view_scheduled_classes'),
    path('update_class/',views.updateClass,name='update_class'),
    path('save_update/',views.saveUpdate,name='save_update'),
    path('delete_class/',views.deleteClass,name='delete_class'),
    path('admin_logout/',views.adminLogout,name='admin_logout'),
]
