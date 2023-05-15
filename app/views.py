from django.shortcuts import get_object_or_404, redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def signinpage(request):
    form=CustomUserForm()
    if request.method == 'POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,user + ",your registration is successfull 🤩 ")
            return redirect('login')
    context={
        'form':form
        }
    return render (request,'signup.html',context)
def loginpage(request):
   if request.user.is_authenticated:
    return redirect('content')
   else:
    if request.method == 'POST':
        uname=request.POST.get('username').lower()
        pass1=request.POST.get('password')
        user=authenticate(request,username=uname,password=pass1)
        if user is not None:
            login(request,user)
            messages.success(request,"Login Successfull 🤗")
            return redirect('content')
        else:
            messages.info(request,"Please check the username and password 😐")
            return redirect('login')
    return render (request,'loginpage.html')
def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"you have been successfully logged out from this page 😊 ")
        return redirect('login')
def content(request):
    if request.method == "POST":
        form=upload(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'file uploaded successfully!')
            return redirect('content')
    else:
        form=upload()
    show_content=csv.objects.all()
    context={
        'show_content':show_content,
        'form':form
        
    }
    return render(request,'content.html',context)
def show(request):
    
    return render(request,'content.html')
def edit(request,id):
    dataget=csv.objects.get(id=id)
    form=upload(request.POST,instance=dataget)
    if form.is_valid():
        form.save()
        messages.success(request,'file edited successfully!')
    context={
        'form':form,
        'dataget':dataget
    }
    return render(request,'content.html',context)
def delete(request,id):
    dataget=csv.objects.get(id=id)
    dataget.delete()
    return redirect('content')