"""fboudinetwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import *
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve
from backlane.views import cv, skills, portfolio, folio
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='backlane/home.html')),
    url(r'^contact$', TemplateView.as_view(template_name='backlane/contact.html')),
    #url(r'^skills$', TemplateView.as_view(template_name='backlane/skills.html')),
    url(r'^skills$', skills, name='skills'),
    url(r'^cv$', cv, name='cv'),
    #url(r'^cv$', TemplateView.as_view(template_name='backlane/cv.html')),
    url(r'^portfolio$', portfolio, name='portfolio'),
    url(r'^portfolio/(?P<name>[\w\d\- ]{2,20})$', folio, name='folio'),
    url(r'^polybox3d_ks$', TemplateView.as_view(template_name='backlane/kickstarter.html')),
    path('gallery/', include('gallery.urls', namespace='gallery')),
    # url(r'^.*$', TemplateView.as_view(template_name='backlane/home.html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += [url(r'^media/(?P<name>.*)', portfolio, name='portfolio')]
# urlpatterns += [url(r'^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT})]


#
