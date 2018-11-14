from django.urls import path
from bloodcamps import views
app_name='bloodcamps'
urlpatterns=[
    path('',views.camphome,name='camphome'),
    path('history/',views.history,name='history'),
    path('upcoming/',views.upcoming,name='upcoming'),
    path('ongoing/',views.ongoing,name='ongoing'),
    path('newdonor/',views.newdonorpage,name='newdonorpage'),
    path('newcamp/',views.newcamppage,name='newcamppage')

]
