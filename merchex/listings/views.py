from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect
from listings.forms import BandForm

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html',{'bands': bands})

def band_detail(request, id):
     band = Band.objects.get(id=id)
     return render(request,'listings/band_detail.html',{'band':band})

def band_create(request):
   form = BandForm()
   return render(request,
            'listings/band_create.html',
            {'form': form})

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing_list.html',{'listings': listings})

def listing_detail(request, id):
     listing = Listing.objects.get(id=id)
     return render(request,'listings/listing_detail.html',{'listing':listing})

def about(request):
    return render(request, 'listings/about.html')

def contact(request):
      if request.method =='POST':
           form = ContactUsForm(request.POST)
           if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonymous"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['boriskf25@gmail.com'],
           )
            return redirect('contact')
      else:
           form = ContactUsForm()
      return render(request, 'listings/contact.html',{'form': form})

