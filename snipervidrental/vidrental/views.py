from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Movie, Genre
from django.views import generic
# Create your views here.


def index(request):
    template = loader.get_template("vidrental/index.html")
    context = {"movie_list": Movie.objects.all()}
    return HttpResponse(template.render(context, request))

class DetailView(generic.DetailView):
    model = Movie
    template_name = "vidrental/detail.html"