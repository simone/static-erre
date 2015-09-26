"""ncc4roma URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import RedirectView
from website.views import HtmlTemplate, TemplateView

urlpatterns = [

    url(r'^(?P<lang>\w{2})/*$', RedirectView.as_view(url='/%(lang)s/index.html', permanent=True)),
    url(r'^$', RedirectView.as_view(url='/it/index.html', permanent=True), name='index'),
    url(r'^robots.txt$', TemplateView.as_view(template_name='tpl/robots.txt'), name='robots'),


] + i18n_patterns('',
    url(r'^(?P<page_name>[^/.]+\.html)', HtmlTemplate.as_view())
)
