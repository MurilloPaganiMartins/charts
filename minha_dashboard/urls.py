from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('medias', views.medias, name="medias")

]

