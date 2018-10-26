from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView
import app.views as appViews

urlpatterns = [
	url(r'^$', appViews.home, name='home'),
	url(r'home/', appViews.home, name='home'),
	url(r'offer/', appViews.offer, name='offer'),
	url(r'pricing/', appViews.pricing, name='pricing'),
	url(r'contact/', appViews.contact, name='contact'),
	url(r'online/', appViews.online, name='online'),
    path('admin/', admin.site.urls)
]