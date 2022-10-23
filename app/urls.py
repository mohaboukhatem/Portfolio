from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('contact',views.contact,name='contact'),
    path('',views.index,name='index'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('resume',views.resume,name='resume')
]
