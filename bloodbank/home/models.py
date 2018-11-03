from django.db import models
from django import forms
from django.contrib.auth.models import User

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

States = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Goa', 'Goa'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('karnataka', 'karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Goa', 'Goa'),
    ('Telangana', 'Telangana'),
    ('Tripura','Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),


)



class DonorAddress(models.Model):
    donoraddressid = models.AutoField(primary_key = True)
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    state = models.CharField(max_length = 30, choices=States)
    city = models.CharField(blank = False, null = False, max_length = 200)
    phone = models.CharField(blank = False, null = False, max_length = 100)
    birth = models.CharField(blank = False, null = False, max_length = 200)
    gender = models.CharField(max_length=15, choices=Gender)
    date = models.DateTimeField(auto_now_add = True)
    blood = models.CharField(max_length=10, choices=Blood_Groups)

class DonorProfile(models.Model):
    donorprofileid = models.AutoField(primary_key = True)
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    #donoraddress = models.OneToOneField(DonorAddress,on_delete = models.CASCADE)
    status = models.CharField(null = True, max_length = 200)
    feedback = models.CharField(null = True, max_length = 1000)


class DonorHistory(models.Model):
    donorhistoryid = models.AutoField(primary_key = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    #username=models.CharField(max_length =200, null = False, blank = False)
    donation_date = models.DateTimeField(auto_now = True, auto_now_add = False)

# Donor's Wallet

class Wallet(models.Model):
    walletid = models.AutoField(primary_key = True)
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    credit = models.IntegerField(default = 0)

class Transaction(models.Model):
    transactionid = models.AutoField(primary_key = True)
    wallet = models.ForeignKey(Wallet, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)
    initialcredit = models.IntegerField(null = True, blank = True)
    aftercredit = models.IntegerField(null = True, blank = True)
    getcredit = models.IntegerField(null = True)
    def updatewallet(self):
        self.wallet.credit = self.wallet.credit + self.getcredit




# Acceptor class



class AcceptorAddress(models.Model):
    acceptoraddressid = models.AutoField(primary_key = True)
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    state = models.CharField(max_length = 30, choices=States)
    city = models.CharField(blank = False, null = False, max_length = 200)
    phone = models.CharField(blank = False, null = False, max_length = 100)
    #birth = models.CharField(blank = False, null = False, max_length = 200)
    gender = models.CharField(max_length=15, choices=Gender)
    date = models.DateTimeField(auto_now = True, auto_now_add = False)
    blood = models.CharField(max_length=10, choices=Blood_Groups)

class AcceptorProfile(models.Model):
    acceptorprofileid = models.AutoField(primary_key = True)
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    status = models.CharField(null = True, max_length = 200)
    feedback = models.CharField(null = True, max_length = 1000)


class AcceptorHistory(models.Model):
    acceptorhistoryid = models.AutoField(primary_key = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    #username=models.CharField(max_length =200, null = False, blank = False)
    acceptation_date = models.DateTimeField(auto_now = True, auto_now_add = False)


#Blood Donation Camp


class BloodCamp(models.Model):
    place = models.CharField(blank=False, null = False, max_length = 100)

class BloodCampDonor(models.Model):
    name = models.CharField(blank=False, null = False, max_length=100)
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length = 11, blank = True)
    gender = models.CharField(max_length=15, choices=Gender)
    date = models.DateTimeField(auto_now = True, auto_now_add = False)
    blood = models.CharField(max_length=10, choices=Blood_Groups)
    bloodcamp = models.ForeignKey(BloodCamp,on_delete = models.CASCADE)
