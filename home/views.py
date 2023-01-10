from django.shortcuts import render


def home(request):
    project = Project.objects.all()
    categorie = Category.objects.all()
    context = {
        'project': project,
        'categories': categorie,
    }
    return render(request, 'home/home.html', context)
