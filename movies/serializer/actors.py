from ..models import Actor
from rest_framework import serializers



class ActorlistSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Actor
        fields = '__all__'