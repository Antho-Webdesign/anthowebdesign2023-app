from django.contrib import admin

from portfolio.models import Categorie, Project, Certificat, Tag


class ProjectAdmin(admin.ModelAdmin):
    class Meta:
        model = Project
        list_display = ('title', 'slug', 'project_thumbnail', 'description', 'date_created_on', 'status', 'categorie',
                        'tags')
        list_filter = ('categorie', 'tags')
        search_fields = ('title', 'description')
        prepopulated_fields = {'slug': ('title',)}


class CategorieAdmin(admin.ModelAdmin):
    class Meta:
        model = Categorie
        list_display = ('category_name', 'slug', 'image_cat', 'projet_cat_description')
        search_fields = ('category_name', 'projet_cat_description')
        prepopulated_fields = {'slug': ('category_name',)}


admin.site.register(Categorie, CategorieAdmin)

admin.site.register(Project, ProjectAdmin)

admin.site.register(Certificat)

admin.site.register(Tag)
