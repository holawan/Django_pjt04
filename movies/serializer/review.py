from django.shortcuts import get_object_or_404
from ..models import Movie,Actor,Review
from rest_framework import serializers


class dummyMovieserializer(serializers.ModelSerializer) :

    class Meta :
        model = Movie
        fields = ('title',)

class ReviewListserializer(serializers.ModelSerializer) :

    class Meta :
        model = Review
        fields = ('title','content',)
        

class Reviewserializer(serializers.ModelSerializer) :
    class Meta :
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)
    def to_representation(self, instance) :
        response = super().to_representation(instance)
        response['movie'] = dummyMovieserializer(instance.movie).data 
        return response