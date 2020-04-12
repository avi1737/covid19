from django.shortcuts import render
import requests
import json
# Create your views here.


def home(request):
    response = requests.get('https://api.covid19api.com/summary')
    data = response.json()
    globalRecord = data['Global']
    print(globalRecord)
    return render(request,'corona/home.html',{"globalRecord":globalRecord})



def news(request):
    response = requests.get('https://newsapi.org/v2/top-headlines',{"apikey":"6d75627c61754ef8926c25aae505f197","country":"in",'category':"health"})
    data = response.json()
    articles = data['articles']
    print(articles)
    return render(request,'corona/news.html',{'headline':articles})

def countrywise(request):
    
    return render(request,'corona/country.html')
