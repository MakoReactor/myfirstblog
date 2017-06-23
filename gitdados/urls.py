from django.conf.urls import url
from .views import profile, index, marketing, mycep


urlpatterns = [
    url(r'^$', profile, name='profile'),
    url(r'^index/$', index, name='index'),
    url(r'^marketing/$', marketing, name='marketing'),
    url(r'^cep/$', mycep, name='cep'),
]
