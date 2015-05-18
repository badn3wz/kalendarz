from django import forms
from playerprofile.models import UserProfile

class ProfileForm(forms.ModelForm):
	class Meta(object):
		exclude =['user', 'rank']
		model = UserProfile
