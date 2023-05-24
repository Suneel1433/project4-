from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def sunil(request):
    return HttpResponse("<h1><i>i am python developer</i></h1>")
def vineeth(request):
    return HttpResponse("<h1><i> tomaarow django mock interview is there</i></h1>")
def ganesh(request):
    return render(request,'loginpage.html')
def karthik(request):
    return render(request,'loginpage2.html')