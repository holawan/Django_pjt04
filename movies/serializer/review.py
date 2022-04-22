from ..models import Movie,Actor,Review
from rest_framework import serializers



class ReviewListserializer(serializers.ModelSerializer) :

    class Meta :
        model = Review
        fields = ('title','content',)
        read_only_fields = ('movie',)