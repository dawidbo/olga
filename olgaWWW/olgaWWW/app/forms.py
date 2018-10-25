from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import Message

from django.forms import ModelForm,Textarea,CharField
#widgets = {'name': Textarea(attrs={'cols': 80, 'rows': 20}),}



class ContactForm(ModelForm):
	class Meta:
		model=Message
		fields='__all__'
		widgets = {
			"name" : forms.TextInput(attrs={'placeholder':'Imię i Nazwisko','id':'name','class':'form-control m-2'}),
			"email" : forms.TextInput(attrs={'placeholder':'E-mail','id':'email','class':'form-control m-2'}),
			"phone" : forms.TextInput(attrs={'placeholder':'Telefon','id':'telefon','class':'form-control m-2'}),
			"message" :Textarea(attrs={'placeholder':'Wiadomość', 'rows': 4, 'class' : 'form-control m-2' }),
		}

		labels = {'name': _(''),
			'email' : _(''),
			'phone' : _(''),
			'message': _(''),
		}
		#help_texts = {'name': _('Wpisz imię i nazwisko.')}
		error_messages = { 'name': { 'required' : _("This writer's name is too long.") } }

	'''
	def clean_name(self):
		""" Filed level validation """
		name_passed = self.cleaned_data.get("email")
		lenName = len(name_passed)
		if name_passed == 0:
			raise forms.ValidationError( "nie podano nazwiska" )
		return name_passed
	'''