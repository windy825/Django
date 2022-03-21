## Django Intro 2



- **Inheritance 템플릿 상속**

  상속은 기본적으로 코드의 재사용성에 초점을 맞춤

  사이트의 모든 공통 요소를 포함하고, 하위 템플릿이 재정의 할 수 있는 블록을 정의하는

  기본 skeleton 템플릿을 만들 수 있음

- **Inheritance - tags**

  ```django
  {{% extends '' %}}
  ```

  - 자식(하위) 템플릿이 부모 템플릿을 확장한다는 것을 알림
  - 반드시 템플릿 최상단에 작성

  ```django
  {% block content %} {% endblock %}
  ```

  - 하위 템플릿에서 재지정 **overridden** 할 수 있는 블록을 정의
  - 하위 템플릿에서 채울 수 있는 공간

- **순서**

  1. app_name/templates 디렉토리 외 템플릿 추가 경로 설정

     ```django
     'DIRS': [BASE_DIR / 'templates'],
     ```

  2. bootstrap 및 간단한 navbar 작성

     ```
     {% block content %}
     {% endblock %}
     ```

     

---



- **Variable Routing**

  URL 주소를 변수로 사용하는 것

  URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음

  즉, 변수 값에 따라 하나의 path()에 여러 페이지를 연결 시킬 수 있음

  ```django
  path('accounts/user/<int:user_pk>/', ...)
  
  - acounts/user/1    
  - acounts/user/2
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



- 패키지 정보 만들기

  ```
  $ pip freeze > requirement.txt
  
  $ pip install -r requirement.txt
  ```

  