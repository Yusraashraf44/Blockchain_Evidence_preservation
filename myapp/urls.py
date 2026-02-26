"""
URL configuration for evidence_preservation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('login_get/',views.login_get),
    path('login_post/',views.login_post),
    path('logout_get/',views.logout_get),
    path('viewcomplaint_get/', views.viewcomplaint_get),
    path('viewevidence_get/', views.viewevidence_get),
    path('viewuser_get/', views.viewuser_get),
    path('changepassword_get/', views.changepassword_get),
    path('changepassword_post/', views.changepassword_post),
    path('sentreply_get/', views.sentreply_get),
    path('sentreply_post/', views.sentreply_post),
    path('adminhome_get/', views.adminhome_get),
    path('assigncase_get/', views.assigncase_get),
    path('assigncase_post/', views.assigncase_post),
    path('viewassignedcase_post/', views.viewassignedcase_post),
    path('editassigncase_get/<id>', views.editassigncase_get),
    path('editassigncase_post/', views.editassigncase_post),
    path('deleteassignedcase_get/<id>', views.deleteassignedcase_get),
    # USERS---
    # path('viewassigncase_get/',views.viewassigncase_get),
    path('viewassigncase_post/',views.viewassigncase_post),
    path('userindex_get/',views.userindex_get),
    path('edit_get/', views.edit_get),
    path('edit_post/', views.edit_post),
    path('forgotpassword_get/', views.forgotpassword_get),
    path('forgotpassword_post/', views.forgotpassword_post),
    path('register_get/', views.register_get),
    path('register_post/', views.register_post),
    path('sentcomplaint_get/', views.sentcomplaint_get),
    path('sentcomplaint_post/', views.sentcomplaint_post),
    path('user_viewcomplaint_get/', views.user_viewcomplaint_get),
    path('viewprofile_get/', views.viewprofile_get),
    path('add_audiovisualevidence_get/<id>',views.add_audiovisualevidence_get),
    path('add_audiovisualevidence_post/',views.add_audiovisualevidence_post),
    path('add_biologicalevidence_get/<id>',views.add_biologicalevidence_get),
    path('add_biologicalevidence_post/',views.add_biologicalevidence_post),
    path('add_chemicalevidence_get/<id>',views.add_chemicalevidence_get),
    path('add_chemicalevidence_post/',views.add_chemicalevidence_post),
    path('add_digitalevidence_get/<id>',views.add_digitalevidence_get),
    path('add_digitalevidence_post/',views.add_digitalevidence_post),
    path('add_documentevidence_get/<id>',views.add_documentevidence_get),
    path('add_documentevidence_post/',views.add_documentevidence_post),
    path('add_financialaccountingevidence_get/<id>',views.add_financialaccountingevidence_get),
    path('add_financialaccountingevidence_post/',views.add_financialaccountingevidence_post),
    path('add_patternevidence_get/<id>',views.add_patternevidence_get),
    path('add_patternevidence_post/',views.add_patternevidence_post),
    path('add_physicalevidence_get/<id>',views.add_physicalevidence_get),
    path('add_physicalevidence_post/',views.add_physicalevidence_post),
    path('add_traceevidence_get/<id>',views.add_traceevidence_get),
    path('add_traceevidence_post/',views.add_traceevidence_post),


    path('view_audio_evidence/<id>',views.view_audio_evidence),
    path('view_biological_evidence/<id>',views.view_biological_evidence),
    path('view_chemical_evidence/<id>',views.view_chemical_evidence),
    path('view_digital_evidence/<id>',views.view_digital_evidence),
    path('view_document_evidence/<id>',views.view_document_evidence),
    path('view_financial_evidence/<id>',views.view_financial_evidence),
    path('view_pattern_evidence/<id>',views.view_pattern_evidence),
    path('view_physical_evidence/<id>',views.view_physical_evidence),
    path('view_trace_evidence/<id>',views.view_trace_evidence),


    path('addstaff_get/',views.addstaff_get),
    path('addstaff_post/',views.addstaff_post),
    path('editstaff_get/<id>',views.editstaff_get),
    path('editstaff_post/',views.editstaff_post),
    path('deletestaff_get/<id>',views.deletestaff_get),
    path('addcase_get/',views.addcase_get),
    path('addcase_post/',views.addcase_post),
    path('viewcase_get/',views.viewcase_get),
    path('editcase_get/<id>',views.editcase_get),
    path('editcase_post/',views.editcase_post),
    path('deletecase_get/<id>',views.deletecase_get),






]
