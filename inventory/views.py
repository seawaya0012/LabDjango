from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(reqeust):
    #return HttpResponse('<h1>Halif</h>')
    return render(reqeust,'inventory/home.html')
