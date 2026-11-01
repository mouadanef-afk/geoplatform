from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cities/", views.city_list_page, name="city-list"),
    path("api/cities/", views.city_list_api, name="api-city-list"),
    path("api/cities/<str:name>/", views.city_detail_api, name="api-city-detail"),
]