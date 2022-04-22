from django.shortcuts import get_list_or_404,get_object_or_404

from movies.serializer.movie import  MovielistSerializer,MovieSerializer
from movies.serializer.review import ReviewListserializer, Reviewserializer
from .models import Actor,Movie,Review
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer.actor import ActorlistSerializer,ActorSerializer
# Create your views here.
from rest_framework import status
@api_view(['GET'])
def actor_list(request) :
    actors = get_list_or_404(Actor)

    serializer = ActorlistSerializer(actors,many=True)

    return Response(serializer.data)


@api_view(['GET'])
def actor_detail(request,actor_pk) :
    actor = get_object_or_404(Actor,pk=actor_pk)

    serializer = ActorSerializer(actor)

    return Response(serializer.data)

@api_view(['GET'])
def movie_list(request) :
    movies = get_list_or_404(Movie)

    serializer = MovielistSerializer(movies,many=True)

    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request,movie_pk) :
    movie = get_object_or_404(Movie,pk = movie_pk)
    serializer = MovieSerializer(movie)

    return Response(serializer.data)

@api_view(['GET'])
def review_list(request) :
    reviews = get_list_or_404(Review) 
    serializer = ReviewListserializer(reviews,many=True)

    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def review_detail(request,review_pk) :
    review = get_object_or_404(Review,pk=review_pk)
    if request.method == 'GET' : 
        review = get_object_or_404(Review,pk=review_pk)
        serializer = Reviewserializer(review)

        return Response(serializer.data)
    
    elif request.method == 'PUT' :
        serializer = Reviewserializer(review,data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == "DELETE" :
        review.delete()
        data = {
            'delete' : f'{review_pk}번 리뷰가 삭제되었습니다.'
        }
        return Response(data,status=status.HTTP_204_NO_CONTENT)

