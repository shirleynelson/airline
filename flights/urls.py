from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from . import views
from .views import index

urlpatterns = [
    path("", views.index, name="index"),
    url(r'^tools$', index),
   url(r'^admin/', include(admin.site.urls)),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book")
]
