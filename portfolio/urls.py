from django.urls import path

from portfolio.views import index, category_list, project_list, details_projet, certificats

urlpatterns = [
    path('', index, name='index_portfolio'),
    path('liste/categorie/', category_list, name='project_category_list'),
    path('liste/projets/<str:slug>', project_list, name='project_list'),
    path('details/projet/<slug:slug>/', details_projet, name='details_projet'),
    path('certificats/', certificats, name='certificats'),
]
