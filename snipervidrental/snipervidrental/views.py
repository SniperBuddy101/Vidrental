from django.shortcuts import render
from django.http import HttpResponse

def siteindex(request):
    return render(request, "homepage.html")
