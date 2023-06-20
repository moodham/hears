from django.urls import path

from .views import home, search, searchpages, pic, vid,wrs


urlpatterns = [
    path("", home, name="home"),
    path("s", search, name="search"),
    path("searchpages/<pagenumber>", searchpages, name="searchpages"),

    path("wrs/<number>", wrs, name="wrs"),
    path("pic", pic, name="pic"),
    path("vid", vid, name="vid"),
]
