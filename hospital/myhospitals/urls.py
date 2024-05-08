from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('index/',views.index,name='index'),
    path('about/',views.about, name='about'),
    path('booking/',views.booking,name='booking'),
    path('doctors/',views.doctors,name='doctors'),
    path('contact/',views.contact,name='contact'),
    path('department/', views.department ,name='department'),
    path('invalid/',views.invalid,name='invalid'),
]