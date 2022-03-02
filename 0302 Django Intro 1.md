## Django Intro





- **Static web page (정적 웹 페이지)**

  서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹 페이지

  서버가 정적 웹 페이지에 대한 요청을 받은 경우

  서버는 추가적인 처리 과정 없이 클라이언트에게 응답을 보냄

  모든 상황에서 모든 사용자에게 동일한 정보를 표시

  일반적으로 HTML, CSS, JavaScript 로 작성됨

  flat page 라고도 함

​                



- **Dynamic web page (동적 웹 페이지)**

  웹 페이지에 대한 요청을 받은 경우 서버는 추가적인 처리 과정 이후

  클라이언트에게 응답을 보냄

  동적 웹 페이지는 방문자와 상호작용하기 때문에 페이지 내용은 그때그때 다름

  서버 사이드 프로그래밍 언어 (python, java, c++ 등) 가 사용되며, 

  파일을 처리하고 데이터베이스와의 상호작용이 이루어짐

​           

​      

- **Framework (Application framwork)**

  프로그래밍에서 특정 운영체제를 위한 응용 프로그램 표준 구조를 구현하는

  클래스와 라이브러리 모임

  재사용할 수 있는 수많은 코드를 프레임워크로 통합함으로써

  개발자가 새로운 애플리케이션을 위한 표준 코드를 다시 작성하지 않아도 

  같이 사용할 수 있도록 도움

​               



- **web framework**

  웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것이 주 목적으로

  데이터베이스 연동, 템플릿 형태의 표준, 세션 관리, 코드 재사용 등의 기능을 포함

  동적인 웹 페이지나, 웹 애플리케이션, 웹 서비스 개발 보조용으로

  만들어지는 Application framework의 일종

​                



---

​            

​    

