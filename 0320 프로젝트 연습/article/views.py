from django.shortcuts import render
from .models import Article

# Create your views here.

def index(request):
    return render(request, 'index.html')

def greeting(request):
    foods = ['apple', 'banana', 'coconut']
    info = {
        'name':'Alice'
    }
    context = {
        'foods':foods,
        'info':info,
    }
    return render(request, 'greeting.html', context)


def throw(request):
    return render(request, 'throw.html')


def catch(request):
    content = {
        'throw_thing':request.GET.get('ms11')
    }
    return render(request, 'catch.html', content)

def hello(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article
    }
    return render(request, 'hello.html', context)