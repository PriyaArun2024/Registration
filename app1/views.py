from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

# def loginpage(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         print(username,password)
#         user=authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('homepage')
#         else:
#             return HttpResponse('invalid details')
#     return render(request,'login.html') 
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return HttpResponse('Invalid details')
    
    return render(request, 'login.html')

def signuppage(request):
     if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        cnpassword=request.POST.get('cnpassword')
        if password!=cnpassword:
            return HttpResponse('password didnot matched')
        else:
            new_user=User.objects.create_user(username,password)
            new_user.save()
            return redirect('login')
            
     return render(request,'signup.html') 
def logoutpage(request):
    logout(request)
    return redirect('login')
def homepage(request):
     return render(request,'home.html') 