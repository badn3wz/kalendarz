from django import forms
from galeria.models import Photo


class PhotoForm(forms.ModelForm):
	class Meta(object):
		exclude =[]
		model = Photo
