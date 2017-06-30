from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.utils import timezone
from blog.models import Post

class IndexList(ListView):
    model = Post
    template_name = 'newblog/index.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self,):
        #queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'newblog/post_detail.html', {'post':post})