# 김동완

## 이번 ptj를 통해 배운 내용

- DRF(Django Rest Framework)를 활용한 API Server 제작

- Database 1:N, M:N에 대한 이해

### 개발도구

- Visual Studio Code
-  Google Chrome Browser
-  Django 3.2+
- Postman

### 요구사항 

- django 프로젝트 이름은 pjt08, 앱 이름은 movies로 지정합니다.
- 모델 간의 관계 설정 후 다음과 같은 기능을 구현합니다. 
- A. Actor 
  - i. 배우 데이터 조회 
- B. Movie 
  - 영화 데이터 조회 
- C. Review 
  - 리뷰 데이터 조회 / 생성 / 수정 / 삭제 

- 데이터 조회는 JSON 데이터 타입을 따릅니다.
  아래 기술된 사항들은 필수적으로 구현해야 하는 내용입니다. 

### Model

- Actor 클래스

| 필드명 | 데이터 유형  |   역할    |
| :----: | :----------: | :-------: |
|  name  | varchar(100) | 배우 이름 |

- Movie 클래스

|    필드명    | 데이터 유형  |    역할     |
| :----------: | :----------: | :---------: |
|    title     | varchar(100) |  영화 제목  |
|   overview   |     text     |   줄거리    |
| release_date |   datetime   |   개봉일    |
| poster_path  |     text     | 포스터 주소 |

- Review

|  필드명  | 데이터 유형  |             역할             |
| :------: | :----------: | :--------------------------: |
|  title   | varchar(100) |          리뷰 제목           |
| content  |     text     |          리뷰 내용           |
| movie_id |   integer    | 외래 키 (Movie 클래스 참조 ) |

#### ERD

![erd](README.assets/erd.PNG)

### 프로젝트 진행

##### 프로젝트는 전반적으로 기능을 구현하며 커밋을 진행했으므로, 커밋 순서에 따라서 진행을 서술하겠습니다.

다만, 협업 프로젝트를 하다보니 정신이 없어 일일히 진행과정을 캡처하지 못해, 최종 결과 캡처본을 첨부합니다.

### D: 김동완, N : 권다솜

### 1단계 : 기본 형식 만들기

#### basic setting 

- 기본적인 장고 세팅을 했습니다.
- 가상환경 설정, gitignore, 프로젝트 생성, 앱 등록, 템플릿(base.html) 만들기를 진행했습니다. 
- api를 다뤄야하고, 가상 데이터를 생성해서 확인하기 위해 django-seed, rest_framwork를 설치했습니다.

### Model 만들기

- ModelSerializer를 사용하기 위해 선제적으로 모델을 만들었습니다.
- ERD명세서에 따라 모델을 구성했으나, ERD필드와 주어진 fixtures 데이터의 형식이 달라 문제를 겪었고, 구현 과정에서 ERD가 잘못되었다는 것을 알게되었습니다.
-  M:N 필드 위치를 조정해 문제를 해결할 수 있었습니다. 

```python
from django.db import models

# Create your models here.

class Actor(models.Model) :
    #배우 이름 
    name = models.CharField(max_length=100)
    
    def __str__(self) :
        return f'배우이름 : {self.name}'

class Movie(models.Model) :
    #영화 제목 
    title = models.CharField(max_length=100)
    #줄거리 
    overview = models.TextField()
    #개봉일 
    release_date = models.DateField()
    #포스터 주소 
    poster_path = models.TextField()
    actors = models.ManyToManyField(Actor,related_name='starring_movie')

    def __str__(self) :
        return f'영화제목 : {self.title} 줄거리 : {self.overview}'


class Review(models.Model) :
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    def __str__(self) :
        return f'영화제목 : {self.title} 줄거리 : {self.content}'

```

![dbsql](README.assets/dbsql.PNG)

### Admin Custom

- 해당 프로젝트의 경우 API를 운영하는 것이고, 편리하게 CRUD를 하는 과정이 없기 때문에, Admin 페이지에서 데이터를 넣어줘야 했습니다.
- 따라서, Admin 페이지에 가독성 있게 데이터를 넣을 수 있도록 Admin 페이지에 List display를 지정하고, Model에는 return 형식을 변경했습니다. 

```python
from django.contrib import admin
from .models import Actor,Movie,Review
# Register your models here.

class ActorAdmin(admin.ModelAdmin) :

    model = Actor
    list_display = ('name',)


class MovieAdmin(admin.ModelAdmin) :

    model = Movie
    list_display = ('title','overview',)


class ReviewAdmin(admin.ModelAdmin) :

    model = Actor
    list_display = ('title','content')

admin.site.register(Actor,ActorAdmin)
admin.site.register(Movie,MovieAdmin)
admin.site.register(Review,ReviewAdmin)
```

- 추가적으로 gitignore를 이용해 db를 원격에서 제거했습니다.

### 2단계 : API 구축

- API 구축에 앞서 url을 분리하고, url 경로를 api/v1으로 설정해주었습니다.

### Actor_list

- serializer를 이용해 view를 작성했습니다. serializer 폴더를 생성해 내부에서 ActorlistSerializer를 만들었고, 이를 통해 db의 데이터를 직렬화 하게 했습니다. get_list_or_404를 이용해 모든 데이터를 가져오고, queryset을 가져오기 때문에, many=True 옵션을 지정했습니다. 
- 명세서에 따라 GET 요청만 허용되도록 view를 작성했습니다. 

![actor_list_get](README.assets/actor_list_get.PNG)

### Actor_detail

- 명세서에서 배우를 조회할 때 배우가 출연한 영화도 조회가 하도록 하는 지시가 있어, manytomany field를 이용해 직렬화 과정의 필드를 추가했습니다.
- 먼저, movieserializer 클래스를 만들고 해당 클래스를 이용 후 역참조를 통해 배우가 출현한 영화 제목을 뽑아내도록 했습니다.

![actor_detail_get](README.assets/actor_detail_get.PNG)



### Movie_list

- 모든 영화 리스트를 출력하게 하는 API를 구성했습니다. 모든 정보가 나올 필요 없으므로 직렬화 과정에서, title과 overview 필드만 노출되게 조정했습니다. 

![movie_list_get](README.assets/movie_list_get.PNG)

### 3단계 : 세부세팅하기







### 느낀점

