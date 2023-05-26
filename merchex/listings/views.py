from django.shortcuts import render, redirect
from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm, BandForm
from django.core.mail import send_mail


def band_list(request): 
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def band_details(request, id):
    band = Band.objects.get(id=id) 
    return render(request, 'listings/bands_details.html', {'band': band})



def about(request): 
    return render(request, 'listings/about.html')


def listings(request): 
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html', {'listings': listings} )


def contact(request):
    if(request.method == 'POST'):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonym"} via MerchEx Contact Us form',
                message = form.cleaned_data["message"],
                from_email = form.cleaned_data["email"],
                recipient_list = ['admin@merchex.xyz']
            )
            return redirect('email')
    else:
        form = ContactUsForm()
    return render(request, 'listings/contact.html', {'form': form})


def email_sent(request):
    return render(request, 'listings/email_sent.html', )

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            #creer une nouvelle band et la sauvegarder dans la base de donnee
            band = form.save()
            return redirect('band-  detail', band.id)

    else: 
        form = BandForm()

    return render(request, 'listings/band_create.html', {'form': form})


def band_update(request, id):
    band = Band.objects.get(id=id)
    form = BandForm(instance=band) # on pre remplir le formulaire avec un groupe existant
    return render(request, 'listings/band_update.html', {'form': form})


def band_delete(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        band.delete()
        return redirect('band-list')
    return render(request, 'listings/band_delete.html', {'band': band})