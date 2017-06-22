from django.conf.urls import url
from .views import profile, index, marketing


urlpatterns = [
    url(r'^$', profile, name='profile'),
    url(r'^index/$', index, name='index'),
    url(r'^marketing/$', marketing, name='marketing'),
]
