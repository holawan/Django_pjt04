from django.shortcuts import get_object_or_404
from ..models import Movie,Actor,Review
from rest_framework import serializers
class MovielistSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Movie
        fields = ('title','overview',)

class dummyMovieserializer(serializers.ModelSerializer) :

    class Meta :
        model = Movie
        fields = ('title',)

# class ReviewListserializer(serializers.ModelSerializer) :
    
#     class Meta :
#         model = Review
#         fields = ('title','content',)
        

class Reviewserializer(serializers.ModelSerializer) :
    # def to_representation(self, instance) :
    #     response = super().to_representation(instance)
    #     response['movie'] = dummyMovieserializer(instance.movie).data 
    #     return response
    movie = dummyMovieserializer(read_only=True)
    class Meta :    
        model = Review
        fields = '__all__'
