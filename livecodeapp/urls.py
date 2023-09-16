from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("coding/", views.coding, name="coding"),
    path("about/", views.about, name="about"),
    path("docs/", views.docs, name="docs"),
    path("html_docs/", views.html_docs, name="html_docs"),
    path("css_docs/", views.css_docs, name="css_docs"),
    path("js_docs/", views.js_docs, name="js_docs"),
    path("credits/", views.credits, name="credits"),
    path("tutorials/", views.tutorials, name="tutorials"),
]
