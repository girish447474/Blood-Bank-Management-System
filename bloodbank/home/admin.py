from django.contrib import admin

# Register your models here.
from .models import DonorAddress,DonorProfile
#from django.contrib.auth.models import User

admin.site.register(DonorAddress)
admin.site.register(DonorProfile)
