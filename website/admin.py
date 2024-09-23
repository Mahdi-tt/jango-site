from django.contrib import admin
from website.models import contact

# Register your models here.
class contactadmin(admin.ModelAdmin):
    date_hierarchy = 'creatade_date'
    list_display = ('name','subject','email','creatade_date',)
    list_filter = ('email',)
    search_fields = ('name','massage',)
admin.site.register(contact,contactadmin)
