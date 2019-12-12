from django.db import models
from django.conf import settings

# Create your models here.


class Person(models.Model):
    imdb_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)

    # class Meta():
    #     ordering = ('imdb_id',)

    def __str__(self):
        return self.name


class Keyword(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content


class Genre(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content


class Movie(models.Model):
    tconst = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    rating = models.FloatField()
    runtimes = models.CharField(max_length=10)
    thumbnail_url = models.TextField()
    poster_url = models.TextField()
    trailer_url = models.TextField()
    plot = models.TextField()
    plot_outline = models.TextField()
    movie_directors = models.ManyToManyField(
        Person, related_name='director_movies')
    movie_cast = models.ManyToManyField(Person, related_name='cast_movies')
    movie_keywords = models.ManyToManyField(
        Keyword, related_name='keyword_movies')
    movie_genres = models.ManyToManyField(Genre, related_name='genre_movies')

    class Meta:
        ordering = ('-rating',)

    def __str__(self):
        return f'{self.title}({self.year})'


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-pk',)
