from django import template
from blog.models import post
from blog.models import categor
from django.utils import timezone
register = template.Library()

@register.inclusion_tag('website/website-lates-post.html')
def lates_post():
    posts=post.objects.filter(status=1).order_by('-publish_date')[:3]
    context={'posts':posts}
    return context
    