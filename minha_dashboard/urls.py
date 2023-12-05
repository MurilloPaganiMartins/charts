from django.urls import path
from . import views
from .views import medias

urlpatterns = [
    path('', views.home, name="home"),
    path('medias', views.medias, name="medias"),
    path('medias/<str:start_date>/<str:end_date>/', medias, name='medias_with_dates'),

]