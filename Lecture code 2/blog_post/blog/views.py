from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import BlogPostForm, BlogPostModelForm
from blog.models import BlogPost, BlogPostCover


def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            BlogPost.objects.create(**form.cleaned_data)
            return redirect('success_page_blog_post_created')
    else:
        form = BlogPostForm()

    return render(request, template_name='create_blog_post.html', context={'form': form})


def success_page_blog_post_created(request):
    return render(request, template_name='success_page_blog_post_created.html')


def create_blog_post_model_form(request):
    if request.method == 'POST':
        form = BlogPostModelForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save()
            cover = form.cleaned_data.get('cover', None)
            if cover:
                BlogPostCover.objects.create(blog_post=blog_post, image=cover)

            return redirect('success_page_blog_post_created')
    else:
        form = BlogPostModelForm()

    return render(request, template_name='create_blog_post_model_form.html', context={'form': form})


def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, template_name='blog_detail.html', context={'post': post})
