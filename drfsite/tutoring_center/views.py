from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from .forms import *

class TutorAPIList(generics.ListCreateAPIView):
   queryset = Tutor.objects.all()
   serializer_class = TutorSerializer
   filterset_fields = ['first_name','last_name','middle_name','birthday','phone','email','education']
   ordering_fields = ['first_name','last_name','middle_name','birthday','phone','email','education']

class TutorAPIDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Tutor.objects.all()
   serializer_class = TutorSerializer


class UserAPIVList(generics.ListCreateAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   filterset_fields = ['login']

class UserAPIDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer


class StudentAPIList(generics.ListCreateAPIView):
   queryset = Student.objects.all()
   serializer_class = StudentSerializer
   filterset_fields = ['first_name','last_name','middle_name','birthday','phone','email','grade','parent_fio','parent_phone']
   ordering_fields = ['first_name','last_name','middle_name','birthday','phone','email','grade','parent_fio','parent_phone']
 
class StudentAPIDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Student.objects.all()
   serializer_class = StudentSerializer


class AdministratorAPIList(generics.ListCreateAPIView):
   queryset = Administrator.objects.all()
   serializer_class = AdministratorSerializer

class AdministratorAPIDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Administrator.objects.all()
   serializer_class = AdministratorSerializer


class ServiceAPIList(generics.ListCreateAPIView):
   queryset = Service.objects.all()
   serializer_class = ServiceSerializer
   filterset_fields = ['tutor','info_about_service','subject','price','level']
   ordering_fields = ['tutor','info_about_service','subject','price','level']
   
class ServiceAPIDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Service.objects.all()
   serializer_class = ServiceSerializer


class SubjectAPIList(generics.ListCreateAPIView):
   queryset = Subject.objects.all()
   serializer_class = SubjectSerializer
   filterset_fields = ['name']

class SubjectAPIDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Subject.objects.all()
   serializer_class = SubjectSerializer


class RegistrationForServiceAPIList(generics.ListCreateAPIView):
   queryset = RegistrationForService.objects.all()
   serializer_class = RegistrationForServiceSerializer
   filterset_fields = ['tutor','student','service','start_date','end_date','theme_of_lesson','additional_info','status']
   ordering_fields = ['tutor','student','service','start_date','end_date','theme_of_lesson','additional_info','status']

class RegistrationForServiceAPIDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = RegistrationForService.objects.all()
   serializer_class = RegistrationForServiceSerializer


class HomeworkAPIList(generics.ListCreateAPIView):
   queryset = Homework.objects.all()
   serializer_class = HomeworkSerializer
   filterset_fields = ['student','tutor','start_date','end_date','theme','description']
   ordering_fields = ['student','tutor','start_date','end_date','theme','description']

class HomeworkAPIDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Homework.objects.all()
   serializer_class = HomeworkSerializer


class FileAPIList(generics.ListCreateAPIView):
   queryset = File.objects.all()
   serializer_class = FileSerializer
   filterset_fields = ['news','name']
   ordering_fields = ['news','name']

class FileAPIDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = File.objects.all()
   serializer_class = FileSerializer


class NewsAPIList(generics.ListCreateAPIView):
   queryset = News.objects.all()
   serializer_class = NewsSerializer
   filterset_fields = ['title','short_description','description']
   ordering_fields = ['title','short_description','description']

class NewsAPIDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = News.objects.all()
   serializer_class = NewsSerializer

def register(request):
	if request.method =='POST':
		form = RegistrationForm(request.POST)
		user_form = ProfiloUtenteForm(request.POST)
		if form.is_valid() and profilo_utente_form.is_valid():

			user = form.save()
			profile = profilo_utente_form.save(commit=False)
			profile.user = user

			profile.save()
			profilo_utente_form.save_m2m()

			return redirect('/incarico_slice')
		else:
			args = {'form': form, 'profilo_utente_form': profilo_utente_form}
			return render(request, 'accounts/register.html', args)
	else:
		form = RegistrationForm()

		profilo_utente_form = ProfiloUtenteForm()


	args = {'form': form, 'profilo_utente_form': profilo_utente_form}
	return render(request, 'accounts/register.html', args)