from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from .forms import AccountForm
from .models import Account
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
# Create your views here.

class AccountForm(forms.ModelForm):
    class Meta:
        model=Account
        fields="__all__"

class loginForm(forms.Form):
    username = forms.CharField(label="Username:")
    password = forms.CharField(label="Password:")


def login(request):
    if request.method== "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("mainpage"))
    return render(request, "theApp/login.html", { "form": loginForm})

            

def register(request):
    return render(request, "theApp/register.html", { "form": AccountForm})


def mainpage(request, user):
    return HttpResponse("Suck it nigga")