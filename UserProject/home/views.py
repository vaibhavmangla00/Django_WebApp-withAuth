from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    if request.user.is_anonymous:
        print('hai bhai')
        return redirect('/login')
    return render(request, 'index.html')


def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


def logoutuser(request):
    logout(request)
    return redirect('/login')