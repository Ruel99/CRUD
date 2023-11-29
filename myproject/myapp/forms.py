from django import forms
from .models import Employee # <- this is the name of the table
from .models import Appointment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#Stuff for the login system
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model= User
        fields = ["username", "email", "password1", "password2"]


#this class is used to make a form with fields of the attributes in the employee table
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('fullname', 'mobile', 'emp_code', 'position') #<- this would create fields of all the attributs in the employee table
        labels = {
            'fullname':'Full Name',
            'emp_code':'EMP. Code'
        }
    
    #this function puts a placeholder in the field for the position drop-down menu
    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select Position"
        self.fields['emp_code'].required = False #<- the following line of code is used to make a field not mandatory


# Appointment table test
class AppoinmentForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'DD-MM-YYYY'}),
        input_formats=['%Y-%m-%d']  # Specify the desired date format
    )
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Appointment
        fields = ('fullname', 'email', 'mobile', 'person_of_intrest', 'department', 'description', 'date', 'time')
        labels = {
            'fullname': 'Full Name',
        }


    #to add the date format in the date

    #to style the dropdown menu in the department field
    def __init__(self, *args, **kwargs):
        super(AppoinmentForm,self).__init__(*args, **kwargs)
        self.fields['department'].empty_label = "Select Department"
        self.fields['date'].required = True