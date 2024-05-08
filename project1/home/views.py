from django.shortcuts import render
from django.http import HttpResponse
from .models import company,job,registration
from .forms import registrationform

# Create your views here.
def index(request):   
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def registraion(request):
    if request.method == "POST":
           form = registrationform(request.POST)
           if form.is_valid():
                   form.save()
                   return render(request,'jobs.html',{'form':form})
    else:
            form = registrationform()    
            return render(request,'registration.html',{'form':form})

    
def companies(request):
    dict_comp={
        'comp': company.objects.all()
    } 
    return render(request, 'companies.html', dict_comp)
def vacancy(request):
    return render(request, 'vacancy.html')
def hiring(request):
    return render(request, 'hiring.html')
def jobs(request):
    dict_jobs = {
        'job': job.objects.all()
    }
    return render(request, 'jobs.html',dict_jobs)






