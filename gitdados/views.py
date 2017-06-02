from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import requests

def profile(request):
    req = requests.get('https://api.github.com/users/makoreactor').json()
    return render(request, 'gitdados/profile.html', {"req":req})
