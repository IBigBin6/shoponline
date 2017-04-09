#!/usr/bin/env python
# encoding: utf-8


from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    url(r'^$',views.index,{'template_name':'catalog/index.html'},name='index'),
    url(r'^product/(?P<product_name>[-\w]+)$',views.show_product,
        {'template_name':'catalog/show_product.html'},name='show_product'),
    url(r'^register$',views.register,{'template_name':'catalog/register.html'}),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
