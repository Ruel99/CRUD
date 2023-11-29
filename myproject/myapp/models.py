from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)

    #this function displays the title of the position in the drop-down menu instead of the object
    def __str__(self):
        return self.title 

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=100)

#creating foreign key here so when it is deleted in the position table it would be deleted in 
# the employee tables as well and vice versa
    position = models.ForeignKey(Position, on_delete=models.CASCADE) 


#APPOINTMENT TABLE TEST
class Department(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Appointment(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    person_of_intrest = models.CharField(max_length=100)
    date = models.DateTimeField(null=True, blank=True)
    time = models.TimeField(null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


