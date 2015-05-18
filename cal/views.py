from braces.views import LoginRequiredMixin, GroupRequiredMixin
from cal.forms import EntryForm, SlotInline, EventForm
from cal.models import Event, Slot, Entry
from datetime import datetime, timedelta
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse_lazy, reverse
from django.db.models import Count
from django.forms import HiddenInput
from django.forms.formsets import all_valid
from django.forms.models import modelform_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, FormView, TemplateView, RedirectView
from django.views.generic.dates import MonthArchiveView
from extra_views import CreateWithInlinesView, UpdateWithInlinesView
from permission.decorators import permission_required
#mixins:

class AuthorRequiredMixin(object):
	def dispatch(self, request, *args, **kwargs):
		obj = self.get_object()
		result = super(AuthorRequiredMixin, self).dispatch(request, *args, **kwargs)
		if self.object.user != self.request.user:
			return redirect(obj)
		return result

class EventAuthorRequiredMixin(object):
	def dispatch(self, request, *args, **kwargs):
		obj = self.get_object()
		result = super(EventAuthorRequiredMixin, self).dispatch(request, *args, **kwargs)
		if self.object.created_by != self.request.user:
			return redirect(obj)
		return result

class EventGroupRequiredMixin(object):
	def dispatch(self, request, *args, **kwargs):
		result = super(EventGroupRequiredMixin, self).dispatch(request, *args, **kwargs)
		if self.request.user.groups.filter(name='Member').exists() or self.request.user.groups.filter(name='Admin').exists():
			return result
		return reverse_lazy('index')


# Create your views here.


class EventList(ListView):
	queryset= Event.objects.order_by('datetime').filter(is_open=True)




class EventDetail(LoginRequiredMixin, DetailView):
	model = Event

	def is_member(self):
		return self.request.user.groups.filter(name='Member').exists()

	def loggedin_user_entry(self):
		for slot in self.object.slot_set.all():
			try:
				slot_user = slot.entry.user
			except ObjectDoesNotExist:
				slot_user = None
			if slot_user == self.request.user:
				return slot.entry
		return False


	def is_signed_up(self):
		for slot in self.object.slot_set.all():
			try:
				slot_user = slot.entry.user
			except ObjectDoesNotExist:
				slot_user = None
			if slot_user == self.request.user:
				return True
		return False

	def can_quit(self):
		if self.is_member() and (timezone.now() + timedelta(days=1) < self.object.datetime):
			return True
		return False

	def can_switch(self):
		if self.is_member() and (timezone.now() + timedelta(seconds = 600) <= self.object.datetime):
			return True
		return False

	def is_logged_in(self, slot_usr):
		if slot_usr == self.request.user:
			return True
		return False

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(EventDetail, self).get_context_data(**kwargs)
		context['slot_list'] = self.object.slot_set.order_by('group_name', 'order', 'type')
		context['is_signed_up'] = self.is_signed_up()
		context['loggedin_user_entry'] = self.loggedin_user_entry()
		context['can_quit'] = self.can_quit()
		context['can_switch'] = self.can_switch()
		context['is_member'] = self.is_member()
		try:
			context['terrain_pic'] = self.object.terrain.pic.url
		except:
			pass
		return context




class EntryUpdate(AuthorRequiredMixin, UpdateView):
	model = Entry
	exclude = []
	form_class =  EntryForm

	def dispatch(self, request, *args, **kwargs):
		#dostep tylko dla zapisanego usera
		obj = self.get_object()
		if obj.user != self.request.user:
			return redirect(obj)
		return super(EntryUpdate, self).dispatch(request, *args, **kwargs)

	def get_initial(self):
		to_id = self.kwargs['to_id']
		self.initial.update({'user': self.request.user, 
							'slot': Slot.objects.get(pk=to_id)})
		return super(EntryUpdate, self).get_initial()

	def get_context_data(self, **kwargs):
		context = super(EntryUpdate, self).get_context_data(**kwargs)
		context['nowy_slot'] = Slot.objects.get(pk=self.kwargs['to_id'])
		return context


class EntryDelete(AuthorRequiredMixin, DeleteView):
	model = Entry
	#success_url = reverse_lazy('index', )

	def get_success_url(self):
		return reverse('detail', kwargs={'pk': self.object.slot.event.pk})



@permission_required('cal.add_entry', raise_exception=True)
class EntryCreate(LoginRequiredMixin, FormView):
	template_name= 'cal/entry_create.html'
	form_class = EntryForm

	def get_initial(self):
		to_id = self.kwargs['to_id']
		self.initial.update({'user': self.request.user, 
							'slot': Slot.objects.get(pk=to_id)})
		return super(EntryCreate, self).get_initial()

	def get_context_data(self, **kwargs):
		context = super(EntryCreate, self).get_context_data(**kwargs)
		context['slot'] = Slot.objects.get(pk=self.kwargs['to_id'])
		return context

	def form_valid(self, form):
		form.save()
		return redirect('detail', pk=Slot.objects.get(pk=self.kwargs['to_id']).event.pk)

	success_url = reverse_lazy('detail', )




def home(request):
	return render(request, 'home.html')








####ZOSTAWIC NA POZNIEJ DO ZROBIENIA WIDOKU KALENDARZA
class MonthArchive(MonthArchiveView):
	queryset = Event.objects.all()
	date_field = 'datetime'
	make_object_list = True
	allow_future = True
####ZOSTAWIC NA POZNIEJ DO ZROBIENIA WIDOKU KALENDARZA





#@permission_required('cal.add_event', raise_exception=True)
class EventCreateView(GroupRequiredMixin, CreateWithInlinesView):
	group_required = u'Member'
	raise_exception = True
	model = Event
	slug_field = 'event_id'
	class Meta:
		exclude = []
	inlines = [SlotInline]



	def forms_valid(self, form, inlines):
		form.instance.created_by = self.request.user
		return super(EventCreateView, self).forms_valid(form, inlines)

	
	# def get_success_url(self):
	# 	return self.object.get_absolute_url()

####trzeba sprobowac z samym initial, wrzucic form.created_by,
####dodac czas utworzenia



@permission_required('cal.change_event', raise_exception=True)
class EventUpdateView(UpdateWithInlinesView):
	model = Event
	form_class = EventForm
	class Meta:
		exclude = []
	inlines = [SlotInline]


	def get_success_url(self):
		return self.object.get_absolute_url()



class Archive(RedirectView):
	#url = reverse('archive_month')
	# pattern_name = 'archive_month'
	def get_redirect_url(self, *args, **kwargs):
		year = datetime.now().strftime('%Y')
		month = datetime.now().strftime('%m')
		return reverse_lazy('archive_month', kwargs={'year':year, 'month':month})


