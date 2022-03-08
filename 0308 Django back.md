모델

- 단일한 데이터에 대한 정보 저장
  - 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함
- 저장된 데이터베이스의 구조
- django는 model을 통해 데이터 접속 관리



데이터 베이스

- 체계화된 데이터의 모임
- rdbms 관계형데이터베이스
  - 체계화된 데이터의 모임
  - Oracle, mySQL, 마리아(mysql 제작자의 다른 작품), SQLite3, MS-SQL server, DB2(IBM), PostgreSQL(linux), 몽고DM



쿼리 (질의어) structed querry language

- 데이터를 조회하기 위한 명령어
- 조건에 맞는 데이터를 추출하거나 조작하는 명령어
- 쿼리를 날린다 -> db를 조작한다.



스키마

- 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조
- 데이터 베이스의 구조와 제약조건(자료규조, 표현 방법, 관계) 관련한 전반적인 명세를 기술한 것



테이블 

- 열과 행의 모델을 사용해 조작된 데이터 요소들의 집합
- SQL데이터베이스에서는 테이블을 관계(relation)라고도 한다.

- 열 : 컬럼, 필드
- 행 :  레코드, 값

- pk 기본키 : 각 행의 고유값으로 Primary Key라고 부른다. 반드시 설정해야 하고 데이터베이스 관계 설정시 중요한 역할



---



모델

- 웝 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구



ORM object-relational-mapping

- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 프로그래밍 기술

- oop 프로그래밍에서 rdbms을 연동할때 데이터베이스와 oop프로그래밍 언어 간 호환되지 않는 데이터를 변환하는 프로그래밍 기법

- django는 내장된 django orm을 사용함

- 장점 : 

  sql을 잘 알지 못해도 db조작 가능

  sql의 절차적 접근이 아닌 객체 지향적 접근으로 인한 높은 생산성

- 단점 :

  orm만으로 완전한 서비스를 구현하기는 어려움

- 현대 웹 프레임워크의 요점은 웹 개발의 속도를 높이는 것 (생산성)

- db를 객체 object로 조작하기 위해 ORM을 사용한다.



---

작성 및 구현하기

```python
class Article(models, Model):                             # 테이블(내용)
	title = models.charfield(max_length=10)               # 칼럼
	content = models.TextField()
```



- `CharField(max_length=None, **options)`
  - 길이의 제한이 있는 문자열을 넣을 때 사용
  - max_length는 필수 인자
  - 필드의 최대 길이(문자), 데이터베이스 레벨과 django의 유효성 검사(값을 검증하는 것)에서 활용



- `TextField(**options)`

  - 글자의 수가 많을 때 사용
  - max_length 옵션 작성시 자동 양식 필드인 textarea 위젯에 반영은 되지만 모델과 데이터베이스 수준에는 적용되지 않음

  - 



- `Migrations`

  sqlite 익스텐션 설치하기 추가하기
  db.sqlite3 오른쪽 클릭으로 open database 로 열기
  varchar(10) : variable 가변적인 메모리를 사용하는 공간 (2칸사용시 8칸은 자동 줄어든다)

  ```
  $ python manage.py makemigrations
    설계도 생성
    
  $ python manage.py migrate
    설계도 추가
  
  $ python manage.py sqlmigrate articles 0001
  
  $ python manage.py showmigrations                    
    [X]는 체크표시
  ```

  - 장고가 model에 생긴 변화를 반영 하는 방법

  - 마이그레이션 실행 및 db 스키마를 다루기 위한 몇가지 명령어

    - makemigrations

      model을 변경한 것에 기반한 새로운 마이그레이션 설계도를 만들 떄 사용

    - migrate

      설계도를 실제 db에 반영하는 과정

    - sqlmigrate

      마이그레이션에 대한 sql 구문을 보기 위해 사용

      마이그레이션이 sql문으로 어떻게 해석되어서 동작할지 미리 확인 할 수 있음

    - showmigrations

      마이그레이션 파일들이 migrate됐는지 안됐는지 여부를 확인 할 수 있음

    - auto_now_add **중요!!!!!!!!!!!**

      최초 생성 일자

    - auto_now **중요!!!!!!!!!!!**

      

    - 중요한 단계 3가지

      ```
      model.py
      makemigrations
      migrate
      ```

      