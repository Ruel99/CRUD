from django.shortcuts import render, redirect
#login system imports
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse

#decorators imports
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group

from .forms import EmployeeForm
from .models import Employee #importing the employee table from database
from .forms import AppoinmentForm
from .forms import Appointment



#login system views
@unauthenticated_user
def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            #auto assigns a user in the student group
            group = Group.objects.get(name='student')
            user.groups.add(group)

            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    
    return render(request,'registration/sign_up.html', {"form":form})

@unauthenticated_user
def default_home(request):
    return render(request, 'myapp/default_home.html')


@login_required(login_url='login')
def home(request):
    return render(request,"myapp/home.html")


# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
def employee_list(request):
    context = {"employee_list":Employee.objects.all()}
    return render(request,"myapp/employee_list.html",context)

#this view would be used to insert and update the form
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
def employee_form(request, id=0): # the reason for having id=0 is to see if it is an insert or update request. So if id=0 we know it is in insert, if id !=0 it is an update.
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request,"myapp/employee_form.html", {'form':form})
    else:
        #Saving data to the database
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

#this view would be used to delete a record from the form
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')

#........................................................................................................

                                                #STUDENT APPOINTMENT VIEWS
#viewing appointments
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'student'])
def STUappointment_list(request):
    email = request.user.email  
    appointments = Appointment.objects.filter(email=email)
    context = {"appointment_list": appointments}
    return render(request, "myapp/appointment_list.html", context)

#...........................................................................................................

#APPOINTMENT VIEWS
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'student'])
def appointment_list(request):
    context = {"appointment_list":Appointment.objects.all()}
    return render(request,"myapp/appointment_list.html", context) 


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'student'])
def appointment_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = AppoinmentForm()
        else:
            appointment = Appointment.objects.get(pk=id)
            form = AppoinmentForm(instance=appointment)
        return render(request, "myapp/appointment_form.html", {'form': form})
    else:
        if id == 0:
            form = AppoinmentForm(request.POST)
        else:
            appointment = Appointment.objects.get(pk=id)
            form = AppoinmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
        if request.user.is_authenticated:
            for group in request.user.groups.all():
                if group.name == "admin":
                    return redirect('appointment_list')
                else:
                    return redirect('STUappointment_list')
    return redirect('login')  # Handle the case where the user is not authenticated


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'student'])
def appointment_delete(request, id):
    appointment = Appointment.objects.get(pk=id)
    appointment.delete()
    return redirect('appointment_list')