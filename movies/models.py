from django.db import models

# Create your models here.

class Actor(models.Model) :
    #배우 이름 
    name = models.CharField(max_length=100)
    

class Movie(models.Model) :
    #영화 제목 
    title = models.CharField(max_length=100)
    #줄거리 
    overview = models.TextField()
    #개봉일 
    release_date = models.DateTimeField()
    #포스터 주소 
    poster_path = models.TextField()
    actors = models.ManyToManyField(Actor,related_name='starring_movie')



    

class Review(models.Model) :
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
