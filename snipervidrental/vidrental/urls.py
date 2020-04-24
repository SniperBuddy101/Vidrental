from django.urls import path
from . import views
from django.http import request

app_name = "vidrental"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail")
]