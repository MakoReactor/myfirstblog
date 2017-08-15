from django.conf.urls import url
from newblog.views import IndexList, post_detail

urlpatterns = [
    url(r'^$', IndexList.as_view(), name='new_index'),
    url(r'^newblog/post/(?P<pk>\d+)/$', post_detail, name='new_post_detail'),


]
