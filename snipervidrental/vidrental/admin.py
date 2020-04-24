from django.contrib import admin
from .models import Movie, Genre
# Register your models here.
from . import models


class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["movie_name"] }),
        ("Financials", {"fields": ["stock", "rate"]}),
        ("Genre information", {"fields": ["genre"]})
    ]
    list_display = ("movie_name", "genre", "stock", "rate")



admin.site.register(Movie, MovieAdmin)
