from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from django.views.generic import ListView
=======
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
>>>>>>> e2764039380b949cfb85bc33eff9b9e27be5cc79
from django.utils import timezone
from .models import Post
from .forms import PostForm

<<<<<<< HEAD
#def post_list(request):
#    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
#    return render(request, 'blog/post_list.html', {'posts':posts})

class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 3
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')




=======

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 3)
    try:
        posts_paginados = paginator.page(page)
    except PageNotAnInteger:
        posts_paginados = paginator.page(1)
    except EmptyPage:
        posts_paginados = paginator.page(paginator.num_pages)

    

    return render(request, 'blog/post_list.html', {'posts_paginados':posts_paginados})
>>>>>>> e2764039380b949cfb85bc33eff9b9e27be5cc79

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'posts_paginados':posts_paginados})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form':form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

post_list = PostList.as_view()