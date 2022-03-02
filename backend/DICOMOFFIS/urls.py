from django.urls import path, include
from django.shortcuts import redirect

from backend.DICOMOFFIS import views

urlpatterns =[
   path("",views.home, name =("home")),
   # path('home/' , lambda req: redirect('/')),
   path('allgemeines/', views.allgemeines, name= ('allgemeines')),
      path('allgemeines/dicom-einfuehrung', views.dicom_einfuehrung, name= ('dicom-einfuehrung')),
      path('allgemeines/standardisierung/', views.standardisierung, name=("standardisierung")),
   path('dcmtk/', views.dcmtk, name = ('dcmtk') ),
      path('dcmtk/dcmtk-einfuehrung', views.dcmtk_einfuehrung, name = ('dcmtk-einfuehrung') ),
      path('dcmtk/softwareentwicklung-mit-dcmtk', views.softwareentwicklung_mit_dcmtk, name = ('softwareentwicklung-mit-dcmtk') ),
      path('dcmtk/dcmtk-tools', views.dcmtk_tools, name = ('dcmtk-tools') ),
      path('dcmtk/spenden', views.spenden, name = ('spenden') ),
      path('dcmtk/support', views.support, name = ('support') ),
   path('dcmtk-erweiterungsmodule/', views.dcmtk_erweiterungsmodule, name=('dcmtk-erweiterungsmodule')),
      path('dcmtk-erweiterungsmodule/dcmjp2k', views.dcmjp2k, name=('dcmjp2k')),
      path('dcmtk-erweiterungsmodule/dcmppscu', views.dcmppscu, name=('dcmppscu')),
      path('dcmtk-erweiterungsmodule/dcmprint', views.dcmprint, name=('dcmprint')),
      path('dcmtk-erweiterungsmodule/dcmstcom', views.dcmstcom, name=('dcmstcom')),
      path('dcmtk-erweiterungsmodule/ppsmgr', views.ppsmgr, name=('ppsmgr')),
      path('dcmtk-erweiterungsmodule/testversionen', views.test_versionen, name=('testversionen')),
      path('dcmtk-erweiterungsmodule/dcmpps', views.dcmpps, name=('dcmpps')),
   path('dicomscope/', views.dicomscope, name = ("dicomscope")),
   path('kontakt/', views.kontakt, name = ("kontakt")),
      path('kontakt/ansprechpartner', views.ansprechpartner, name = ("ansprechpartner")),
   path('dienstleistungen/', views.dienstleistungen, name = ("dienstleistungen")),
   path('dienstleistungen/dicom-beratung', views.dicom_beratung, name = ("dicom-beratung")),
   path('dienstleistungen/dicom-schulung', views.dicom_schulung, name = ("dicom-schulung")),
   path('dienstleistungen/ihe-schulung', views.ihe_schulung, name = ("ihe-schulung")),
   path('dienstleistungen/hl7-schulung', views.hl7_schulung, name = ("hl7-schulung")),
   path('datenschutz/', views.datenschutz, name = ("datenschutz")),
   path('impressum/', views.impressum, name = ("impressum")),
]
