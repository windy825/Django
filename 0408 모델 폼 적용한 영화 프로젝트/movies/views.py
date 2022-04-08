from django.shortcuts import render, redirect
from movies.forms import MovieForm
from movies.models import Movie


def index(request):
    movies = Movie.objects.order_by('pk')
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)


def detail(request, pk):
    target_movie = Movie.objects.get(pk=pk)
    context = {
        'movie': target_movie,
    }
    return render(request, 'movies/detail.html', context)


def create(request): 
    if request.method == 'POST':   # post이면 우선 양식 생성하고
        form = MovieForm(request.POST)
        if form.is_valid():     # 유효한 양식이면 저장 허락해준다
            passed_form = form.save()
            return redirect('movies:detail', passed_form.pk)   # 통과한 경우
    else:   # 아니면 빈 양식을 만들어서, 코드 계속 실행
        form = MovieForm()
    
    context = {
        'form':form,
    }
    return render(request, 'movies/create.html', context)      # 통과 못한 경우는 데이터 조작 안해주고, 다시 작성하도록 돌리기


def update(request, pk):
    now_movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=now_movie)
        if form.is_valid():
            passed_movie = form.save()
            return redirect('movies:detail', passed_movie.pk)
    else:
        form = MovieForm(instance=now_movie)
    
    context = {
        'movie':now_movie,
        'form':form,
    }
    return render(request, 'movies/update.html', context)


def delete(request, pk): # post
    target_movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        target_movie.delete()
        return redirect('movies:index')
    return redirect('movies:detail', target_movie/pk)