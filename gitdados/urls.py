from django.conf.urls import url
from .views import profile, teste


urlpatterns = [
    url(r'^$', profile, name='profile'),
    url(r'^teste/$', teste, name='teste'),
    
]