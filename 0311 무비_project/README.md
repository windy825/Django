## 관통 프로젝트 05 crud

<br>

<br>

### 1. 데이터 준비하기

TMDB API를 이용하여 추천영화들을 받아왔습니다. 하지만 기존의 json 파일은 인식이 되지 않아, 장고에 맞도록 indentation을

수정하는 작업을 진행했습니다.

아래 코드를 기반으로 json 파일을 생성 후 , loaddata를 통해 제 서버에 데이터를 업로드 하였습니다.

```python
import requests
import json


def get_genre(genre_ids):           # 장르 아이디를 기반으로 각 영화의 장르를 획득
    url = f'https://api.themoviedb.org/3/genre/movie/list?api_key=95df29b4b9da9e2aca14c18f410253ee&language=ko-KR'
    data = requests.get(url).json()['genres']
    answer = []

    for number in genre_ids:
        for genre in data:
            if genre['id'] == number:
                answer.append(genre['name'])
    return answer


def get_movie_data():               # TMDB API를 이용하여 추천영화목록 받아오기
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
    with open("movie_data.json", "w", encoding="utf-8") as w:       # 데이터를 장고가 받을 수 있도록
        json.dump(total_data, w, indent="\t", ensure_ascii=False)   # 장고에 맞는 json 형식으로 변환하여 저장


get_movie_data()   # TMDB API에서 데이터 받아오기 실행
```

```bash
$ python manage.py loaddata movi_data.json    # 서버에 업로드
```

<br>

- 서버 DB에 잘 올라갔는지 확인하기 입니다. (사실 잘 돼서 자랑하려고 올렸습니다 죄송합니다! )

![db](https://user-images.githubusercontent.com/89068148/157884749-a40f0076-5c6a-40f9-960c-b46a848a9b1e.png)

---

<br>

<br>

### 2. index 페이지 만들기

부트스트랩... 처음으로 평가에 있어 낮은 점수를 안겨준 과목인 웹 입니다.

하지만 어느 때처럼 피하지 않았습니다. 계속 보다보니 그렇게 밉던 웹도 귀엽고 친숙해졌습니다.

역시 익숙함의 차이였던 것일까요....

관통프로젝트 특히 웹 파트를 지금까지 해오면서 안된다고 힘들어하고 나 자신을 원망 했었지만, 

그럴수록 더 바닥을 내려갈려고 하는 기분때문에 한번 힘차게 태세 전환 해봤습니다.

징징 거린다고 사회에서 누가 대신 일해줄것도 아니니까요!

<br>

- 엉성한 웹 디자인 이지만, 저에겐 정말 장족의 발전이랍니다... 무려 그리드 시스템을 도입 및 다룰 수 있어요!

  ![index](https://user-images.githubusercontent.com/89068148/157880604-6fbc6051-b85f-4f7e-85a7-40afe41cce5c.png)

  <br>

  **DETAIL 상세 페이지**

  ![디테일](https://user-images.githubusercontent.com/89068148/157882644-098e570f-e7f6-4a85-aec4-686044972e92.png)

---

<br>

<br>

### 3. NEW 새로운 게시글 작성하기

- new 버튼을 통해 새로운 영화게시글을 작성하여 서버에 저장할 수 있습니다.!

![new](https://user-images.githubusercontent.com/89068148/157880998-abbdfea9-f7bf-4acb-bdf1-be1077526da1.png)

 <br> <br>       

- 작성을 완료 한 후 제출을 누르면, 아래와 같이 새로운 게시글이 생성되고, 해당 게시글의 detail 화면이 띄워진다.

![new생성후](https://user-images.githubusercontent.com/89068148/157881002-cb87b3ef-6221-4561-8de6-bcd442d95600.png)

- 삭제를 누르면 게시글이 삭제되고, 다시 index 화면으로 돌아가게 됩니다.

---

<br>

<br>

### EDIT 게시글 수정하기

아무 영화에서 상세보기 페이지(detail) 에 들어갑니다. 그리고 수정 버튼을 누르면 아래와 같이 화면이 띄워집니다.

![수정하기](https://user-images.githubusercontent.com/89068148/157882474-bd9a3460-16d1-4bdc-891d-50ba1335639c.png)

<br>

<br>

<br>

---

## 결론

- 역시나!! 웹과 장고가 힘들게 느껴졌던 건, 기존에 파이썬 언어 다루듯이 익숙한 상태가 아니었습니다.

  좌절만 하고 짜증만 부리기 보단, 그 1분1초 시간에 공부를 하고 열심히 배우면 

  익숙하게 다룰 수 있음을 느꼈습니다.

  관통프로젝트를 거치면서 저는 성장했습니다.

  약간 태도를 바꾸게 된 계기가 딱 이번 프로젝트 였습니다.

  제 자신이 대견하기도 하고, 앞으로도 새로운 언어나, 기술을 배울때 좀더 긍정적으로 뛰어 들 수 있는 자신감을

  얻었습니다!!

  감사합니다!!
