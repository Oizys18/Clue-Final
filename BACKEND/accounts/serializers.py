from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'is_superuser')

from movies.serializers import MovieSerializer

class UserDetailSerializer(serializers.ModelSerializer):
    like_movies = MovieSerializer(many=True)

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('like_movies',)
