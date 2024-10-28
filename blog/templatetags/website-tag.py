from django import template
from blog.models import post
from blog.models import categor
from django.utils import timezone
register = template.Library()

@register.inclusion_tag('website/website-lates-post.html')
def lates_post(pid):
    posts=post.objects.filter(pk=pid,status=1)[:3]
    context={'posts':posts}
    return context
    # now=timezone.now()
    # posts=post.objects.filter(status=1,publish_date__lte=now).order_by('-publish_date')
    # cat= categor.objects.all()
    # cat_dict = {}
    # for name in cat:
    #     cat_dict[name]=posts.filter(categore = name )
        
    # return {'posts': posts[:arg], 'category': cat_dict}
    