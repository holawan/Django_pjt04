from ..models import Movie,Actor,Review
from rest_framework import serializers



class MovieActorserializer(serializers.ModelSerializer) :

    class Meta :
        model = Movie
        fields = ('title',)

class MovielistSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Movie
        fields = ('title','overview',)


class dumyActorlistSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Actor
        fields = ('name',)

class dumyReviewSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Review 
        fields = ('title','content')
        read_only_fields = ('movie',)

class MovieSerializer(serializers.ModelSerializer) :
    review_set = dumyReviewSerializer(many=True,read_only=True)
    # reviews = Review.objects.get(pk=review_set)
    actors = dumyActorlistSerializer(read_only=True, many=True)
    class Meta :
        model = Movie
        fields = ('title','actors','review_set',)
