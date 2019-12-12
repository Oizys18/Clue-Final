from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from movies.models import Movie

# Create your models here.


class User(AbstractUser):
    like_movies = models.ManyToManyField(
        Movie, related_name='movie_like_users')
    seen_movies = models.ManyToManyField(
        Movie, related_name='movie_seen_users')
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="followings")
    # comments = models.ForeignKey(Movie, on_delete=models.CASCADE)