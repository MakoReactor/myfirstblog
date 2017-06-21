from django.conf.urls import url
from .views import profile, index


urlpatterns = [
    url(r'^$', profile, name='profile'),
    url(r'^index/$', index, name='index'),
]
