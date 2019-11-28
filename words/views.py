from django.shortcuts import render
from .models import Words



def index(request):
    context = {
        'vocab': Words.objects.all()
    }
    return render(request, 'words/index.html', context)

def about(request):
    return render(request, 'words/about.html', {'title': 'about words'})
