from django import forms
from django.forms import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import Message
from django.forms import ModelForm,Textarea,CharField
from django.core.validators import validate_email
#widgets = {'name': Textarea(attrs={'cols': 80, 'rows': 20}),}

# bierze pola z modelu
class ContactForm(ModelForm):
	class Meta:
		model=Message
		fields='__all__'
		widgets = {
			"name" : forms.TextInput(attrs={'placeholder':'Imię i Nazwisko','id':'name','class':'form-control m-2'}),
			"email" : forms.TextInput(attrs={'placeholder':'E-mail','id':'email','class':'form-control m-2'}),
			"phone" : forms.TextInput(attrs={'placeholder':'Telefon','id':'telefon','class':'form-control m-2'}),
			"message" : Textarea(attrs={'placeholder':'Wiadomość', 'rows': 4, 'class' : 'form-control m-2' }),
		}

		labels = {'name': _(''),
			'email' : _(''),
			'phone' : _(''),
			'message': _(''),
		}
		# validate empty input 1st level
		error_messages = {
			'name': { 'required' : _("Imię i Nazwisko jest wymagane!") },
			'email':{ 'required' : _("E-mail jest wymagany!") },
			'phone': { 'required' : _("Telefon jest wymagany!") },
			'message': { 'required' : _("Wiadomość jest wymagana!") },
		}

	# additional validation 2nd level
	def clean_name(self):
		""" Filed level validation - name """
		name_passed = self.cleaned_data.get("name")
		lenName = len(name_passed)
		if lenName <= 2:
			raise forms.ValidationError("Nazwisko musi mieć więcej niż 2 litery!")
		return name_passed

	def clean_email(self):
		email_passed = self.cleaned_data.get("email")
		try:
			validate_email(email_passed)
		except ValidationError:
			raise forms.ValidationError("Email nie jest poprawny!")
		return email_passed

	''' Clean - validate all form
		def clean(self):
			cleaned_data = super(ContactForm,self).clean()
			email_passed = cleaned_data.get("email")
			try:
				validate_email(email_passed)
			except ValidationError:
				raise forms.ValidationError("Email nie jest poprawny!")
			return email_passed
	'''
	# save overwrite
	"""old approach to save form

		form

	    class UrlForm(forms.Form):
	        url = forms.URLField(label='URL')
	        title = forms.CharField(label='Title')
	        nick = forms.CharField(label='Nick')


		from .models import Url
		def form_valid(self, form):

            title = self.request.POST.get('title')
            nick = self.request.POST.get('nick')
            url = self.request.POST.get('url')

            db_url = Url.create(url=url, title=title, nick=nick)
            db_url.save()
	"""