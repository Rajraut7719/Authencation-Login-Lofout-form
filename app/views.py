from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render,HttpResponseRedirect
from .forms import Sign_upForm,Sign_in_Form
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
# Register Form
def sign_up(request):
    if request.method=='POST':
        fm=Sign_upForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Successfully')
            fm.save()
            return redirect('/')
    else:
        fm=Sign_upForm()
    return render(request,'app/sign_up.html',{'form':fm})
# Login Form
def sign_in(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=Sign_in_Form(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Successfullay')
                    return HttpResponseRedirect('/profile/')
        else:
            fm=Sign_in_Form()
        return render(request,'app/sign_in.html',{'form':fm})
    else:
        return  HttpResponseRedirect('profile')


# Profile
def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'app/profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/sign-in/')

# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/sign-in/')