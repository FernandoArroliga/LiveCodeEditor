from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def coding(request):
    return render(request, "coding.html")

def about(request):
    return render(request, "about.html")

def docs(request):
    return render(request, "docs.html")

def html_docs(request):
    return render(request, "html_docs.html")

def css_docs(request):
    return render(request, "css_docs.html")

def js_docs(request):
    return render(request, "js_docs.html")