from email import message

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
def login_get(request):
    return render(request,'login1.html')
def login_post(request):
    username=request.POST['username']
    password=request.POST['password']

    user=authenticate(request,username=username,password=password)

    if user is not None:
        login(request,user)
        if user.groups.filter(name='admin'):
            return redirect('/myapp/adminhome_get/')
        else:
            messages.error(request,'error')
            return redirect('/myapp/login_get/')
    else:
        messages.error(request, 'error')
        return redirect('/myapp/login_get/')



# A D M I N ---------

def adminhome_get(request):
    return render(request,'admins/adminhomeindex.html')

# def loginindex

def viewcomplaint_get(request):
    return render(request,'admins/viewcomplaint.html')

def viewevidence_get(request):
    return render(request,'admins/viewevidence.html')

def viewuser_get(request):
    return render(request,'admins/viewuser.html')

def changepassword_get(request):
    return render(request,'admins/changepassword.html')

def changepassword_post(request):
    current_password=request.POST['currentpassword']
    new_password=request.POST['newpassword']
    confirm_password=request.POST['confirmpassword']


    data=request.user
    if not data.check_password(current_password):
        messages.error(request,'invalid password')
        return redirect('/myapp/changepassword_get/')
    if new_password != confirm_password:
        messages.error(request,'Password not match')
        return redirect('/myapp/changepassword_get/')

    data.set_password(new_password)
    data.save()
    return redirect('/myapp/login_get/')




    return render(request,'admins/changepassword.html')


def sentreply_get(request):
    return render(request,'admins/sentreply.html')

def sentreply_post(request):
    return render(request,'admins/sentreply.html')

# USERS

def edit_get(request):
    return render(request,'users/edit.html')

def edit_post(request):
    return render(request,'users/edit.html')

def forgotpassword_get(request):
    return render(request,'users/forgotpassword.html')

def forgotpassword_post(request):
    return render(request,'users/forgotpassword.html')

def register_get(request):
    return render(request,'users/register.html')

def register_post(request):
    return render(request,'users/register.html')


def sentcomplaint_get(request):
    return render(request,'users/sentcomplaint.html')

def sentcomplaint_post(request):
    return render(request,'users/sentcomplaint.html')


def user_viewcomplaint_get(request):
    return render(request,'users/viewcomplaint.html')

def viewprofile_get(request):
    return render(request,'users/viewprofile.html')



