from django.db import models

# Create your models here.
Blood_Groups = (
    ('A+','A-'),
    ('A-', 'A+'),
    ('B+','B+'),
    ('B-','B-'),
    ('O+','O+'),
    ('O-','O-'),
    ('AB+', 'AB+'),
    ('AB-','AB-'),
)

Gender = (
    ('male','Male'),
    ('female', 'Female'),
    ('transgender', 'Transgender'),
)

class bloodcamp(models.Model):
    campid=models.CharField(blank=False,null=False,max_length=150)
    startdate=models.DateField()
    enddate=models.DateField()
    location=models.CharField(blank=False,null=False,max_length=150)
    status=models.BooleanField(default=True)
class bloodcampdonor(models.Model):
    firstname=models.CharField(blank=False,null=False,max_length=150)
    lastname=models.CharField(blank=False,null=False,max_length=150)
    email=models.EmailField(unique=True)
    phone = models.CharField(max_length = 11, blank = True)
    gender=models.CharField(max_length=15,choices=Gender)
    date=models.DateField(auto_now=True,auto_now_add=False)
    blood=models.CharField(max_length=10,choices=Blood_Groups)
    bloodcamp=models.ForeignKey(bloodcamp,on_delete=models.CASCADE)
