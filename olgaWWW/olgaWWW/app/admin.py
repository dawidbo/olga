from django.contrib import admin
from .models import Sites, Section, Articles,Price,Message,Myaddress

# Register your models here.
# admin.site.register(Sites)

@admin.register(Sites)
class SitesEdit(admin.ModelAdmin):
	list_display = ('id','tabs','creator','createDate')
	list_editable = ('tabs',)


@admin.register(Section)
class SitesEdit(admin.ModelAdmin):
	list_display = ('id','title', 'sites', 'creator','createDate')
	list_editable = ('title',)

@admin.register(Articles)
class ArticlesEdit(admin.ModelAdmin):
	list_display = ('id','content','section', 'description','active','creator')
	list_editable = ('content',)

@admin.register(Price)
class PriceEdit(admin.ModelAdmin):
	list_display = ('id','service','price')
	list_editable = ('service','price')

@admin.register(Message)
class ContactEdit(admin.ModelAdmin):
	list_display = ('id','name','message','email','phone')

@admin.register(Myaddress)
class MyaddressEdit(admin.ModelAdmin):
	list_display=('id','city','street','telephone','email')
	list_editable=('city','street','telephone','email')