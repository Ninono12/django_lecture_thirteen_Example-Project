from django.urls import path
from blog.views import create_blog_post, thank_you, create_blog_post_model_form, blog_detail

urlpatterns = [
    path('create_blog_post/', create_blog_post, name='create_blog_post'),
    path('thank_you/', thank_you, name='thank_you'),
    path('create_blog_post_model_form/', create_blog_post_model_form, name='create_blog_post_model_form'),
    path('blog_detail/<int:post_id>/', blog_detail, name='blog_detail'),
]
