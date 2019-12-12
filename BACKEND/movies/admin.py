from django.contrib import admin
from .models import Movie, Person, Keyword, Genre
# Register your models here.
admin.site.register(Movie)
admin.site.register(Person)
admin.site.register(Genre)
admin.site.register(Keyword)
