from django.conf.urls import url
from . import views

urlpatterns = [
    url('count', views.count),url('about', views.index),url('contact', views.contact),url('', views.homepage, name = 'home'),
]
