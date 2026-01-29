from email import message

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
from myapp.models import Complaint, Users


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
    data=Complaint.objects.all()
    return render(request,'admins/viewcomplaint.html',{'data':data})

def viewevidence_get(request):
    return render(request,'admins/viewevidence.html')

def viewuser_get(request):
    users=Users.objects.all()
    return render(request,'admins/viewuser.html',{'data':users})

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






def sentreply_get(request,id):
    return render(request,'admins/sentreply.html',{'id':id})

def sentreply_post(request):
    reply=request.POST['reply']
    id=request.POST['id']
    c=Complaint.objects.get(id=id)
    c.reply=reply
    c.status='replied'
    c.save()
    return redirect('myapp/viewcomplaint_get/')

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

def add_audiovisualevidence_get(request):
    return render(request,'users/add_audiovisualevidence.html')
def add_audiovisualevidence_post(request):
    Filename=request.FILES["File name"]
    mediaType= request.POST["media Type"]
    duration_seconds= request.POST["duration_seconds"]
    format = request.POST["format"]
    Collectedfrom = request.POST["Collected from"]
    Collectedat = request.POST["Collected at"]
    filehash = request.POST["file hash"]

    return render(request,'users/add_audiovisualevidence.html')

def add_biologicalevidence_get(request):
    return render(request,'users/add_biologicalevidence.html')
def add_biologicalevidence_post(request):
    Filename = request.FILES["File name"]
    evidence=request.POST["Evidence"]
    Source = request.POST["Source"]
    CollectionLocation=request.POST["Collection Location"]
    CollectedDate=request.POST["Collected Date"]
    CollectedTime=request.POST["Collected Time"]
    Labrefernceid=request.POST["Lab refernce id"]
    narration=request.POST["narration"]

    return render(request,'users/add_biologicalevidence.html')

def add_chemicalevidence_get(request):
    return render(request,'users/add_chemicalevidence.html')
def add_chemicalevidence_post(request):
    Filename = request.FILES["File name"]
    SubstanceType = request.POST["Substance Type"]
    quantity = request.POST["quantity"]
    Collectedfrom = request.POST["Collected from"]
    Collectedat = request.POST["Collected at"]
    lab_reference_id = request.POST["lab_reference_id"]
    digitalhash = request.POST["digital hash"]

    return render(request,'users/add_chemicalevidence.html')

def add_digitalevidence_get(request):
    return render(request,'users/add_digitalevidence.html')
def add_digitalevidence_post(request):
    Filename = request.FILES["File name"]
    FileType = request.POST["File Type"]
    Filesize = request.POST["File size"]
    Hashvalue = request.POST["Hash value"]
    Collectedsource = request.POST["Collected source"]
    CollectedTime = request.POST["Collected Time"]
    PreservationTime = request.POST["Preservation Time"]
    return render(request,'users/add_digitalevidence.html')

def add_documentevidence_get(request):
    return render(request,'users/add_documentevidence.html')
def add_documentevidence_post(request):
    Filename = request.FILES["File name"]
    DocumentType = request.POST["Document Type"]
    Title = request.POST["Title"]
    Pages = request.POST["Pages"]
    Collectedfrom = request.POST["Collected from"]
    Collectedat = request.POST["Collected at"]
    filehash = request.POST["file hash"]
    return render(request,'users/add_documentevidence.html')

def add_financialaccountingevidence_get(request):
    return render(request,'users/add_financialaccountingevidence.html')
def add_financialaccountingevidence_post(request):
    Filename = request.FILES["File name"]
    TransactionType = request.POST["Transaction Type"]
    reference_number = request.POST["reference_number"]
    amount = request.POST["amount"]
    Collectedfrom = request.POST["Collected from"]
    Collectedat = request.POST["Collected at"]
    digitalhash = request.POST["digital hash"]
    return render(request,'users/add_financialaccountingevidence.html')

def add_patternevidence_get(request):
    return render(request,'users/add_patternevidence.html')
def add_patternevidence_post(request):
    Filename = request.FILES["File name"]
    PatternType = request.POST["Pattern Type"]
    capturemethod = request.POST["capture method"]
    Collectedfrom = request.POST["Collected from"]
    Collectedat = request.POST["Collected at"]
    filehash = request.POST["file hash"]
    return render(request,'users/add_patternevidence.html')

def add_physicalevidence_get(request):
    return render(request,'users/add_physicalevidence.html')
def add_physicalevidence_post(request):
    Filename = request.FILES["File name"]
    evidencetype = request.POST["evidencetype"]
    Description = request.POST["Description"]
    CollectionLocation = request.POST["Collection Location"]
    CollectedDate = request.POST["Collected Date"]
    CollectedTime = request.POST["Collected Time"]
    digitalhash = request.POST["digital hash"]
    return render(request,'users/add_physicalevidence.html')

def add_traceevidence_get(request):
    return render(request,'users/add_traceevidence.html')
def add_traceevidence_post(request):
    Filename = request.FILES["File name"]
    TraceType = request.POST["Trace Type"]
    Description = request.POST["Description"]
    Collectedfrom = request.POST["Collected from"]
    Collectedat = request.POST["Collected at"]
    storagelocation = request.POST["storage location"]
    digitalhash = request.POST["digital hash"]
    return render(request,'users/add_traceevidence.html')








