from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib.auth.decorators import login_required
#from django.utils import timezone
import requests
# Form import
from .forms import GitDadosForm



def profile(request):
    template_name = 'gitdados/profile.html'
    context = {}
    
    if request.method == 'POST':
        username = request.POST.get('user') 
        req = requests.get('https://api.github.com/users/{}'.format(username)).json()
        context['req']=req

    return render(request, template_name, context)


def teste(request):
    template_name = 'gitdados/teste.html'
    context = {}
    

    if request.method == 'POST':
        form = form(data=request.POST)

        if form.is_valid():
            git_name = request.POST.get('git_name')            
            context['git_name']=git_name          
          

        return redirect('teste')    

    else:
        form = GitDadosForm()


        context['form']=form
  


    return render(request, template_name, context)


