from django import forms
from cal.models import Entry, Event, Slot
from extra_views import InlineFormSet


class EntryForm(forms.ModelForm):
	#user = forms.ModelChoiceField()

	class Meta:
		model = Entry
		exclude = []
		widgets = {
			'slot': forms.HiddenInput(),
			'user': forms.HiddenInput(),
			'absence': forms.HiddenInput(),
		}


class SlotInline(InlineFormSet):
	model=Slot
	exclude = []
	extra=20
	max_num=25

class EventForm(forms.ModelForm):
	class Meta(object):
		exclude =[]
		model = Event
		