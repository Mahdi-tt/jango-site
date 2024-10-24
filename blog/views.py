from django.shortcuts import render , get_object_or_404
from django.http import *
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from blog.models import post
from django.utils import timezone

from website.forms import contactforms

def blog_home(request,cat_name=None,author_username=None,tag_name=None):
    now= timezone.now()
    posts = post.objects.filter(publish_date__lte=now,status=1)
    if cat_name:
        posts=posts.filter(categore__name=cat_name)
    if author_username:
        posts=posts.filter(author__username=author_username)
    if tag_name:
       posts=posts.filter(tags__name=tag_name)
    paginat= Paginator(posts,2)
    page_number=request.GET.get("page")
    try:
        posts= paginat.get_page(page_number)
    except PageNotAnInteger :
        posts = paginat.get_page(1)
    except EmptyPage :
        posts = paginat.get_page(1) 
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    now= timezone.now()
    posts=get_object_or_404(post,pk=pid,status=1,publish_date__lte=now)
    posts.cuntent_view +=1
    posts.save()
    post_all=post.objects.filter(publish_date__lte=now,status=1)
    post_index=list(post_all).index(posts)
    back_post= post_all[post_index - 1] if post_index > 0 else None
    next_post= post_all[post_index +1] if post_index < len(post_all) - 1 else None
    if back_post and back_post.status != 1:
        back_post=None
    if next_post and next_post.status != 1:
        next_post=None

    context={'posts':posts,
             'next_post':next_post,
             'back_post':back_post}
    return render(request,'blog/blog-single.html',context)

def blog_category(request, cat_name):
    posts= post.objects.filter(status=1)
    p=posts.filter(categore__name=cat_name)
    context={'posts':p}
    return render(request,'blog/blog-home.html',context)
def blog_search(request):
    posts=post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('search'):
            posts=posts.filter(content__contains=s)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)   
    
def test(request):
    if request.method == 'POST':
        form = contactforms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect ("done")
        
        elif request.method== 'GET':
            print('get')
    else:
        form=contactforms
    return render(request,'test.html',{'form':form})
