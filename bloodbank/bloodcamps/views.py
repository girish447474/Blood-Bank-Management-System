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


def checkdate(o):
    if(date.today() > o.enddate):
        print('check 1')
        return  '1'
    elif(date.today() < o.startdate):
        print('check 3')
        return  '3'
    else:
        print('check 2')
        return  '2'
def default_fun(request):
    camps = bloodcamp.objects.all()
    for camp in camps:
        if checkdate(camp) == '1' :
            print('is 1')
            camp.status='1'
            camp.save()
        elif checkdate(camp) == '2' :
            print('is 2')
            camp.status='2'
            camp.save()
        elif checkdate(camp) == '3' :
            print('is 3')
            camp.status='3'
            camp.save()


def history(request):
    default_fun(request)

    camps=bloodcamp.objects.filter(status='1')
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
def ongoing(request):
    default_fun(request)

    camps=bloodcamp.objects.filter(status=2)
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
    return render(request,'bloodcamps/ongoing.html',context=content)

def upcoming(request):
    default_fun(request)

    camps=bloodcamp.objects.filter(status=3)
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
