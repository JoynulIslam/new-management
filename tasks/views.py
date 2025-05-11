from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome To The Task management System</h1>")

def contact(request):
    return  HttpResponse("This is contact Page")

def show_task(request):
    return HttpResponse("This is our task Page")
