from blog.forms import BlogPostForm, BlogPostModelForm
from blog.models import BlogPost, BannerImage
from django.shortcuts import render, redirect, get_object_or_404


def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            BlogPost.objects.create(**form.cleaned_data)
            return redirect('thank_you')
    else:
        form = BlogPostForm()
    return render(request, template_name='create_blog_post.html', context={'form': form})


def thank_you(request):
    return render(request, template_name='thank_you.html')

def create_blog_post_model_form(request):
    if request.method == 'POST':
        form = BlogPostModelForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save()
            banner_file = request.FILES.get('banner_image')
            if banner_file:
                BannerImage.objects.create(blog_post=blog_post, image=banner_file)
            return redirect('thank_you')
    else:
        form = BlogPostModelForm()
    return render(request, template_name='create_blog_post_model_form.html', context={'form': form})

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, template_name='blog_detail.html', context={'post': post})
