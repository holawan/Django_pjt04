from ..models import Movie
from rest_framework import serializers



class MovieActorserializer(serializers.ModelSerializer) :

    class Meta :
        model = Movie
        fields = ('title',)

