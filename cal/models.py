from django.db import models
from django.conf import settings
from datetime import datetime, timedelta
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models.signals import post_save
from django.dispatch import receiver

#domyslny czas rozpoczecia eventu
def default_start_time():
    now = datetime.now()
    start = now.replace(hour=20, minute=0, second=0, microsecond=0)
    return start + timedelta(days=1)  

LIST_CLASSES = [
	('list-group-item-warning', 'warning'),
	('list-group-item-info', 'info'),
	('list-group-item-success', 'success'),
	('list-group-item-danger', 'danger'),
	('list-group-item-default', 'default'),
]

# Create your models here.

class EventType(models.Model):
	name = models.CharField(max_length=100, verbose_name='nazwa')
	css_class = models.CharField(max_length=50, verbose_name='klasa css', blank=True, 
		choices=LIST_CLASSES,
		default='')
	
	class Meta:
		verbose_name = 'typ wydarzenia'
		verbose_name_plural = 'Typy wydarzeń'

	def __str__(self):
		return self.name


class Terrain(models.Model):
	name = models.CharField(max_length=50, verbose_name='nazwa')
	pic = models.ImageField(upload_to='terrains', blank=True, null=True)
	is_active = models.BooleanField(default=True, verbose_name='aktywna')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'mapa'
		verbose_name_plural = 'mapy'

class Event(models.Model):
	title = models.CharField(max_length=200, verbose_name='tytuł')
	author = models.CharField(max_length=200, verbose_name='autor')
	datetime = models.DateTimeField(default=default_start_time, verbose_name='data i czas')
	type = models.ForeignKey(EventType, verbose_name='typ')
	#details = models.TextField(max_length=5000, blank=True, verbose_name='szczegóły')
	url = models.URLField(blank=True, verbose_name='Link')
	terrain = models.ForeignKey(Terrain, null=True, blank=True, verbose_name='Mapa')
	is_open = models.BooleanField(default=True, verbose_name='otwarte')
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, 
		verbose_name='stworzone przez', null=False,blank=False, editable=False)

	class Meta:
		verbose_name = 'wydarzenie'
		verbose_name_plural = 'wydarzenia'
		ordering = ['datetime']

	def __str__(self):
		return self.title

	def is_mission(self):
		return self.type.name=='Misja'

	def is_course(self):
		return self.type.name=='Szkolenie'

	def is_training(self):
		return self.type.name=='Trening'

	def is_campaign(self):
		return self.type.name=='Kampania'

	def date(self):
		return self.datetime.date()
	date.short_description = "data"

	def time(self):
		return self.datetime.time()
	time.short_description = "godzina"

	def slots_no(self):
		return self.slot_set.count()
	slots_no.short_description = "liczba slotów"

	def slots_taken(self):
		count = 0
		for slot in self.slot_set.all():
			if slot.is_taken():
				count+=1
		return count

	def has_open_slots(self):
		for slot in self.slot_set.all():
			if not slot.is_taken():
				return True
		return False

	def get_absolute_url(self):
		return reverse_lazy('detail', kwargs={'pk':self.pk})






class SlotType(models.Model):
	name = models.CharField(max_length=100, verbose_name='nazwa')
	translation = models.CharField(max_length=100, blank=True, null=False, default='', verbose_name='Tłumaczenie')
	description = models.TextField(max_length=5000, blank=True, verbose_name='Opis')
	
	class Meta:
		verbose_name = 'typ slotu'
		verbose_name_plural = 'typy slotów'
		ordering = ['pk']

	def __str__(self):
		return self.name




class Slot(models.Model):
	group_name = models.CharField(max_length=50, blank = True, verbose_name='nazwa grupy')
	type = models.ForeignKey(SlotType, verbose_name='typ')
	event = models.ForeignKey(Event, verbose_name='wydarzenie')
	order = models.IntegerField(default=0, max_length=20, verbose_name='kolejność')

	class Meta:
		verbose_name = 'slot'
		verbose_name_plural = 'sloty' 

	def __str__(self):
		return "[{0}] {1}".format(str(self.pk), self.type.name)

	def is_taken(self):
		try:
			return self.entry!=None
		except ObjectDoesNotExist:
			return False
	is_taken.boolean=True

	def event_datetime(self):
		return self.event.datetime
	event_datetime.short_description = "data i czas wydarzenia"

	#def reserved_by(self):
	#	return self.archive_set.first().user




class Entry(models.Model):
	slot = models.OneToOneField(Slot)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, verbose_name='użytkownik')
	absence = models.BooleanField(default=False, verbose_name='nieobecność')
	
	class Meta:
		verbose_name = 'zapis'
		verbose_name_plural = 'zapisy'

	def __str__(self):
		return "{0} | {1} - {2}".format(self.slot.event.title, self.user, self.slot)

	def mission(self):
		return self.slot.event.title
	mission.short_description = "Wydarzenie"

	def get_absolute_url(self):
		return reverse('detail', kwargs={'pk': self.slot.event.pk})



from permission import add_permission_logic
from permission.logics import AuthorPermissionLogic, GroupInPermissionLogic
add_permission_logic(Event, AuthorPermissionLogic(
	field_name='created_by',
	change_permission=True,
	delete_permission=False,
))
add_permission_logic(Event, GroupInPermissionLogic(
	group_names=['Administratorzy', 'Moderator'],
	any_permission=True,
	))
add_permission_logic(Event, GroupInPermissionLogic(
	group_names=['Member'],
	add_permission=False,
	change_permission=False,
	delete_permission=False,
	))
add_permission_logic(Entry, GroupInPermissionLogic(
	group_names=['Member'],
	add_permission=True,
	change_permission=False,
	delete_permission=False,
	))





######SIGNALS#########
# @receiver(post_save, sender=event)