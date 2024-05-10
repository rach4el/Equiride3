from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_Equiride(request):
    return HttpResponse("Hello, Booking System!")

def homepage(request):
    return render(request, 'homepage.html')