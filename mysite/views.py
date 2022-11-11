from django.shortcuts import HttpResponseRedirect, render,redirect
from django.contrib.auth import login as loginFrom,authenticate
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User,Group
from django.db.models import Q
from django.db import models
from . import models
 



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

    bloodA1 = models.RbcStock.objects.get(blood_type="A+")
    bloodA0 = models.RbcStock.objects.get(blood_type="A-")
    bloodAB1 = models.RbcStock.objects.get(blood_type="AB+")
    bloodAB0 = models.RbcStock.objects.get(blood_type="AB-")
    bloodB1 = models.RbcStock.objects.get(blood_type="B+")
    bloodB0 = models.RbcStock.objects.get(blood_type="B-")
    bloodO1 = models.RbcStock.objects.get(blood_type="O+")
    bloodO0 = models.RbcStock.objects.get(blood_type="O-")

    donors = models.Donors.objects.count()
    totalblood= bloodA1.blood_quantity + bloodA0.blood_quantity +bloodB1.blood_quantity+bloodB0.blood_quantity+bloodAB1.blood_quantity+bloodAB0.blood_quantity+bloodO1.blood_quantity+bloodO0.blood_quantity
    
    context = {'bloodA1':bloodA1,
                'bloodA0':bloodA0,
                'bloodAB1':bloodAB1,
                'bloodA0':bloodAB0,
                'bloodB1':bloodB1,
                'bloodA0':bloodB0,
                'bloodO1':bloodO1,
                'bloodO0':bloodO0,
                'totaldonors':donors, 
                'totalblood':totalblood
                
                }
    return render(request,'site/dashboard/dashboard.html',context)

def collectors(request):
    list = User.objects.all()
    context= {'list':list}
    return render(request,'site/dashboard/collectors.html',context)


def registercollectors(request):
     if(request.method=='POST'):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if(password!=cpassword):
            messages.error(request,'password not match')
            return redirect('register-collector')
        else:

            #  if User.objects.filter(Q(username=username)).exists:
            #     messages.error(request,'User with this username already exist')
            #     return redirect('signup')  
             group = Group.objects.filter(Q(name="collector"))
             if(group.exists):
                group = Group.objects.get(name="collector")
                users = User.objects.create_user(
                                        first_name=first_name,last_name=last_name,email=email, password=password, username=username)
                users.save()
                users.groups.add(group)

                messages.error(request,'account created')
                return redirect('./collector')
             else:
                messages.error(request,'something went wrong')
                return redirect('register-collector')   
     return render(request, 'site/forms/register-collectors.html')


def donors(request):
    list = models.Donors.objects.all()
    context= {'list':list}
    return render(request,'site/dashboard/donors.html',context)


def registerdonors(request):
     
    if(request.method=='POST'):
        first_name=request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        age= request.POST.get('age')
        body_weight = request.POST.get('body_weight')
        phone_number=request.POST.get('phone_number')
        blood_type=request.POST.get('blood_type')
        blood_quantity=request.POST.get('blood_quantity')

        donors= models.Donors(
            first_name= first_name,
            last_name= last_name,
            age = age,
            body_weight= body_weight,
            phone_number= phone_number,
            blood_type= blood_type,
            blood_quantity= blood_quantity,
            # created_by = request.user.id

        )

        # update rbc stock
        d= models.RbcStock.objects.get(blood_type=blood_type)
        d.blood_quantity = d.blood_quantity + int(blood_quantity)
        d.save()

        donors.save()

       

        messages.error(request,'donor added suscessfully')
        return redirect('/donors')
    else:
        return render(request, 'site/forms/register-donors.html')
    

def collectors(request):
    list = models.User.objects.all()
    context= {'list':list}
    return render(request,'site/dashboard/collectors.html',context)


def patients(request):
    list = models.Patients.objects.all()
    context= {'list':list}
    return render(request,'site/dashboard/patients.html',context)


def registerpatients(request):
    if(request.method=='POST'):
        first_name=request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        age= request.POST.get('age')
        body_weight = request.POST.get('body_weight')
        phone_number=request.POST.get('phone_number')
        blood_type=request.POST.get('blood_type')
        blood_quantity=request.POST.get('blood_quantity')

        patients= models.Patients(
            first_name= first_name,
            last_name= last_name,
            age = age,
            body_weight= body_weight,
            phone_number= phone_number,
            blood_type= blood_type,
            blood_quantity= blood_quantity,
            hospital= request.user.username
            # created_by = request.user.id

        )
        patients.save()
        messages.error(request,'patient added successfully')
        return redirect('/patients')
    else:
        return render(request, 'site/forms/register-patients.html')
    
 
def rbcstock(request):
    stock = models.RbcStock.objects.all()
    context = {'stock':stock}
    return render(request,'site/dashboard/rbc_stock.html',context)
    
# def registercollectors(request):
#     return render(request,'site/forms/register-collectors.html')

def hospitalrequest(request):
    return render(request,'site/forms/hospital-request-form.html')

def registerpatients(request):
    return render(request, 'site/forms/register-patients.html')