import datetime
from email import message
from unittest import case

from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect


# Create your views here.
from myapp.blockchain import contract, w3
from myapp.models import Complaint, Users, Case, Assigncase


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
        elif user.groups.filter(name='user'):
            return redirect('/myapp/userindex_get/')
        else:
            messages.error(request,'error')
            return redirect('/myapp/login_get/')
    else:
        messages.error(request, 'error')
        return redirect('/myapp/login_get/')


def logout_get(request):
    logout(request)
    return redirect('/myapp/login_get/')



# A D M I N ---------

def adminhome_get(request):
    return render(request,'admins/adminhomeindex.html')

# def loginindex

def viewcomplaint_get(request):
    data=Complaint.objects.all()
    return render(request,'admins/viewcomplaint.html',{'data':data})

def viewevidence_get(request):
    # a=Evidence.objects.all()
    return render(request,'admins/viewevidence.html')


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

def addstaff_get(request):
    return render(request,'admins/addstaff.html')
def addstaff_post(request):
    name=request.POST['name']
    gender=request.POST['gender']
    dob = request.POST['dob']
    email = request.POST['email']
    phone = request.POST['phone']
    photo = request.FILES['photo']
    f=FileSystemStorage()
    date=datetime.datetime.now().strftime('%d%M%Y%H%M%S')+'.jpg'
    f.save(date,photo)
    path=f.url(date)


    a=User.objects.create_user(username=email,password=phone)
    a.groups.add(Group.objects.get(name='user'))
    a.save()

    u=Users()
    u.name=name
    u.gender=gender
    u.dob=dob
    u.email=email
    u.phone=phone
    u.AUTHUSER=a
    u.photo=path
    u.save()

    return redirect('/myapp/viewuser_get/')


def viewuser_get(request):
    users=Users.objects.all()
    return render(request,'admins/viewuser.html',{'data':users})

def editstaff_get(request,id):
    a=Users.objects.get(id=id)
    return render(request, 'admins/editstaff.html',{'d':a})


def editstaff_post(request):
    name = request.POST['name']
    gender = request.POST['gender']
    dob = request.POST['dob']
    email = request.POST['email']
    phone = request.POST['phone']
    id = request.POST['id']
    u = Users.objects.get(id=id)
    k=u.AUTHUSER
    k.username=email
    k.save()


    if 'photo' in request.FILES:
        photo = request.FILES['photo']
        f = FileSystemStorage()
        date = datetime.datetime.now().strftime('%d%M%Y%H%M%S') + '.jpg'
        f.save(date, photo)
        path = f.url(date)
        u.photo = path
        u.save()


    u.name = name
    u.gender = gender
    u.dob = dob
    u.email = email
    u.phone = phone
    u.AUTHUSER = k
    u.save()

    return redirect('/myapp/viewuser_get/')

def deletestaff_get(request,id):
    Users.objects.get(AUTHUSER_id=id).delete()
    User.objects.get(id=id).delete()
    return redirect('/myapp/viewuser_get/')

def addcase_get(request):
    return render(request, 'admins/addcase.html')
def addcase_post(request):
    caseid = request.POST['caseid']
    case_title = request.POST['case_title']
    case_type = request.POST['case_type']
    date_of_incident = request.POST['date_of_incident']
    case_description = request.POST['case_description']
    date_filed = request.POST['date_filed']
    petitioner_name = request.POST['petitioner_name']
    petitioner_email = request.POST['petitioner_email']
    petitioner_phone = request.POST['petitioner_phone']
    petitioner_place = request.POST['petitioner_place']
    petitioner_pincode = request.POST['petitioner_pincode']
    petitioner_district = request.POST['petitioner_district']
    petitioner_state = request.POST['petitioner_state']
    accused = request.POST['accused']
    filing_mode = request.POST['filing_mode']
    court_name = request.POST['court_name']
    judge_assigned = request.POST['judge_assigned']

    priority = request.POST['priority']
    remarks = request.POST['remarks']
    case_duration_days = request.POST['case_duration_days']

    c=Case()
    c.caseid=caseid
    c.case_title=case_title
    c.case_type=case_type
    c.date_of_incident=date_of_incident
    c.case_description=case_description
    c.date_filed=date_filed
    c.petitioner_name=petitioner_name
    c.petitioner_email=petitioner_email
    c.petitioner_phone=petitioner_phone
    c.petitioner_place=petitioner_place
    c.petitioner_pincode=petitioner_pincode
    c.petitioner_district=petitioner_district
    c.petitioner_state=petitioner_state
    c.accused=accused
    c.filing_mode=filing_mode
    c.court_name=court_name
    c.judge_assigned=judge_assigned
    c.priority=priority
    c.remarks=remarks
    c.case_duration_days=case_duration_days
    c.save()
    return redirect('/myapp/viewcase_get/')


