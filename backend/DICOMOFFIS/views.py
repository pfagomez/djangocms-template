from django.shortcuts import render
from django.template import loader
from .models import eintrag

# create your views here.
def home (request):
    letzer_eintrag = eintrag.objects.order_by('datum')
    loader.get_template('website/home.html')
    context = {
        'latest_question_list': letzer_eintrag,
    }
    return render (request,'website/home.html',context)

def allgemeines (request):
    return render (request,'website/allgemeines/allgemeines.html')

def dcmtk (request):
    return render (request, 'website/dcmtk/dcmtk.html')

def home (request):
    return render (request, 'website/home.html')

def dcmtk_erweiterungsmodule (request):
    return render (request, 'website/dcmtk-erweiterungsmodule/dcmtk-erweiterungsmodule.html')

def dicomscope (request):
    return render(request, 'website/dicomscope.html')

def kontakt (request):
    return render(request, 'website/kontakt/kontakt.html')

def ansprechpartner (request):
    return render(request, 'website/kontakt/ansprechpartner.html')

def dienstleistungen (request):
    return render(request, 'website/dienstleistungen/dienstleistungen.html')

def datenschutz (request):
    return render(request, 'website/datenschutz.html')

def impressum (request):
    return render(request, 'website/impressum.html')

def offis (request):
    return render(request, 'https://www.offis.de')

def standardisierung (request):
    return render(request, 'website/allgemeines/standardisierung.html')

def dicom_einfuehrung (request):
    return render(request, 'website/allgemeines/dicom-einfuehrung.html')

def dcmtk_einfuehrung (request):
    return render (request, 'website/dcmtk/dcmtk-einführung.html')

def dcmtk_tools (request):
    return render (request, 'website/dcmtk/dcmtk-tools.html')

def softwareentwicklung_mit_dcmtk (request):
    return render (request, 'website/dcmtk/softwareentwicklung-mit-dcmtk.html')

def spenden (request):
    return render (request, 'website/dcmtk/spenden.html')

def support (request):
    return render (request, 'website/dcmtk/support.html')

def dcmjp2k (request):
    return render (request, 'website/dcmtk-erweiterungsmodule/dcmjp2k.html')

def dcmppscu (request):
    return render (request, 'website/dcmtk-erweiterungsmodule/dcmppscu.html')

def dcmprint (request):
    return render (request, 'website/dcmtk-erweiterungsmodule/dcmprint.html')

def ppsmgr (request):
    return render (request, 'website/dcmtk-erweiterungsmodule/ppsmgr.html')

def test_versionen (request):
    return render (request, 'website/dcmtk-erweiterungsmodule/testversionen.html')

def dcmpps (request):
    return render (request, 'website/dcmtk-erweiterungsmodule/dcmpps.html')

def dcmstcom (request):
    return render (request, 'website/dcmtk-erweiterungsmodule/dcmstcom.html')

def dicom_beratung (request):
    return render(request, 'website/dienstleistungen/dicom-beratung.html')

def dicom_schulung (request):
    return render(request, 'website/dienstleistungen/dicom-schulung.html')

def hl7_schulung (request):
    return render(request, 'website/dienstleistungen/hl7-schulung.html')

def ihe_schulung (request):
    return render(request, 'website/dienstleistungen/ihe-schulung.html')