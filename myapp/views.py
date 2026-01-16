from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def page1(request):
    return HttpResponse("Hello world!")

def page2(request):
    return HttpResponse("Hello")

def page2(request):
    return render (request,'myfile.html')

def page3(request):
    return render (request,'loginpage.html')

