from .import views
from django.urls import include, path

urlpatterns = [
    path('',views.home,name='covid-home'),
    path('news',views.news,name='covid-news'),
    path('counrty-wise',views.countrywise,name='country-wise')
]
