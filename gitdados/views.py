from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib.auth.decorators import login_required
#from django.utils import timezone
import requests
# Form import
from .forms import GitDadosForm, MeuCepForm

def mycep(request):
    template_name = 'gitdados/mycep.html'
    context = {}

    if request.method = "POST":
        form = MeuCepForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            


    return render(request, template_name, context)

def marketing(request):
    template_name = 'gitdados/marketing.html'
    context = {}
    return render(request, template_name, context)

def profile(request):
    template_name = 'gitdados/profile.html'
    context = {}

    if request.method == 'POST':
        username = request.POST.get('user')
        req = requests.get('https://api.github.com/users/{}'.format(username)).json()
        context['req']=req

    return render(request, template_name, context)


def index(request):
    template_name = 'gitdados/index.html'
    context = {}

    return render(request, template_name, context)