def viewcase_get(request):
    cases=Case.objects.all()
    return render(request,'admins/viewcase.html',{'data':cases})

def editcase_get(request,id):
    f=Case.objects.get(id=id)
    return render(request, 'admins/editcase.html',{'d':f})

def editcase_post(request):
    # caseid = request.POST['caseid']
    case_title = request.POST['case_title']
    case_type = request.POST['case_type']
    date_of_incident = request.POST['date_of_incident']
    case_description = request.POST['case_description']
    date_filed = request.POST['date_filed']
    petitioner_name = request.POST['petitioner_name']
    petitioner_email = request.POST['petitioner_email']
    petitioner_phone = request.POST['petitioner_phone']
    petitioner_place = request.POST['petitioner_place']
    petitioner_pincode = request.POST['petitioner_pincode']
    petitioner_district = request.POST['petitioner_district']
    petitioner_state = request.POST['petitioner_state']
    accused = request.POST['accused']
    filing_mode = request.POST['filing_mode']
    court_name = request.POST['court_name']
    judge_assigned = request.POST['judge_assigned']
    priority = request.POST['priority']
    remarks = request.POST['remarks']
    case_duration_days = request.POST['case_duration_days']
    case_id = request.POST['id']

    h = Case.objects.get(id=case_id)

    h.case_title = case_title
    h.case_type = case_type
    h.date_of_incident = date_of_incident
    h.case_description = case_description
    h.date_filed = date_filed
    h.petitioner_name = petitioner_name
    h.petitioner_email = petitioner_email
    h.petitioner_phone = petitioner_phone
    h.petitioner_place = petitioner_place
    h.petitioner_pincode = petitioner_pincode
    h.petitioner_district = petitioner_district
    h.petitioner_state = petitioner_state
    h.court_name = court_name
    h.accused = accused
    h.filing_mode = filing_mode
    h.judge_assigned = judge_assigned
    h.priority = priority
    h.remarks = remarks
    h.case_duration_days = case_duration_days
    h.save()

    return redirect('/myapp/viewcase_get/')

def deletecase_get(request,id):
    Case.objects.get(id=id).delete()

    return redirect('/myapp/viewcase_get/')

def assigncase_get(request):
    staff=Users.objects.all()
    case=Case.objects.all()
    return render(request,'admins/assigncase.html',{'staff':staff,'case':case})

def assigncase_post(request):
    staff=request.POST["staff"]
    case= request.POST["case"]

    data=Assigncase()
    data.USERS_id=staff
    data.CASE_id=case
    data.save()





    return redirect('/myapp/viewassignedcase_post/')

def viewassignedcase_post(request):
    data=Assigncase.objects.all()
    return render(request,'admins/viewassignedcases.html',{'data':data})

def editassigncase_get(request,id):
    f=Assigncase.objects.get(id=id)
    staff = Users.objects.all()
    case = Case.objects.all()
    return render(request, 'admins/editassigncase.html',{'d':f,'staff':staff,'case':case})



def editassigncase_post(request):
    staff=request.POST["staff"]
    case= request.POST["case"]
    id=request.POST['id']

    data=Assigncase.objects.get(id=id)
    data.USERS_id=staff
    data.CASE_id=case

    data.save()





    return redirect('/myapp/viewassignedcase_post/')

def deleteassignedcase_get(request,id):
    Assigncase.objects.get(id=id).delete()

    return redirect('/myapp/viewassignedcase_post/')



