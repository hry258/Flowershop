from django.shortcuts import render
from flower import forms
from flower.models import Flower
import time
from flower.forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def index(request):
    produs_redus = discounted_flower()
    pret_redus = int((produs_redus.pret * 4) / 5)
    return render(request, 'index.html', {'produs_redus': produs_redus, 'pret_redus': pret_redus, 'pret_intreg': produs_redus.pret})

def produse(request):
    produse_que = Flower.objects.all()
    produs_redus = discounted_flower()
    pret_redus = int((produs_redus.pret * 4) / 5)
    return render(request, 'produse.html', {'produs_redus': produs_redus, 'produse': produse_que, 'pret_redus': pret_redus})

def entry_details(request, entry_id):
    produs = Flower.objects.get(id=entry_id)
    produs_redus = discounted_flower()
    pret_redus = int((produs_redus.pret * 4) / 5)
    return render(request, "entry_details.html", {"produs": produs, 'produs_redus': produs_redus, 'pret_redus': pret_redus})

def discounted_flower():
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    today = ""
    for i in range(3):
        today += time.ctime()[i]
    for day in days:
        if today == day:
            flower_id = days.index(day) + 1
            break
    return Flower.objects.get(id=flower_id)

def contact(request):
  if request.method == 'POST':
     form = ContactForm(request.POST)
     if form.is_valid():
         mesaj = "Mesage from:" + form.cleaned_data['contact_name'] + "\nemail:" + form.cleaned_data['contact_email'] + "\n\n" + form.cleaned_data['content']
         send_mail('Contact florarie', mesaj, settings.EMAIL_HOST_USER,
                 ['popescu.catalin.ionut@gmail.com'], fail_silently=False)
     return render(request, 'contact_sent.html', {})
  else:
     return render(request, 'contact.html', {'form': ContactForm})
