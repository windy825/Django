from django.shortcuts import render, redirect
from .models import Movie



def index(request):
    movie_list = Movie.objects.order_by('pk')
    content = {
        'movie_list': movie_list,
    }
    return render(request, 'movies/index.html',content)


def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    content = {
        'movie':movie,
    }
    return render(request, 'movies/detail.html',content)

def new(request):
    return render(request, 'movies/new.html')

def create(request):
    new = Movie()
    new.title = request.POST.get('title')
    new.audience = request.POST.get('audience')
    new.release_date = request.POST.get('trip-start')
    new.genere = request.POST.get('genere')
    new.score = request.POST.get('score')
    new.poster = request.POST.get('poster')
    new.description = request.POST.get('description')
    new.save()

    return redirect('movies:detail', new.pk)

def delete(request, pk):
    target = Movie.objects.get(pk=pk)

    if request.method == 'POST':
        target.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', target.pk)

def edit(request, pk):
    movie = Movie.objects.get(pk=pk)
    content = {
        'movie':movie,
    }
    return render(request, 'movies/edit.html', content)

def update(request, pk):
    change = Movie.objects.get(pk=pk)
    change.title = request.POST.get('title')
    change.audience = request.POST.get('audience')
    change.release_date = request.POST.get('trip-start')
    change.genere = request.POST.get('genere')
    change.score = request.POST.get('score')
    change.poster = request.POST.get('poster')
    change.description = request.POST.get('description')

    return redirect('movies:detail', change.pk)