def adminview_audio_evidence(request,id):
    audio_list = []

    ids = contract.functions.getAllAudioevidenceIds().call()
    for evidence_id in ids:
        file_name, media_type,duration_seconds,format,collected_from,collected_at,file_hash,caseid = contract.functions.getAudioevidence(evidence_id).call()

        if str(caseid) == str(id):

            audio_list.append({
                "id": evidence_id,
                "file_name": file_name,
                "media_type": media_type,
                "duration_seconds": duration_seconds,
                "format": format,
                "collected_from": collected_from,
                "collected_at": collected_at,
                "file_hash": file_hash
            })
    return render(request,'admins/adminviewadd_audiovisualevidence.html', {"audioevidence": audio_list})


def adminview_biological_evidence(request,id):
    biological_list = []

    ids = contract.functions.getAllBiologicalevidenceIds().call()
    for evidence_id in ids:
        file_name, evidence_type,source,collection_location,collected_date,collected_time,lab_referenceid,narration,caseid = contract.functions.getBiologicalevidence(evidence_id).call()
        if str(caseid) == str(id):
            biological_list.append({


                "id": evidence_id,
                "file_name": file_name,
                "evidence_type": evidence_type,
                "source": source,
                "collection_location": collection_location,
                "collected_date": collected_date,
                "collected_time": collected_time,
                "lab_referenceid": lab_referenceid,
                "narration": narration
        })
    return render(request,'admins/adminviewadd_biologicalevidence.html', {"biologicalevidence": biological_list})

def adminview_chemical_evidence(request,id):
    chemical_list = []

    ids = contract.functions.getAllChemicalevidenceIds().call()
    for evidence_id in ids:
        file_name, substance_type,quantity,collected_from,collected_at,lab_refernceid,digital_hash,caseid = contract.functions.getChemicalevidence(evidence_id).call()
        if str(caseid) == str(id):
            chemical_list.append({

            "id": evidence_id,
            "file_name": file_name,
            "substance_type": substance_type,
            "quantity": quantity,
            "collected_from": collected_from,
            "collected_at": collected_at,
            "lab_refernceid": lab_refernceid,
            "digital_hash": digital_hash

        })
    return render(request,'admins/adminviewadd_chemicalevidence.html', {"chemicalevidence": chemical_list})


def adminview_digital_evidence(request,id):
    digital_list = []

    ids = contract.functions.getAllDigitalevidenceIds().call()
    for evidence_id in ids:
        file_name, file_type,file_size,hash_value,collected_source,collected_time,preservation_time,caseid = contract.functions.getDigitalevidence(evidence_id).call()
        if str(caseid) == str(id):
            digital_list.append({
            "id": evidence_id,
            "file_name": file_name,
            "file_type": file_type,
            "file_size": file_size,
            "hash_value": hash_value,
            "collected_source": collected_source,
            "collected_time": collected_time,
            "preservation_time": preservation_time,

        })
    return render(request,'admins/adminviewadd_digitalevidence.html', {"digitalevidence": digital_list})

def adminview_document_evidence(request,id):
    document_list = []

    ids = contract.functions.getAllDocumentevidenceIds().call()
    for evidence_id in ids:
        file_name, document_type,title,pages,collected_from,collected_at,file_hash,caseid = contract.functions.getDocumentevidence(evidence_id).call()
        if str(caseid) == str(id):
            document_list.append({
            "id": evidence_id,
            "file_name": file_name,
            "document_type": document_type,
            "title": title,
            "pages": pages,
            "collected_from": collected_from,
            "collected_at": collected_at,
            "file_hash": file_hash,

        })
    return render(request,'admins/adminviewadd_documentevidence.html', {"documentevidence": document_list})


def adminview_financial_evidence(request,id):
    financial_list = []

    ids = contract.functions.getAllFinancialaccoundingevidenceIds().call()
    for evidence_id in ids:
        file_name, transaction_type,reference_number,amount,collected_from,collected_at,digital_hash,caseid = contract.functions.getFinancialaccoundingevidence(evidence_id).call()
        if str(caseid) == str(id):
            financial_list.append({
            "id": evidence_id,
            "file_name": file_name,
            "transaction_type": transaction_type,
            "reference_number": reference_number,
            "amount": amount,
            "collected_from": collected_from,
            "collected_at": collected_at,
            "digital_hash": digital_hash

        })
    return render(request,'admins/adminviewadd_financialaccountingevidence.html', {"Financialaccoundingevidence": financial_list})


