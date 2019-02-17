from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")

def count(request):
    data = request.GET["area"]
    wordlist = data.split()
    list = len(wordlist)

    dictionary = {}

    for word in wordlist:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return render(request,"cnt.html",{"fulltext" : data, "words" : list, "dictionary" : dictionary  })

def homepage(request):
    return HttpResponse("<h1>THIS IS HOMEPAGE</h1>")

def contact(request):
    return HttpResponse("<h1>contact us </h1> <br> this is our contact")