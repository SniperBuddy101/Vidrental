from django.db import models

# Create your models here.

class Genre(models.Model):
    genre_text = models.CharField(max_length=200)

    def __str__(self):
        return self.genre_text

class Movie(models.Model):
    movie_name = models.CharField(max_length=200)
    stock = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.movie_name


