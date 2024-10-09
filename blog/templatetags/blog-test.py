from django import template
from blog.models import post

register = template.Library()

@register.simple_tag(name='totalpost')
def hello():
    posts=post.objects.filter(status=1)
    return  posts
@register.simple_tag(name='posts')
def hello():
    posts=post.objects.filter(status=1)
    return  posts
@register.filter(name='filter')
def h1(value,arg=20):
    return value[:arg]+'...'

@register.inclusion_tag('pupilarpost.html')
def pupilarpost():
    posts=post.objects.filter(status=1).order_by('publish_date')[:1]
    return {'posts':posts}
