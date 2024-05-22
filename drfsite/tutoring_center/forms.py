
from .models import *


class RegistrationForm(StudentCreationForm):
   
    first_name = models.CharField(max_length=20,verbose_name="Имя")
    last_name = models.CharField(max_length=20,verbose_name="Фамилия")
    middle_name = models.CharField(max_length=20,verbose_name="Отчество")
    birthday = models.DateField(verbose_name="Дата рождения")
    email = models.CharField(max_length=30,verbose_name="Электронная почта")
    phone = models.CharField(max_length=15,verbose_name="Номер телефона")
    grade = models.CharField(max_length=15, choices=EducationLevelChoices.choices, verbose_name="Уровень образования")
    parent_fio = models.CharField(max_length=100,verbose_name="ФИО родителя", null=True)
    parent_phone = models.CharField(max_length=15,verbose_name="Номер телефона родителя", null=True)

    class Meta: # define a metadata related to this class
        model = Student
        fields = (
			'first_name',
			'last_name',
			'middle_name',
			'birthday',
			'email',
			'phone',
			'grade',
			'parent_fio',
			'parent_phone',
			'password1',
			'password2',)
        
    def save(self, commit=True):
        student = super(RegistrationForm, self).save(commit=False)
        student.first_name = self.cleaned_data['first_name']
        student.last_name = self.cleaned_data['last_name']
        student.middle_name = self.cleaned_data['middle_name']
        student.birthday = self.cleaned_data['birthday']
        student.email = self.cleaned_data['email']
        student.phone = self.cleaned_data['phone']
        student.grade = self.cleaned_data['grade']
        student.parent_fio = self.cleaned_data['parent_fio']
        student.parent_phone = self.cleaned_data['parent_phone']
        
        if commit:
            student.save() # running sql in database to store data
        return student