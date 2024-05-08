from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('registration/', views.registraion,name='registration'),
    path('companies/', views.companies,name='companies'),
    path('vacancy/', views.vacancy,name='vacancy'),
    path('hiring/', views.hiring,name='hiring'),
    path('jobs/', views.jobs,name='jobs'),


]
