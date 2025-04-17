from django.shortcuts import render
from django.http import HttpResponse
from Habibapp.models import Contact
# Create your views here.
def index(request):
    return render(request,'Habibapp/index.html')

def contact(request):
    if request.method == 'POST':
        Firstname = request.POST.get('Firstname')
        Lastname = request.POST.get('Lastname')
        Email = request.POST.get('Email')
        message = request.POST.get('message')
        en = Contact(Firstname = Firstname, Lastname = Lastname, Email = Email, message = message)
        en.save()
    return render(request,"Habibapp/contact.html")

def about(request):
    return render(request, 'Habibapp/about.html')

def blog(request):
    return render(request, 'Habibapp/blog.html')

def cart(request):
    return render(request, 'Habibapp/cart.html')

def checkout(request):
    return render(request, 'Habibapp/checkout.html')

def services(request):
    return render(request, 'Habibapp/services.html')

def shop(request):
    return render(request, 'Habibapp/shop.html')

def thankyou(request):
    return render(request, 'Habibapp/thankyou.html')
