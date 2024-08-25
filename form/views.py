from django.shortcuts import render
from .models import Login
from .forms import LoginForms
from .modelform import ModelForm

def form(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        Login(username=user_name, password=password).save()
    return render(request, 'form/form.html') # Render the form page for GET requests


def  Login_fun(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        Login(username=user_name, password=password).save()
    return render(request, 'form/login.html', {'lf':LoginForms})

def LoginForm(request):
     if request.method == 'POST':
        form = ModelForm(request.POST)  
        if form.is_valid():
            form.save()  
            
        return render(request, 'form/modelform.html', {'lf':ModelForm})
