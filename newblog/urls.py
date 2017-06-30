from django.conf.urls import url
from .views import IndexList, post_detail

urlpatterns = [
    url(r'^$', IndexList.as_view(), name='index'),
    url(r'^post/(?P<pk>\d+)/$', post_detail, name='post_detail'),
    
]
