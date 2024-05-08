from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import departments,doctors1,name
from .forms import bookingsForm
from django.contrib.auth .models import auth,User
from  django .db.models import Q
import razorpay

from django.contrib.auth import authenticate, login


def invalid(request):
       return  render (request,'ivalid.html')
def index(request):
       return  render (request,'index.html')
def about(request):
       return render( request,'about.html')
def booking(request):
       if request.method =="POST":
        form =bookingsForm(request.POST)
        if form. is_valid():
              form.save()
              return render(request,'confirmation.html')
       form=bookingsForm
       dict_book={'form':form}
       return render( request,'booking.html',dict_book)

def doctors(request):
    if request.method=="POST":
         name=request.POST.get('name')
         results=doctors1.objects.filter(Q(doc_name__icontains=name))
         sufu={'result':results}
         return render (request,'doctors.html',sufu)

    dict_doc = {'doc': doctors1.objects.all()}
   

   

    return render(request, 'doctors.html', dict_doc,)


def contact(request):
      return render( request,'contact.html')



def department(request):
    if request.method=="POST":
         
      amount= 100,
      currency='INR'
      client = razorpay.Client(auth=("rzp_test_bExXeTSGdRlunx", "IQm8XkvZmAl3F61mT7mJLbrK"))
      payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
    
       
    dict_dept={'dept':departments.objects.all()}
    return render(request,"department.html",dict_dept) 



def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            return render(request,'about.html')

        # Check if the password and confirm_password match
        if password != confirm_password:
            return render(request,'contact.html')

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return redirect('login')
    else:
        return render(request, 'signup.html')

















from django.contrib.auth import authenticate, login

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('index')  # Replace 'dashboard' with the actual URL or name of the dashboard page
        else:
            return render(request,'invalid.html')

    return render(request, 'login.html')