def adminview_pattern_evidence(request,id):
    pattern_list = []

    ids = contract.functions.getAllPatternevidenceIds().call()
    for evidence_id in ids:
        file_name, pattern_type,capture_method,collected_from,collected_at,file_hash,caseid = contract.functions.getPatternevidence(evidence_id).call()
        if str(caseid) == str(id):
            pattern_list.append({
            "id": evidence_id,
            "file_name": file_name,
            "pattern_type": pattern_type,
            "capture_method": capture_method,
            "collected_from": collected_from,
            "collected_at": collected_at,
            "file_hash": file_hash,

        })
    return render(request,'admins/adminviewadd_patternevidence.html', {"patternevidence": pattern_list})


def adminview_physical_evidence(request,id):
    physical_list = []

    ids = contract.functions.getAllPhysicalevidenceIds().call()
    for evidence_id in ids:
        file_name, evidence_type,description,collection_location,collected_date,collected_time,digital_hash,caseid = contract.functions.getPhysicalevidence(evidence_id).call()
        if str(caseid) == str(id):
            physical_list.append({
            "id": evidence_id,
            "file_name": file_name,
            "evidence_type": evidence_type,
            "description": description,
            "collection_location": collection_location,
            "collected_date": collected_date,
            "collected_time": collected_time,
            "digital_hash": digital_hash

        })
    return render(request,'admins/adminviewadd_physicalevidence.html', {"physicalevidence": physical_list})

def adminview_trace_evidence(request,id):
    trace_list = []

    ids = contract.functions.getAllTraceevidenceIds().call()
    for evidence_id in ids:
        file_name, trace_type,description,collected_from,collected_at,storage_location,digital_hash,caseid = contract.functions.getTraceevidence(evidence_id).call()
        if str(caseid) == str(id):
            trace_list.append({
            "id": evidence_id,
            "file_name": file_name,
            "trace_type": trace_type,
            "description": description,
            "collected_from": collected_from,
            "collected_at": collected_at,
            "storage_location": storage_location,
            "digital_hash": digital_hash

        })
    return render(request,'admins/adminviewadd_traceevidence.html', {"traceevidence": trace_list})









# --------------------USERS
# def viewassigncase_get(request):
#     return render(request,'users/viewassigncase.html')

def viewassigncase_post(request):
    data=Assigncase.objects.filter(USERS__AUTHUSER=request.user)
    return render(request,'users/viewassigncase.html',{'data':data})


def userindex_get(request):
    return render(request,'users/userindex.html')
def edit_get(request):
    return render(request,'users/edit.html')

def edit_post(request):
    return render(request,'users/edit.html')

def forgotpassword_get(request):
    return render(request,'users/forgotpassword.html')

def forgotpassword_post(request):
    current_password = request.POST['currentpassword']
    confirm_password = request.POST['confirmpassword']
    new_password = request.POST['newpassword']
    data = request.user
    if not data.check_password(current_password):
        messages.error(request, 'invalid password')
        return redirect('/myapp/forgotpassword_get/')
    if new_password != confirm_password:
        messages.error(request, 'Password not match')
        return redirect('/myapp/forgotpassword_get/')

    data.set_password(new_password)
    data.save()
    return redirect('/myapp/login_get/')






def register_get(request):
    return render(request,'users/register.html')

def register_post(request):
    return render(request,'users/register.html')


def sentcomplaint_get(request):

    return render(request,'users/sentcomplaint.html')

def sentcomplaint_post(request):
    complaint=request.POST['complaint']

    t=Complaint()
    t.date=datetime.datetime.now().today()
    t.sendcomplaint=complaint
    t.reply='pending'
    t.status='pending'
    t.USER=Users.objects.get(AUTHUSER_id=request.user.id)
    t.save()
    return redirect('/myapp/userindex_get/')


