from django.urls import path,include
from . import views

urlpatterns = [
    #login system urls
    path('sign-up/', views.sign_up, name='sign_up'),

    path('home', views.home, name='home'),

    path('', views.default_home, name='default_home'),

    #Employee CRUD urls
    path('form/',views.employee_form, name='employee_insert'), #get and post req. for insert operation

    path('form/<int:id>/',views.employee_form, name='employee_update'), # get and post req. for update operation
    
    #URL LINK: localhost:portnum/employee/list
    path('list/',views.employee_list, name='employee_list'),# get req. to retrieve and display all records

    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),

#Student Appointment URLs
path('STUappointment_list', views.STUappointment_list, name='STUappointment_list'),

#APPOINTMENT URLs
    path('appointment/', views.appointment_form, name='appointment_insert'),

    path('appointment/list', views.appointment_list, name='appointment_list'),

    path('appointment/<int:id>', views.appointment_form, name='appointment_update'),

    path('appointment/delete/<int:id>/', views.appointment_delete, name='appointment_delete'),


]