from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User

# Options
STATUS_BIT_ARTICLE = (
	(1, 'Active'),
	(0, 'In Active'),
)

# Queryset section
class ArticlesQuerySet(models.QuerySet):
    def getAboutUs(self):
        return self.filter(
           ( Q(active=1) & Q(section_id=1) )
        )
    def getCosmetics(self):
    	return self.filter(
    		( Q(active=1) & Q(section_id=2) )
    	)
    def getCosmeticTreatment(self):
    	return self.filter(
    		( Q(active=1) & Q(section_id=3) )
    	)

    def getOffer(self):
    	return self.filter(
    		( Q(active=1) & Q(section_id=4) )
    	)

# Models
class Sites(models.Model):
	tabs=models.CharField(max_length=300, null=True,unique=True)
	createDate=models.DateTimeField(auto_now=True, blank=True)
	creator=models.ForeignKey(User,related_name="sites_creator",on_delete=models.CASCADE)
	def __str__(self):
		return str(self.tabs)

class Section(models.Model):
	title=models.CharField(max_length=255)
	createDate=models.DateTimeField(auto_now=True, blank=True)
	creator=models.ForeignKey(User,related_name="section_creator", on_delete=models.CASCADE)
	sites=models.ForeignKey(Sites, related_name="section_to_site", on_delete=models.CASCADE)
	def __str__(self):
		return str(self.title)

class Articles(models.Model):
	content=models.TextField(max_length=10000)
	description=models.CharField(max_length=100)
	active=models.BooleanField(default=True, choices=STATUS_BIT_ARTICLE)
	createDate=models.DateTimeField(auto_now=True)
	creator=models.ForeignKey(User, related_name="article_creator", on_delete=models.CASCADE)
	section=models.ForeignKey(Section, related_name="article_to_section", on_delete=models.CASCADE)

	objects = ArticlesQuerySet.as_manager()

	def __str__(self):
		return str(self.content)

class Price(models.Model):
	service=models.CharField(max_length=200)
	price=models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
	def __str__(self):
		return str(self.service)

class Message(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=50)
	phone=models.CharField(max_length=20)
	message=models.TextField(max_length=1000)
	def __str__(self):
		return str(self.name)

class Myaddress(models.Model):
	city=models.CharField(max_length=50)
	street=models.CharField(max_length=50)
	telephone=models.CharField(max_length=20)
	email=models.CharField(max_length=50)
	def __str__(self):
		return str("Adres firmy")