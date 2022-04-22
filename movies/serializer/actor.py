from .movie import MovieActorserializer
from ..models import Actor
from rest_framework import serializers


class ActorlistSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Actor
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer) :
    starring_movie = MovieActorserializer(many=True,read_only=True)

    class Meta :
        model = Actor
        fields = '__all__'