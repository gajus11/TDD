from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def persona_login(request):
    authenticate(assertion=request.POST['assertion'])
    return HttpResponse()