from django.contrib import admin

# Register your models here.
from .models import *
#from django.contrib.auth.models import User

admin.site.register(DonorAddress)
admin.site.register(DonorProfile)
admin.site.register(DonorHistory)
admin.site.register(Wallet)
admin.site.register(Transaction)
admin.site.register(AcceptorAddress)
admin.site.register(AcceptorProfile)
admin.site.register(AcceptorHistory)
admin.site.register(BloodCamp)
admin.site.register(BloodCampDonor)
