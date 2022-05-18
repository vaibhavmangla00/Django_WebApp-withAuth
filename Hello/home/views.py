from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime
# Create your views here.
from home.models import Contact
from django.contrib import messages


def index(request):
    return render(request, 'index.html')
    # return HttpResponse('This is home page')

    # context = {
    #     'value': 5
    # }
    # return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone,
                          message=message, date=datetime.today())
        contact.save()
        messages.success(request, 'Your enquiry has been sent to admin.')
    return render(request, 'contact.html')
