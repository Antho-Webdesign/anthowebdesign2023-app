from django.shortcuts import render, get_object_or_404

from blog.models import Post, Category
from portfolio.models import Categorie, Project, Certificat, Tag


def base(request):
    queryset = Project.objects.all()
    querycat = Categorie.objects.all()
    context = {
        'categorie_list': querycat,
        'project_list': queryset,
    }
    return render(request, 'portfolio/index.html', context)


def navbar(request):
    categories = Categorie.objects.all()
    projects = Project.objects.all()
    posts = Post.objects.all()
    cat_blog = Category.objects.all()

    context = {
        'categories_list': categories,
        'projects_list': projects,
        'posts_list': posts,
        "cat_blog_list": cat_blog,
    }
    return render(request, 'inc/navbar.html', context)


def footer(request):
    querycat = Categorie.objects.all()
    queryset = Project.objects.all()
    context = {
        'categorie_list': querycat,
        'project_list': queryset,
    }
    return render(request, 'portfolio/inc/navbar.html', context)


# Index
def index(request):
    querycat = Categorie.objects.all()
    queryset = Project.objects.all()
    context = {
        'project_list': queryset,
        'categorie_list': querycat,
    }
    return render(request, 'portfolio/index.html', context)


def category_list(request):
    querycat = Categorie.objects.all()
    queryset = Project.objects.all()
    context = {
        'project_list': queryset,
        'categorie_list': querycat,
    }
    return render(request, 'portfolio/projets/category/list_category.html', context)


def project_list(request, slug):
    querycat = Categorie.objects.all()
    queryset = Project.objects.filter(category__slug=slug)
    tag = Tag.objects.all()
    context = {
        'project_list': queryset,
        'categorie_list': querycat,
        'tags': tag,
    }
    return render(request, 'portfolio/projets/category/list_project.html', context)


def details_projet(request, slug):
    details_project = get_object_or_404(Project, slug=slug)
    tag = Tag.objects.all()
    context = {
        'details_project': details_project,
        'tags': tag,
    }

    return render(request, 'portfolio/projets/category/details_projet.html', context)


def certificats(request):
    queryset = Certificat.objects.all()
    context = {
        'certificat_list': queryset,
    }

    return render(request, 'portfolio/certificats/certificats.html', context)