def user_viewcomplaint_get(request):
    return render(request,'users/viewcomplaint.html')

def viewprofile_get(request):
    return render(request,'users/viewprofile.html')

def add_audiovisualevidence_get(request,id):
    return render(request,'users/add_audiovisualevidence.html',{'id':id})

def add_audiovisualevidence_post(request):
    file=request.FILES["File name"]
    media_type= request.POST["media Type"]
    duration_seconds= request.POST["duration_seconds"]
    format = request.POST["format"]
    collected_from = request.POST["Collected from"]
    collected_at = request.POST["Collected at"]
    file_hash = request.POST["file hash"]
    caseid = request.POST["caseid"]

    fs = FileSystemStorage()
    date = datetime.datetime.now().strftime('%d%M%Y%H%M%S') + '.jpg'
    fs.save(date, file)
    file_name = fs.url(date)

    try:
        tx_hash = contract.functions.addAudioevidence(file_name,media_type,duration_seconds,format,collected_from,collected_at,file_hash,caseid).transact()
        w3.eth.wait_for_transaction_receipt(tx_hash)
        message = "EvidenceRecords " + file_name + " added successfully."
    except Exception as e:
        message = "Error: " + str(e)

    return render(request,'users/add_audiovisualevidence.html')

def add_biologicalevidence_get(request,id):
    return render(request,'users/add_biologicalevidence.html',{'id':id})
def add_biologicalevidence_post(request):
    file = request.FILES["File name"]
    evidence_type=request.POST["evidence"]
    source = request.POST["Source"]
    collection_location=request.POST["Collection Location"]
    collected_date=request.POST["Collected Date"]
    collected_time=request.POST["Collected Time"]
    lab_referenceid=request.POST["Lab refernce id"]
    narration=request.POST["narration"]
    caseid=request.POST["caseid"]

    fs = FileSystemStorage()
    date = datetime.datetime.now().strftime('%d%M%Y%H%M%S') + '.jpg'
    fs.save(date, file)
    file_name = fs.url(date)

    try:
        tx_hash = contract.functions.addBiologicalevidence(file_name,evidence_type,source,collection_location,collected_date,collected_time,lab_referenceid,narration,caseid).transact()
        w3.eth.wait_for_transaction_receipt(tx_hash)
        message = "EvidenceRecords " + file_name + " added successfully."
    except Exception as e:
        message = "Error: " + str(e)

    return render(request,'users/add_biologicalevidence.html')

def add_chemicalevidence_get(request,id):
    return render(request,'users/add_chemicalevidence.html',{'id':id})
def add_chemicalevidence_post(request):
    file = request.FILES["File name"]
    substance_type = request.POST["Substance Type"]
    quantity = request.POST["quantity"]
    collected_from = request.POST["Collected from"]
    collected_at = request.POST["Collected at"]
    lab_refernceid = request.POST["lab_reference_id"]
    digital_hash = request.POST["digital hash"]
    caseid = request.POST["caseid"]

    fs = FileSystemStorage()
    date = datetime.datetime.now().strftime('%d%M%Y%H%M%S') + '.jpg'
    fs.save(date, file)
    file_name = fs.url(date)

    try:
        tx_hash = contract.functions.addChemicalevidence(file_name,substance_type,quantity,collected_from,collected_at,lab_refernceid,digital_hash,caseid).transact()
        w3.eth.wait_for_transaction_receipt(tx_hash)
        message = "EvidenceRecords " + file_name + " added successfully."
    except Exception as e:
        message = "Error: " + str(e)


    return render(request,'users/add_chemicalevidence.html')

def add_digitalevidence_get(request,id):
    return render(request,'users/add_digitalevidence.html',{'id':id})
def add_digitalevidence_post(request):
    file = request.FILES["File name"]
    file_type = request.POST["File Type"]
    file_size = request.POST["File size"]
    hash_value = request.POST["Hash value"]
    collected_source = request.POST["Collected source"]
    collected_time = request.POST["Collected Time"]
    preservation_time = request.POST["Preservation Time"]
    caseid = request.POST["caseid"]

    fs = FileSystemStorage()
    date = datetime.datetime.now().strftime('%d%M%Y%H%M%S') + '.jpg'
    fs.save(date, file)
    file_name = fs.url(date)

    try:
        tx_hash = contract.functions.addDigitalevidence(file_name,file_type,file_size,hash_value,collected_source,collected_time,preservation_time,caseid,).transact()
        w3.eth.wait_for_transaction_receipt(tx_hash)
        message = "EvidenceRecords " + file_name + " added successfully."
    except Exception as e:
        message = "Error: " + str(e)

    return render(request,'users/add_digitalevidence.html')

