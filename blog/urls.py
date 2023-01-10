from django.urls import path
from .views import PostDetail, index_blog, blog_post_dev, blog_post_cyber, blog_post_ia, blog_post_cryptos

urlpatterns = [
    # Liste category
    path('blog/categories/liste/', index_blog, name="index_blog"),
    # Liste des posts category dev
    path('blog/categories/dev/', blog_post_dev, name="blog_post_dev"),
    # Liste des posts category cyber
    path('blog/categories/cyber/', blog_post_cyber, name="blog_post_cyber"),
    # Liste des posts category ia
    path('blog/categories/ia/', blog_post_ia, name="blog_post_ia"),
    # Liste des posts category cryptos
    path('blog/categories/cryptos/', blog_post_cryptos, name="blog_post_cryptos"),
    # Détails des posts
    path('blog/list/categorie/<slug:slug>/details/', PostDetail.as_view(), name='post_detail'),

]
