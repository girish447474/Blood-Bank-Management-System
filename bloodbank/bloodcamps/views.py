from django.shortcuts import render
from django.http import HttpResponse
from bloodcamps.models import bloodcamp,bloodcampdonor
from bloodcamps.forms import newcamp,newdonor
from datetime import date


# Create your views here.
def index(request):
    return render(request,'bloodcamps/index.html')
def camphome(request):
    return render(request,'bloodcamps/camphome.html')


def is_past_due(o):
    return date.today() > o.enddate

def def_fun(request):
    camps = bloodcamp.objects.filter(status=True)
    for camp in camps:
        if is_past_due(camp):
            camp.status=False
            camp.save()

def history(request):
    def_fun(request)

    camps=bloodcamp.objects.filter(status=False)
    donors=bloodcampdonor.objects.all()

    for camp in camps:
        print(camp.campid)
        if donors:
            for donor in donors:
                if donor.bloodcamp.campid == camp.campid:
                    print(donor.firstname)

    #print('camps:',camps)
    #print('donors:',donors)
    content = {
        'camps' : camps,
        'donors': donors,
    }
    return render(request,'bloodcamps/history.html',context=content)

def upcoming(request):
    def_fun(request)

    camps=bloodcamp.objects.filter(status=True)
    donors=bloodcampdonor.objects.all()

    for camp in camps:
        print(camp.campid)
        if donors:
            for donor in donors:
                if donor.bloodcamp.campid == camp.campid:
                    print(donor.firstname)

    #print('camps:',camps)
    #print('donors:',donors)
    content = {
        'camps' : camps,
        'donors': donors,
    }

    return render(request,'bloodcamps/upcoming.html',context=content)
def newcamppage(request):
    form=newcamp()
    if request.method=='POST':
        form=newcamp(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return camphome(request)
        else:
            print('form invalid')
    return render(request,'bloodcamps/newcamp.html',{'form':form})
def newupcomingcamp(request):
    form=newupcomingcamp()
    if request.method=='POST':
        form=newupcomingcamp(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return upcoming(request)
        else:
            print('form invalid')
    return render(request,bloodcamps/newcamp)
def newdonorpage(request):
    form1=newdonor()
    if request.method=='POST':
        form1=newdonor(request.POST)
        if form1.is_valid():
            form1.save(commit=True)
            return camphome(request)
        else:
            print('form invalid')
    return render(request,'bloodcamps/newdonor.html',{'form1':form1})