def add_documentevidence_get(request,id):
    return render(request,'users/add_documentevidence.html',{'id':id})
def add_documentevidence_post(request):
    file = request.FILES["File name"]
    document_type = request.POST["Document Type"]
    title = request.POST["Title"]
    pages = request.POST["Pages"]
    collected_from = request.POST["Collected from"]
    collected_at = request.POST["Collected at"]
    file_hash = request.POST["file hash"]
    caseid = request.POST["caseid"]

    fs = FileSystemStorage()
    date = datetime.datetime.now().strftime('%d%M%Y%H%M%S') + '.jpg'
    fs.save(date, file)
    file_name = fs.url(date)

    try:
        tx_hash = contract.functions.addDocumentevidence(file_name,document_type,title,pages,collected_from,collected_at,file_hash,caseid).transact()
        w3.eth.wait_for_transaction_receipt(tx_hash)
        message = "EvidenceRecords " + file_name + " added successfully."
    except Exception as e:
        message = "Error: " + str(e)

    return render(request,'users/add_documentevidence.html')

def add_financialaccountingevidence_get(request,id):
    return render(request,'users/add_financialaccountingevidence.html',{'id':id})
def add_financialaccountingevidence_post(request):
    file = request.FILES["File name"]
    transaction_type = request.POST["Transaction Type"]
    reference_number = request.POST["reference_number"]
    amount = request.POST["amount"]
    collected_from = request.POST["Collected from"]
    collected_at = request.POST["Collected at"]
    digital_hash = request.POST["digital hash"]
    caseid = request.POST["caseid"]

    fs = FileSystemStorage()
    date = datetime.datetime.now().strftime('%d%M%Y%H%M%S') + '.jpg'
    fs.save(date, file)
    file_name = fs.url(date)

    try:
        tx_hash = contract.functions.addFinancialaccoundingevidence(file_name,transaction_type,reference_number,amount,collected_from,collected_at,digital_hash,caseid).transact()
        w3.eth.wait_for_transaction_receipt(tx_hash)
        message = "EvidenceRecords " + file_name + " added successfully."
    except Exception as e:
        message = "Error: " + str(e)

    return render(request,'users/add_financialaccountingevidence.html')

def add_patternevidence_get(request,id):
    return render(request,'users/add_patternevidence.html',{'id':id})
def add_patternevidence_post(request):
    file = request.FILES["File name"]
    pattern_type = request.POST["Pattern Type"]
    capture_method = request.POST["capture method"]
    collected_from = request.POST["Collected from"]
    collected_at = request.POST["Collected at"]
    file_hash = request.POST["file hash"]
    caseid = request.POST["caseid"]

    fs = FileSystemStorage()
    date = datetime.datetime.now().strftime('%d%M%Y%H%M%S') + '.jpg'
    fs.save(date, file)
    file_name = fs.url(date)

    try:
        tx_hash = contract.functions.addPatternevidence(file_name,pattern_type,capture_method,collected_from,collected_at,file_hash,caseid).transact()
        w3.eth.wait_for_transaction_receipt(tx_hash)
        message = "EvidenceRecords " + file_name + " added successfully."
    except Exception as e:
        message = "Error: " + str(e)

    return render(request,'users/add_patternevidence.html')

def add_physicalevidence_get(request,id):
    return render(request,'users/add_physicalevidence.html',{'id':id})
