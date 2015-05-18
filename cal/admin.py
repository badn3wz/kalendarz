from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from cal.models import Event, EventType, Slot, SlotType, Entry, Terrain
# Register your models here.


class SlotInLine(admin.TabularInline):
	model = Slot
	extra = 0

class SlotAdmin(admin.ModelAdmin):
	list_display = ('type', 'pk', 'event', 'event_datetime', 'group_name', 'is_taken')

class EventAdmin(admin.ModelAdmin):
	model = Event
	inlines = [SlotInLine]
	ordering = ['-datetime']
	list_display = ('title', 'pk', 'terrain', 'created_by', 'date', 'time', 'is_open', 'slots_no')
	def save_model(self, request, obj, form, change):
		obj.created_by = request.user
		obj.save()

class EntryAdmin(admin.ModelAdmin):
	list_display = ('pk', 'mission', 'slot', 'user')



admin.site.register(Terrain)
admin.site.register(Entry, EntryAdmin)
admin.site.register(EventType)
admin.site.register(Event, EventAdmin)
admin.site.register(Slot, SlotAdmin)
admin.site.register(SlotType)
#admin.site.register(Archive)


