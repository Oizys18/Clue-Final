from rest_framework import serializers
from .models import Movie, Person, Genre, Keyword, Review


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'content',)


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ('id', 'content',)


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'imdb_id', 'name',)


class MovieSerializer(serializers.ModelSerializer):
    movie_directors = PersonSerializer(many=True)
    movie_genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'year', 'rating', 'runtimes', 'thumbnail_url',
                  'poster_url', 'trailer_url', 'plot_outline', 'movie_genres', 'movie_directors',)


from accounts.serializers import UserSerializer


class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('id', 'content', 'created_at', 'movie', 'user')


class MovieDetailSerializer(serializers.ModelSerializer):
    movie_cast = PersonSerializer(many=True)
    movie_directors = PersonSerializer(many=True)
    movie_keywords = KeywordSerializer(many=True)
    movie_genres = GenreSerializer(many=True)
    movie_seen_users = UserSerializer(many=True)
    review_set = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'tconst', 'title', 'year', 'rating', 'runtimes', 'thumbnail_url', 'poster_url', 'trailer_url',
                  'plot', 'plot_outline', 'movie_genres', 'movie_keywords', 'movie_directors', 'movie_cast', 'movie_seen_users', 'review_set')


class PersonDetailSerializer(serializers.ModelSerializer):
    cast_movies = MovieSerializer(many=True)
    director_movies = MovieSerializer(many=True)

    class Meta:
        model = Person
        fields = ('id', 'imdb_id', 'name', 'cast_movies', 'director_movies',)


class GenreDetailSerializer(serializers.ModelSerializer):
    genre_movies = MovieSerializer(read_only=True, many=True)

    class Meta:
        model = Genre
        fields = ('id', 'content', 'genre_movies',)


class KeywordDetailSerializer(serializers.ModelSerializer):
    keyword_movies = MovieSerializer(many=True)

    class Meta:
        model = Keyword
        fields = ('id', 'content', 'keyword_movies',)
