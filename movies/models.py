from django.db import models

# Create your models here.

class Movie(models.Model) :
    #영화 제목 
    title = models.CharField(max_length=100)
    #줄거리 
    overview = models.TextField()
    #개봉일 
    release_date = models.DateTimeField()
    #포스터 주소 
    poster_path = models.TextField()
    
class Actor(models.Model) :
    #배우 이름 
    name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie,related_name='starring_actors')

    

class Review(models.Model) :
    title = models.CharField(max_length=100)
    content = models.TextField()
    movies = models.ForeignKey(Movie,on_delete=models.CASCADE)
