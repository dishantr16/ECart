from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def demoPage(request):
    return HttpResponse("demo Page")

def demoPageTemplate(request):
    return render(request, "demo.html")