from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("coding/", views.coding, name="coding"),
    path("about/", views.about, name="about"),
    path("docs/", views.docs, name="docs")
]
