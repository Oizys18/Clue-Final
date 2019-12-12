from django.shortcuts import render, get_object_or_404
from .models import Movie, Person, Genre, Keyword, Review
from .serializers import MovieSerializer, MovieDetailSerializer, PersonSerializer, PersonDetailSerializer, GenreSerializer, GenreDetailSerializer, KeywordSerializer, KeywordDetailSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import random

# Create your views here.
@api_view(['GET'])
def movies(request):
    movies_all = Movie.objects.all()
    serializer = MovieSerializer(movies_all, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST', 'DELETE'])
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'POST':
        movie = MovieDetailSerializer(data=request.POST)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)

        return Response(status=400)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=204)

    else:
        return Response(status=405)


@api_view(['GET'])
def persons(request):
    persons_all = Person.objects.all()
    serializer = PersonSerializer(persons_all, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def person_detail(request, pk):
    person = Person.objects.get(pk=pk)
    serializer = PersonDetailSerializer(person)
    return Response(serializer.data)


@api_view(['GET'])
def keywords(request):
    keywords_all = Keyword.objects.all()
    serializer = KeywordSerializer(keywords_all, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def keyword_detail(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    serializer = KeywordDetailSerializer(keyword)
    return Response(serializer.data)


@api_view(['GET'])
def genres(request):
    genres_all = Genre.objects.all()
    serializer = GenreSerializer(genres_all, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def genre_detail(request, pk):
    genre = Genre.objects.get(pk=pk)
    serializer = GenreDetailSerializer(genre)
    return Response(serializer.data)


# genres_id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
# genres = ["Biography", "Crime", "Drama", "Action", "Adventure", "Thriller", "Sci-Fi", "Comedy", "Music", "Mystery", "Fantasy", "Romance", "History", "Horror", "Animation", "Family", "Musical", "Western", "War", "Documentary", "Sport"]
genre_dic = {
    "Biography":1, 
    "Crime": 2, 
    "Drama": 3, 
    "Action": 4, 
    "Adventure": 5, 
    "Sci-Fi": 6, 
    "Thriller": 7, 
    "Comedy": 8, 
    "Music": 9, 
    "Mystery": 10, 
    "Fantasy": 11, 
    "Romance": 12, 
    "History": 13, 
    "Horror": 14, 
    "Animation": 15, 
    "Family": 16, 
    "Musical": 17, 
    "War": 18, 
    "Western": 19, 
    "Documentary": 20, 
    "Sport": 21,
}
@api_view(['GET'])
def pick_n(request, num=1, genres="+"):
    user = request.user
    movie_num = Movie.objects.count()
    genres_id = []
    if len(genres) == 1:
        genres_id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    else:
        genres = genres[1:]
        temp = list(genres.split('+'))
        for g in temp:
            if g != '+' and g != '':
                genres_id.append(genre_dic[g])
    seen = set(user.seen_movies.all())
    unseen = set(i for i in range(1, movie_num+1))-set(seen) 
    unseen_pick = Movie.objects.filter(pk__in=unseen).filter(movie_genres__in=genres_id)
    li = [obj.id for obj in unseen_pick]
    pick_num = random.sample(li, min(len(li), num)) 
    picked = Movie.objects.filter(pk__in=pick_num)
    serializer = MovieDetailSerializer(picked, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST', 'DELETE'])
def reviews(request, pk):
    if request.method == 'GET':
        reviews = Review.objects.filter(movie_id=pk)
        serializer = ReviewSerializer(reviews, many=True)

        return Response(serializer.data)

    elif request.method == 'DELETE':
        review_id = request.data.get('review_id')
        review = get_object_or_404(Review, pk=review_id)
        review.delete()
        return Response(status=204)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        movie = get_object_or_404(Movie, pk=pk)
        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(movie_id=pk, user=request.user)

        return Response(serializer.data)
    else:
        return Response(status=405)


@api_view(['POST'])
def movie_seen(request, pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=pk)
    print(movie)
    res = movie.movie_seen_users.add(user)
    print(res)

    return Response(status=200)


@api_view(['POST'])
def movie_like(request, pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=pk)
    res = movie.movie_like_users.add(user)

    return Response(status=200)