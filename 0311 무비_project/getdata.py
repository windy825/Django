import requests
import json


def get_genre(genre_ids):
    url = f'https://api.themoviedb.org/3/genre/movie/list?api_key=95df29b4b9da9e2aca14c18f410253ee&language=ko-KR'
    data = requests.get(url).json()['genres']
    answer = []

    for number in genre_ids:
        for genre in data:
            if genre['id'] == number:
                answer.append(genre['name'])

    return answer


def get_movie_data():
    total_data = []

    for i in range(1,10):
        url = f"https://api.themoviedb.org/3/movie/popular?api_key=95df29b4b9da9e2aca14c18f410253ee&language=ko-KR&page={i}"
        
        movies = requests.get(url).json()

        for movie in movies['results']:

            if movie.get('release_date', ''):
                fields = {
                    'title' : movie['title'],
                    'audience' : movie['popularity']* 8560,
                    'release_date' : movie['release_date'],
                    'genere' : get_genre(movie['genre_ids']),
                    'score' : movie['vote_average'],
                    'poster_url' : f"https://image.tmdb.org/t/p/w500{movie['poster_path']}",
                    'description' : movie['overview'],
                }
                data = {
                    'pk' : movie['id'],
                    'model' : 'movies.movie',
                    'fields' : fields
                }
                total_data.append(data)    

    with open("movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\t", ensure_ascii=False)


get_movie_data()

# python manage.py loaddata movi_data.json
