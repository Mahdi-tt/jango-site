from django.shortcuts import render , get_object_or_404
from blog.models import post
from django.utils import timezone
def blog_home(request):
    now= timezone.now()
    posts = post.objects.filter(publish_date__lte=now,status=1)
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

def test(request,name,lname,age):
    context={'name':name,'lname':lname, 'age':age}
    return render(request,'test.html',context)