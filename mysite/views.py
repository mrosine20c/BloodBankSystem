from django.shortcuts import HttpResponseRedirect, render,redirect
from django.contrib.auth import login as loginFrom,authenticate
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User,Group
from django.db.models import Q




def indexall(request):
    return render(request, 'site/base.html')

def login(request):
    if(request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username+" "+password)
        user = authenticate(username=username,password=password)
        # print(user.is_active)
        if user is not None:
                loginFrom(request,user)
                return redirect('dashboard')
        else:
            messages.error(request,'username or password not correct')
            return redirect('login')
    return render(request, 'site/login.html')
    

def signup(request):
     if(request.method=='POST'):
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if(password!=cpassword):
            messages.error(request,'password not match')
            return redirect('signup')
        else:

            #  if User.objects.filter(Q(username=username)).exists:
            #     messages.error(request,'User with this username already exist')
            #     return redirect('signup')  
             group = Group.objects.filter(Q(name="hospital"))
             if(group.exists):
                group = Group.objects.get(name="hospital")
                users = User.objects.create_user(
                                        email=email, password=password, username=username)
                users.save()
                users.groups.add(group)

                messages.error(request,'account created')
                return redirect('login')
             else:
                messages.error(request,'something went wrong')
                return redirect('signup')   
     return render(request, 'site/signup.html')

def dashboard(request):
    return render(request,'site/dashboard/dashboard.html')

def collectors(request):
    return render(request,'site/dashboard/collectors.html')