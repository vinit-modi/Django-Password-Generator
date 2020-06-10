from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    char = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        char.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if request.GET.get('numbers'):
        char.extend('0123456789')

    if request.GET.get('special'):
        char.extend('!@#$%^&*()')

    length = int(request.GET.get('length'))

    gen_password = ''
    for i in range(length):
        gen_password += random.choice(char)

    return render(request, 'generator/password.html', {'password':gen_password})