def add_physicalevidence_post(request):
    file = request.FILES["File name"]
    evidence_type = request.POST["evidencetype"]
    description = request.POST["Description"]
    collection_location = request.POST["Collection Location"]
    collected_date = request.POST["Collected Date"]
    collected_time = request.POST["Collected Time"]
    digital_hash = request.POST["Digital Hash"]
    caseid = request.POST["caseid"]


    fs=FileSystemStorage()
    date=datetime.datetime.now().strftime('%d%M%Y%H%M%S')+'.jpg'
    fs.save(date,file)
    file_name=fs.url(date)


    try:
        tx_hash = contract.functions.addPhysicalevidence(file_name,evidence_type,description,collection_location,collected_date,collected_time,digital_hash,caseid).transact()
        w3.eth.wait_for_transaction_receipt(tx_hash)
        message = "EvidenceRecords " + file_name + " added successfully."
    except Exception as e:
        message = "Error: " + str(e)

    return render(request,'users/add_physicalevidence.html')

def add_traceevidence_get(request,id):
    return render(request,'users/add_traceevidence.html',{'id':id})
def add_traceevidence_post(request):
    file = request.FILES["File name"]
    trace_type = request.POST["Trace Type"]
    description = request.POST["Description"]
    collected_from = request.POST["Collected from"]
    collected_at = request.POST["Collected at"]
    storage_location = request.POST["storage location"]
    digital_hash = request.POST["digital hash"]
    caseid = request.POST["caseid"]

    fs = FileSystemStorage()
    date = datetime.datetime.now().strftime('%d%M%Y%H%M%S') + '.jpg'
    fs.save(date, file)
    file_name = fs.url(date)

    try:
        tx_hash = contract.functions.addTraceevidence(file_name,trace_type,description,collected_from,collected_at,storage_location,digital_hash,caseid).transact()
        w3.eth.wait_for_transaction_receipt(tx_hash)
        message = "EvidenceRecords " + file_name + " added successfully."
    except Exception as e:
        message = "Error: " + str(e)

    return render(request,'users/add_traceevidence.html')

def view_audio_evidence(request,id):
    audio_list = []

    ids = contract.functions.getAllAudioevidenceIds().call()
    for evidence_id in ids:
        file_name, media_type,duration_seconds,format,collected_from,collected_at,file_hash,caseid = contract.functions.getAudioevidence(evidence_id).call()

        if str(caseid) == str(id):

            audio_list.append({
                "id": evidence_id,
                "file_name": file_name,
                "media_type": media_type,
                "duration_seconds": duration_seconds,
                "format": format,
                "collected_from": collected_from,
                "collected_at": collected_at,
                "file_hash": file_hash
            })
    return render(request,'users/viewadd_audiovisualevidence.html', {"audioevidence": audio_list})


def view_biological_evidence(request,id):
    biological_list = []

    ids = contract.functions.getAllBiologicalevidenceIds().call()
    for evidence_id in ids:
        file_name, evidence_type,source,collection_location,collected_date,collected_time,lab_referenceid,narration,caseid = contract.functions.getBiologicalevidence(evidence_id).call()
        if str(caseid) == str(id):
            biological_list.append({


                "id": evidence_id,
                "file_name": file_name,
                "evidence_type": evidence_type,
                "source": source,
                "collection_location": collection_location,
                "collected_date": collected_date,
                "collected_time": collected_time,
                "lab_referenceid": lab_referenceid,
                "narration": narration
        })
    return render(request,'users/viewadd_biologicalevidence.html', {"biologicalevidence": biological_list})

def view_chemical_evidence(request,id):
    chemical_list = []

    ids = contract.functions.getAllChemicalevidenceIds().call()
    for evidence_id in ids:
        file_name, substance_type,quantity,collected_from,collected_at,lab_refernceid,digital_hash,caseid = contract.functions.getChemicalevidence(evidence_id).call()
        if str(caseid) == str(id):
            chemical_list.append({

            "id": evidence_id,
            "file_name": file_name,
            "substance_type": substance_type,
            "quantity": quantity,
            "collected_from": collected_from,
            "collected_at": collected_at,
            "lab_refernceid": lab_refernceid,
            "digital_hash": digital_hash

        })
    return render(request,'users/viewadd_chemicalevidence.html', {"chemicalevidence": chemical_list})


