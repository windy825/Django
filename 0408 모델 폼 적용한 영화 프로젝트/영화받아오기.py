# api 사이트에서 추천영화 정보들을 받아오는 작업

import requests
import json

def get_genre(target_id):
    url = 'https://api.themoviedb.org/3/genre/movie/list?api_key=95df29b4b9da9e2aca14c18f410253ee&language=ko-KR'
    data = requests.get(url).json()['genres']
    what = []

    for num in target_id:
        for genre in data:
            if genre['id'] == num:
                what.append(genre['name'])

    return what


def get_movies_info():
    answer = []

    for i in range(1, 10):
        url = f"https://api.themoviedb.org/3/movie/popular?api_key=95df29b4b9da9e2aca14c18f410253ee&language=ko-KR&page={i}"
        movies = requests.get(url).json()

        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    'title' : movie['title'],
                    'audience' : movie['popularity']* 8560,
                    'release_date' : movie['release_date'],
                    'genre' : get_genre(movie['genre_ids']),
                    'score' : movie['vote_average'],
                    'poster_url' : f"https://image.tmdb.org/t/p/w500{movie['poster_path']}",
                    'description' : movie['overview'],
                }
                data = {
                    'pk' : movie['id'],
                    'model' : 'movies.movie',
                    'fields' : fields,
                }
                answer.append(data)
    
    with open('movie_data.json', 'w', encoding='utf-8') as w:
        json.dump(answer, w, indent='\t', ensure_ascii=False)


get_movies_info() # json 파일 생성