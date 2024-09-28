from django.shortcuts import render , get_object_or_404
from blog.models import post
from django.utils import timezone
def blog_home(request):
    now= timezone.now()
    posts = post.objects.filter(publish_date__lte=now,status=1)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)
def blog_single(request,pid):
    posts=get_object_or_404(post,pk=pid,status=1)
    posts.cuntent_view +=1
    posts.save()
    context={'posts':posts}
    return render(request,'blog/blog-single.html',context)

def test(request,name,lname,age):
    context={'name':name,'lname':lname, 'age':age}
    return render(request,'test.html',context)
