### Model 반영하기

- Migrations

  ```
  makemigrations : 모델을 변경한 것에 기반하여 새 설계도(마이그레이션)을 생성
  migrate : 설계도(migtation)을 DB에 반영하기 위해 사용
  sqlmigrate : 마이그레이션에 대한 SQL 구문을 보기 위해 사용
  ```

   



### Model 변경사항 저장하기

- 모델 변경사항을 DB와 동기화하는 작업

  ```bash
  $ python manage.py migrate
  ```

  

- 마이그레이션에 대한 SQL 구문을 확인(동작 방식 미리보기)

  ```sql
  $ python manage.py sqlmigrate articles 0001   앱이름 과 생성된 설계도 번호
  
  >>>
  BEGIN;
  --
  -- Create model Article
  --
  CREATE TABLE "articles_article"                      # 생성된 스키마
  ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,    # 레코드의 고유값인 기본키 "id"
  "title" varchar(10) NOT NULL,                        # 속성들의 공간 및 정보 표시
  "content" text NOT NULL);
  
  COMMIT;
  ```

  



### Python Shell

- 장고에서 사용가능한 다양한 라이브러리와 그 안의 모듈들을 사용하기 위한 방법

  ```bash
  $ pip install ipython
  $ pip install django-extensions          # 기존 셸보다 추가기능을 사용하기 위한 설치
                                           # 라이브러리 등록하기 (setting.py의 앱목록에 추가)
  
  $ python manage.py shell_plus            # 라이브러리 등록 및 실행
  ```

  





### Django Model Field

- 다양한 형태를 지원하는 것 같다...

  ```
  Primary key : AutoField, BigAutoFild
  문자열 : CharField, TextField
  날짜 시간 : DataField, TimeField, DateTimeField
  참 거짓 : BooleanField, NullBooleanField
  숫자 : IntegerField....등등
  파일 : BinaryField, FileField, ImageField
  이메일 : EmailField
  URL : URLField
  아이피 : GenericIPAdrdressField
  ```



---