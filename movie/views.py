from django.shortcuts import render
# Create your views here.
dic = {"name": "Jorge A. Villarreal Márquez"}
def home(req):
    return render(req, "home.html", 
                  dic)
def about(req):
    return render(req, "about.html", 
                  dic)
