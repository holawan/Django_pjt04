from ..models import Movie,Actor
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
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer) :
    review_set = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    actors = dumyActorlistSerializer(read_only=True, many=True)
    class Meta :
        model = Movie
        fields = ('title','review_set','actors')
