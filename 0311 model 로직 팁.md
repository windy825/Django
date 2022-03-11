## Django Model

<br>

### 1 **models.py** 를 작성한 후 마이그레이션 작업을 위해 터미널에 작성해야 하는 핵심 명령어

```bash
$ python manage.py makemigrations    작성한 model.py를 기반으로 설계도 생성
$ python manage.py migrate           설계도 추가(동기화)
```

<br>

### 2 새 Post 를 저장하는 코드

```python
# 3번
post = Post(title='제목', content='내용')   # 옳바른 위치에 저장하고 싶다면, 키워드인자를 사용
post.save()
```

<br>

### 3 첫번째 Post 가져오는 코드

```python
post1 = Post.objects.all()[0]
post1 = Post.objects.all()[-10] # 지원안함
post1 = Post.objects.first()  
post1 = Post.objects.all().get(id=1)
```

<br>

### 4 my_post 변수에 Post객체 하나가 저장되 있을때 title과content를 수정하기

```python
new = my_post()
new.title = '안녕하세요'
new.content = '반갑습니다'


new_article = my_post.first()
new_article.title = new.title
new_article.content = new.content
new.save()
```

<br>

### 5 만들어진 모든 Post 객체를 쿼리셋 형태로 반환하기

```python
posts = Post.objects.all()
```

