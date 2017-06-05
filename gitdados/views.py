from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import requests

def profile(request):
    
    if request.method == 'POST':
        req = requests.get('https://api.github.com/users/{}'.format(username)).json()
        username = request.POST.get('user')
        

    return render(request, 'gitdados/profile.html', {"req":req})
