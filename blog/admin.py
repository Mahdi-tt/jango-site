from django.contrib import admin
from blog.models import post
from blog.models import categor
from django_summernote.admin import SummernoteModelAdmin
from blog.models import comment

# Register your models here.
class postadmin(SummernoteModelAdmin):
    date_hierarchy = 'publish_date'
    empty_value_display = "-empty-"
    list_display=('titel','cuntent_view','status','publish_date',)
    list_filter=('status','author')
    # ordering=['-publish_date']
    search_fields=['titel','content']
    summernote_fields = ('content',)

class commentadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    list_display=('name','approved','created_date',)
    list_filter=('name','approved')
    # ordering=['-publish_date']
    search_fields=['name','approved']

admin.site.register(comment,commentadmin)
admin.site.register(post,postadmin)
admin.site.register(categor)