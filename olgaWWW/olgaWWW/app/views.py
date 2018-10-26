from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from .models import Articles,Price,Myaddress
from .forms import ContactForm
from django.contrib import messages
from .functions import json

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    aboutUs = Articles.objects.getAboutUs()
    cosmetics = Articles.objects.getCosmetics()
    cosmeticTreatment = Articles.objects.getCosmeticTreatment()

    return render(
        request,
        'home/index.html',
        {
            'title' : 'Strona domowa',
            'year' : datetime.now().year,
            'aboutUs' :  aboutUs[0].content,
            'cosmetics' : cosmetics[0].content,
            'cosmeticTreatment' : cosmeticTreatment[0].content
        }
    )

def offer(request):
    """Renders the offer page """
    assert isinstance(request, HttpRequest)
    offer = Articles.objects.getOffer()
    return render(
        request,
        'offer/offer.html',
        {
            'title' : 'Offer',
            'year'  : datetime.now().year,
            'offer' : offer[0].content
        }


    )

def pricing(request):
    """Renders the price page """
    assert isinstance(request, HttpRequest)
    pricing = Price.objects.all()
    return render(
        request,
        'pricing/pricing.html',
        {
            'title' : 'Cennik',
            'year'  : datetime.now().year,
            'pricing' : pricing
        }
    )

def contact(request):
    """Renders the contact page """
    assert isinstance(request, HttpRequest)
    actualYearOfCopyright = datetime.now().year
    address = Myaddress.objects.filter(pk=1)
    # this below only for text
    if request.method == "GET":
        return render(
            request, 'contact/contact.html',
            {
                'title' : 'Kontakt',
                'year' : actualYearOfCopyright,
                'contact' : ContactForm,
                'showForm' : True,
                'address' : address[0]
            }
        )
    elif request.method == "POST":
        #form = ContactForm(request.POST)
        form = ContactForm(data=request.POST)

        if form.is_valid():
            save=form.save(commit=False)
            # additional field
            # save.author = request.user
            save.save()
            messages.success(request, 'Wiadomość została wysłana!')
            return render(
                request,
                'contact/contact.html',
                {
                    'title' : 'Kontakt',
                    'year' : actualYearOfCopyright,
                    'contact' : None,
                    'showForm' : False,
                    'address' : address[0]
                })
        else:

            error = json(form.errors.as_json())
            messages.error(request,error.getMessageFormCleanValidation())
            return render(
                request, 'contact/contact.html',
                {
                    'title' : 'Kontakt',
                    'year' : actualYearOfCopyright,
                    'contact' : ContactForm,
                    'showForm' : True,
                    'address' : address[0]
                }
            )

    else:
        messages.error(request, 'Niepodziewany bląd, wyślij maila do db@ap.pl!')
        return render(
            request, 'contact/contact.html',
            {
                'title' : 'Kontakt',
                'year' : actualYearOfCopyright,
                'contact' : None,
                'showForm' : False,
                'address' : address[0]
            }
        )

def online(request):
    """Renders the register online page """
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'registrationOnLine/online.html',
        {
            'title' : 'Rejestracja online',
            'year'  : datetime.now().year,
            'online' : ""
        }


    )