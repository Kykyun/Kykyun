from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new_course", views.new_course, name="new_course"),
    path("course", views.course, name="course"),
    path("search_course", views.search_course, name="search_course"),
    path("search_by_course", views.search_course, name="search_by_course"),

    ]
