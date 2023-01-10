from django.shortcuts import render, get_object_or_404

from django.views import generic
from .models import Post, Category


def index_blog(request):
    queryset = Post.objects.all()
    querycat = Category.objects.all()
    context = {
        'post_list': queryset,
        'categorie_list': querycat,
    }
    return render(request, 'blog/index_blog.html', context)

def navbar(request):
    querycat = Category.objects.all()
    queryset = Post.objects.all()
    context = {
        'categorie_list': querycat,
        'post_list': queryset,
    }
    return render(request, 'blog/inc/navbar.html', context)


def blog_post_dev(request):
    post = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'posts': post,
        'categorie': categories,
    }
    return render(request, 'blog/dev/devactus.html', context)

def blog_post_cyber(request):
    post = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'posts': post,
        'categorie': categories,
    }
    return render(request, 'blog/cyber/cyberactus.html', context)

def blog_post_ia(request):
    post = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'posts': post,
        'categorie': categories,
    }
    return render(request, 'blog/ia/ia.html', context)


def blog_post_cryptos(request):
    post = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'posts': post,
        'categorie': categories,
    }
    return render(request, 'blog/cryptomonnaie/cryptoactus.html', context)



class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    app_name = 'blog'

