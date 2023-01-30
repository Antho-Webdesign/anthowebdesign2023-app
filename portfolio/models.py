from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Tag(models.Model):
    tag_name = models.CharField(max_length=120, blank=True, null=True)
    slug = models.SlugField(max_length=120, blank=True, null=True)
    image_tag = models.ImageField(upload_to='images/portfolio/prod/tag/', default='images/default.png', blank=True,
                                  null=True)

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['tag_name']


class Contact(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(max_length=2500, blank=True, null=True)
    date_send = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_send']


class Categorie(models.Model):
    category_name = models.CharField(max_length=120, blank=True, null=True)
    slug = models.SlugField(max_length=120, blank=True, null=True)
    image_cat = models.ImageField(upload_to='images/portfolio/prod/category/',
                                  default='images/default.png')
    projet_cat_description = models.TextField(max_length=2500, blank=True, null=True)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('project_category_list', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'
        ordering = ['category_name']


PROJECT_STATUS = (
    ('En Cours', 'En Cours'),
    ('Terminé', 'Terminé'),
    ('Suspendu', 'Suspendu'),
)


class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    description = models.TextField()
    date_created_on = models.DateTimeField(auto_now_add=True)
    project_status = models.CharField(choices=PROJECT_STATUS, default='en_cours', max_length=30)
    project_thumbnail = models.ImageField(upload_to='images/portfolio/prod/project/',
                                          default='images/default.png')
    project_url = models.URLField(max_length=200, default='#', blank=True, null=True)
    git_url = models.URLField(max_length=200, default='#', blank=True, null=True)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='cat_projects',
                                 blank=True, null=True)
    project_goal = models.CharField(max_length=500, blank=True, null=True)
    type = models.CharField(max_length=120, blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='tag_projects', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_details', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-date_created_on']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class Certificat(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    image = models.ImageField(upload_to='images/portfolio/certificats/', blank=True, null=True,
                              default='images/default.png')
    slug = models.SlugField(max_length=250, unique=True)
    delivery_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    delivrer_par = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-delivery_date']
        verbose_name = 'Certificat'
        verbose_name_plural = 'Certificats'
