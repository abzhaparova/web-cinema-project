from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class MovieManager(models.Manager):
    def genre_filter(self, genre_list):
        movies = super().get_queryset()
        for genre in genre_list:
            movies = movies.filter(genres__name=genre)
        return movies


class User(AbstractUser):
    profile_picture = models.CharField(max_length=500)
    pass


class CommentPage(models.Model):
    pass


class Comment(models.Model):
    username = models.CharField(max_length=500)
    message = models.CharField(max_length=500)
    date_posted = models.DateTimeField(default=datetime.now())
    score = models.IntegerField()
    comment_page = models.ForeignKey(CommentPage, on_delete=models.CASCADE, related_name='comments', blank=True)


class Movie(models.Model):
    title = models.CharField(max_length=500, blank=True)
    background = models.CharField(max_length=500, blank=True)
    poster = models.CharField(max_length=500, blank=True)
    release_date = models.CharField(max_length=500, blank=True)
    director = models.CharField(max_length=500, blank=True)
    cast = models.CharField(max_length=500, blank=True)
    synopsis = models.CharField(max_length=5000, blank=True)
    comment_page = models.ForeignKey(CommentPage, on_delete=models.CASCADE, blank=True)
    objects = models.Manager()
    genre_manager = MovieManager()


class Genre(models.Model):
    name = models.CharField(max_length=500)
    movies = models.ManyToManyField(Movie, related_name='genres')
