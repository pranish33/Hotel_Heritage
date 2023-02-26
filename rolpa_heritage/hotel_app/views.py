from django.shortcuts import render
from .models import Gallery, Clients, Rating
from django.contrib import messages

# Create your views here.

def index(request):
    images = Gallery.objects.all()
    client_images = Clients.objects.all()
    context = {
        'images': images,
        'client_images': client_images
    }
    if request.method == 'POST':
        rating_message = request.POST['rating_message']
        index = Rating(rating_message=rating_message)
        index.save()
        messages.info(request,'Thank you for your review!!')
    return render(request, 'index.html', context)