def view_digital_evidence(request,id):
    digital_list = []

    ids = contract.functions.getAllDigitalevidenceIds().call()
    for evidence_id in ids:
        file_name, file_type,file_size,hash_value,collected_source,collected_time,preservation_time,caseid = contract.functions.getDigitalevidence(evidence_id).call()
        if str(caseid) == str(id):
            digital_list.append({
            "id": evidence_id,
            "file_name": file_name,
            "file_type": file_type,
            "file_size": file_size,
            "hash_value": hash_value,
            "collected_source": collected_source,
            "collected_time": collected_time,
            "preservation_time": preservation_time,

        })
    return render(request,'users/viewadd_digitalevidence.html', {"digitalevidence": digital_list})

def view_document_evidence(request,id):
    document_list = []

    ids = contract.functions.getAllDocumentevidenceIds().call()
    for evidence_id in ids:
        file_name, document_type,title,pages,collected_from,collected_at,file_hash,caseid = contract.functions.getDocumentevidence(evidence_id).call()
        if str(caseid) == str(id):
            document_list.append({
            "id": evidence_id,
            "file_name": file_name,
            "document_type": document_type,
            "title": title,
            "pages": pages,
            "collected_from": collected_from,
            "collected_at": collected_at,
            "file_hash": file_hash,

        })
    return render(request,'users/viewadd_documentevidence.html', {"documentevidence": document_list})


def view_financial_evidence(request,id):
    financial_list = []

    ids = contract.functions.getAllFinancialaccoundingevidenceIds().call()
    for evidence_id in ids:
        file_name, transaction_type,reference_number,amount,collected_from,collected_at,digital_hash,caseid = contract.functions.getFinancialaccoundingevidence(evidence_id).call()
        if str(caseid) == str(id):
            financial_list.append({
            "id": evidence_id,
            "file_name": file_name,
            "transaction_type": transaction_type,
            "reference_number": reference_number,
            "amount": amount,
            "collected_from": collected_from,
            "collected_at": collected_at,
            "digital_hash": digital_hash

        })
    return render(request,'users/viewadd_financialaccountingevidence.html', {"Financialaccoundingevidence": financial_list})


def view_pattern_evidence(request,id):
    pattern_list = []

    ids = contract.functions.getAllPatternevidenceIds().call()
    for evidence_id in ids:
        file_name, pattern_type,capture_method,collected_from,collected_at,file_hash,caseid = contract.functions.getPatternevidence(evidence_id).call()
        if str(caseid) == str(id):
            pattern_list.append({
            "id": evidence_id,
            "file_name": file_name,
            "pattern_type": pattern_type,
            "capture_method": capture_method,
            "collected_from": collected_from,
            "collected_at": collected_at,
            "file_hash": file_hash,

        })
    return render(request,'users/viewadd_patternevidence.html', {"patternevidence": pattern_list})


def view_physical_evidence(request,id):
    physical_list = []

    ids = contract.functions.getAllPhysicalevidenceIds().call()
    for evidence_id in ids:
        file_name, evidence_type,description,collection_location,collected_date,collected_time,digital_hash,caseid = contract.functions.getPhysicalevidence(evidence_id).call()
        if str(caseid) == str(id):
            physical_list.append({
            "id": evidence_id,
            "file_name": file_name,
            "evidence_type": evidence_type,
            "description": description,
            "collection_location": collection_location,
            "collected_date": collected_date,
            "collected_time": collected_time,
            "digital_hash": digital_hash

        })
    return render(request,'users/viewadd_physicalevidence.html', {"physicalevidence": physical_list})

def view_trace_evidence(request,id):
    trace_list = []

    ids = contract.functions.getAllTraceevidenceIds().call()
    for evidence_id in ids:
        file_name, trace_type,description,collected_from,collected_at,storage_location,digital_hash,caseid = contract.functions.getTraceevidence(evidence_id).call()
        if str(caseid) == str(id):
            trace_list.append({
            "id": evidence_id,
            "file_name": file_name,
            "trace_type": trace_type,
            "description": description,
            "collected_from": collected_from,
            "collected_at": collected_at,
            "storage_location": storage_location,
            "digital_hash": digital_hash

        })
    return render(request,'users/viewadd_traceevidence.html', {"traceevidence": trace_list})











