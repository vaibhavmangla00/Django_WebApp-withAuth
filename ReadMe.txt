django-admin startproject <PROJECT NAME>

cd . <PROJECT NAME>
 python manage.py makemigrations
 python manage.py migrate

 python manage.py startapp home

* New Terminal *

#register your app
home.apps.HomeConfig                    in PN>settings.py

#create static and templates folder 

STATICFILES_DIRS = [
    BASE_DIR / "static",
]                                       in PN>settings.py

BASE_DIR / "templates"                in TEMPLATES DIRS 


Create urls.py in the app
path('', include('home.urls')) #from django.urls import path,include  in Hello>urls.py 


* This is URL dispatching * 
path("", views.index, name='home') # from home import views in home>urls.py  // for all funcs and htmls

def index(request):
    return render(request,'index.html')


def index(request):
    return HttpResponse('This is home page') # from django.shortcuts import render, HttpResponse in home>views.py










 class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    message = models.TextField()
    date = models.DateField()

    # in home>models.py

from home.models import Contact

admin.site.register(Contact) 

    # in home>admin.py


* 'home.apps.HomeConfig' in Installed Apps * # settings.py

    if request.method == 'post':
        name = request.post.get('name')
        email = request.post.get('email')
        phone = request.post.get('phone')
        message = request.post.get('message')
        contact = Contact(name=name, email=email, phone=phone,
                          message=message, date=datetime.today())
        contact.save()