- **Framework Architecture**

  **MVC 디자인 패턴 (model - view - controller)**

  소프트웨어 공학에서 사용되는 디자인 패턴 중 하나

  사용자 인터페이스로부터 프로그램 로직을 분리하여

  애플리케이션의 시각적 요소나 이면에서 실행되는 부분을 

  서로 영향 없이 쉽게 고칠 수 있는 애플리케이션을 만들 수 있음

  ​              

  

  - Django : **MTV 패턴**이라고 함 (model - template - view)

    **Model**

    - 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리 (추가, 수정, 삭제)

    **Template**

    - 파일의 구조나 레이아웃을 정의
    - 실제 내용을 보여주는 데 사용 (presentation)

    **View**

    - HTTP 요청을 수신하고 HTTP응답을 반환
    - model을 통해 요청을 충족시키는데 필요한 데이터에 접근
    - template에게 응답의 서식 설정을 맡김

    ![제목 없음](https://user-images.githubusercontent.com/89068148/156374002-d3b940ab-1b20-4924-b638-2dcef9e34fda.png)

    ![제목 없음](https://user-images.githubusercontent.com/89068148/156375401-3b27f70b-7b7f-4011-a5e8-356ee26c3e4f.png)





---

​             

​            

- **가상환경 생성 및 활성화** 

  ```python
  $ python -m venv 이름
  
  $ source venv/Scripts/activate
  
  $ deactivate
  ```

​    



- **Django 코드 작성 순서 중요**

  ```python
  $ pip install django==3.2.12
  
  $ django-admin startproject 이름 .
  
  $ python manage.py startapp articles   # 일반적으로 Application명은 복수형 권장
  
  setting.py에서 출생신고
  INSTALLED_APPS = ['articles',]         
  # Django installation에 활성화 된 모든 앱을 지정하는 문자열 목록
  # 반드시 생성 후 등록해야 함, 반대로 할 경우 앱 생성 불가
  
  urls.py
  
  views.py
  
  articles/templates/목표html
  
  $ python manage.py runserver
  ```

  LTS(장기 지원 버전) 버전 확인 필요 

  일반적인 경우보다 장기간에 걸쳐 지원하도록 고안된 소프트웨어의 버전

  컴퓨터 소프트웨어의 제품 수명주기 관리 정책

  배포자는 LTS 확정을 통해 장기적이고 안정적인 지원을 보장함





- **프로젝트 구조**

  > **> firstpjt**
  >
  > >**__init__.py**
  > >
  > >```
  > >파이썬에게 이 디렉토리를 하나의 파이썬 패키지로 다루도록 지시
  > >```
  > >
  > >**asgi.py**
  > >
  > >```
  > >Asynchronous Server Gateway Interface
  > >Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움
  > >```
  > >
  > >**settings.py**
  > >
  > >```
  > >애플리케이션의 모든 설정을 포함
  > >```
  > >
  > >**urls.py**
  > >
  > >```
  > >사이트의 url과 적절한 views의 연결을 지정 
  > >HTTP request를 알맞은 view로 전달
  > >```
  > >
  > >**wsgi.py**
  > >
  > >```
  > >Web Server Gateway Interface
  > >Django 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움
  > >```
  >
  > **manage.py**
  >
  > ```
  > Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티
  > 
  > # manage.py Usage
  > $ python manage.py <command> [options]
  > ```

​                                   

- **Application 구조**

  **> articles**

  > **> migrations**
  >
  > **> templates**
  >
  > ```
  > : 데이터 표현을 제어하는 도구이자 표현에 관련된 로직
  > 
  > built-in system 인 django template language 를 사용함
  > 실제 내용을 보여주는데 사용되는 파일
  > 파일의 구조나 레이아웃을 정의 (html 등)
  > template 파일 경로의 기본 값은 app 폴더 안의 templates 폴더로 지정되어 있음
  > ```
  >
  > **__init__.py**
  >
  > **admin.py**
  >
  > ```
  > 관리자용 페이지를 설정하는 곳
  > ```
  >
  > **apps.py**
  >
  > ```
  > 앱의 정보가 작성된 곳
  > ```
  >
  > **models.py**
  >
  > ```
  > 앱에서 사용하는 Model을 정의하는 곳
  > ```
  >
  > **test.py**
  >
  > ```
  > 프로젝트의 테스트 코드를 작성하는 곳
  > ```
  >
  > **views.py**
  >
  > ```
  > view 함수들의 정의 되는 곳
  > HTTP 요청을 수신하고 응답을 반환하는 함수 작성
  > model을 통해 요청에 맞는 필요 데이터에 접급
  > template에게 HTTP 응답 서식을 맡김
  > ```





- **DTL (django template language)**

  조건, 반복, 변수 치환, 필터 등의 기능 제공
  프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것
  파이썬 코드로 실행되는 것이 아님 (비슷한 구조를 사용할 순 있음)

  

  - **Variable**  

    `{{ variable }}`

    `render()` 를 사용하여 views.py에서 정의한 변수를 template 파일로 넘겨 사용하는 것

    변수명은 영어, 숫자와 언더바 조합 가능하지만 , 밑줄로 시작할 수 없음(공백이나, 구두점 문자도 불가)

    dot`.` 을 통해 변수 속성에 접근 가능

    `render()` 의 세번째 인자로 `{'key' : value}` 와 같이 딕셔너리 형태로 넘겨주며, 

    여기서 정의한 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨

  - **Filters**  

    `{{ variable | filter }}`

    표시할 변수를 수정할 때 사용

    60개의 built-in template filters 를 제공

    ```django
    {{ name|lower }}   {#name 변수를 소문자로 출력#}
    
    {{ variable|truncatewords:30 }} {# chained가 가능하며 일부 필터는 인자를 받기도 함 #}
    ```

  - **Tags**

    `{% tag %}`

    출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일 수행

    일부 태그는 시작과 종료 태그가 필요

    약 24개의 built-in template tags 를 제공

    ```django
    {% if %}{% eldif %}
    ```

  - **Comments**

    `{#  #}`

    Django template에서 라인의 주석을 표현하기 위해 사용

    ```django
    {# 한줄짜리 주석 #}
    
    {% comment %}
    여러줄
    짜리 
    주석
    {% endcomment %}
    ```

    

  ```
  ctrl + l : 창 클리어
  ctrl + c : 가상환경 종료
  ```





- 코드 작성 순서
  - URL (언더바 권장 안함 - 하이픈 쓰자)
  - VIEW (언더바 권장)
  - TEMPLATE





- 상속 중요





- BASE_DIR

python object oriented filesystem path

운영체제가 다르기 때문에 경로시스템을 공통적으로 맞춰주기 위해서

파이썬의 객체지향적인 파일 시스템

경로를 하드코딩해놓으면 다른 운영체제 (특히 /개념이 다른 체제)

는 경로 불가