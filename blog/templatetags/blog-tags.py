from django import template
from blog.models import post
from blog.models import categor

register = template.Library()

@register.inclusion_tag('blog/blog-lates-posts.html')
def latespost(arg=2):
    posts=post.objects.filter(status=1).order_by('publish_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-category.html')
def postcategory():
    posts=post.objects.filter(status=1)
    categories=categor.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(categore=name).count()
    return {'categorys':cat_dict}

    