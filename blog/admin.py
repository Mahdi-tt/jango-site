from django.contrib import admin
from blog.models import post
from blog.models import categor

# Register your models here.
class postadmin(admin.ModelAdmin):
    date_hierarchy = 'publish_date'
    empty_value_display = "-empty-"
    list_display=('titel','cuntent_view','status','publish_date',)
    list_filter=('status','author')
    # ordering=['-publish_date']
    search_fields=['titel','content']
admin.site.register(post,postadmin)
admin.site.register(categor)