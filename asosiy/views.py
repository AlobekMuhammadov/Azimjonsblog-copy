from django.shortcuts import render,redirect
from .models import *

def home(request):
    return render(request,'home.html')

def blog(request):
    content = {
        "maqolalar": Maqola.objects.all()
    }
    return render(request, 'blog.html', content)

def bitta_blog(request,son):
    content = {
        'maqola': Maqola.objects.get(id=son)
    }
    return render(request, 'maqola.html', content)

def about(request):
    return render(request, 'about.html')

def maqola(request):
    return render(request, 'maqola.html')

