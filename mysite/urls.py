"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , re_path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap
from django.http import HttpResponse
from debug_toolbar.toolbar import debug_toolbar_urls

sitemaps = {
    "static": StaticViewSitemap,
    "blog" : BlogSitemap
}

def comming_soon(request):
   return HttpResponse('<h1>به زودی در دسترس خواهد بود</h1>')

urlpatterns = [
    # re_path('',comming_soon),
    path('admin/', admin.site.urls),
    path('',include('website.url')),
    path('blog/',include('blog.urls')),
    path('accounts/',include('accounts.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path("sitemap.xml",sitemap,{"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",),
    path('robots.txt', include('robots.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('captcha/', include('captcha.urls')),

]+ debug_toolbar_urls()

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
