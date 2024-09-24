from django.shortcuts import render
from blog.models import post
def blog_home(request):
    posts = post.objects.filter(status=1)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)
def blog_single(request):
    return render(request,'blog/blog-single.html')
def test(request):
    posts=post.objects.filter(status=0)
    context={'posts':posts}
    return render(request,'test.html',context)
