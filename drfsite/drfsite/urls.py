"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from tutoring_center.views import *
from tutoring_center.yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/tutors/', TutorAPIList.as_view()),
    path('api/v1/tutors/<uuid:pk>/', TutorAPIDetail.as_view()),
    path('api/v1/students/', StudentAPIList.as_view()),
    path('api/v1/students/<uuid:pk>/', StudentAPIDetail.as_view()),
    path('api/v1/admins/', AdministratorAPIList.as_view()),
    path('api/v1/admins/<uuid:pk>/', AdministratorAPIDetail.as_view()),
    path('api/v1/subjects/', SubjectAPIList.as_view()),
    path('api/v1/subjects/<uuid:pk>/', SubjectAPIDetail.as_view()),
    path('api/v1/services/', ServiceAPIList.as_view()),
    path('api/v1/services/<uuid:pk>/', ServiceAPIDetail.as_view()),
	 path('api/v1/regs/', RegistrationForServiceAPIList.as_view()),
    path('api/v1/regs/<uuid:pk>/', RegistrationForServiceAPIDetail.as_view()),
    path('api/v1/homeworks/', HomeworkAPIList.as_view()),
    path('api/v1/homeworks/<uuid:pk>/', HomeworkAPIDetail.as_view()),
    path('api/v1/files/', FileAPIList.as_view()),
    path('api/v1/files/<uuid:pk>/', FileAPIDetail.as_view()),
    path('api/v1/news/', NewsAPIList.as_view()),
    path('api/v1/news/<uuid:pk>/', NewsAPIDetail.as_view()),
]
urlpatterns+=doc_urls
