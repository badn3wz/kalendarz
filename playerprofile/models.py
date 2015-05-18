from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from playerprofile.xmltest import generate_squadxml
from cal.models import Slot
from django.db.models import Count
# Create your models here.



PANEL_CLASSES = [
	('panel-warning', 'warning'),
	('panel-info', 'info'),
	('panel-success', 'success'),
	('panel-danger', 'danger'),
	('panel-primary', 'primary'),
	('panel-default', 'default')
]



class Rank(models.Model):
	name = models.CharField(max_length=30, blank=False, null=False, verbose_name='nazwa')
	importance = models.IntegerField(blank=False, null=False, verbose_name='waga', default=0)
	css_class = models.CharField(max_length=50, verbose_name='klasa css', blank=True, 
		choices=PANEL_CLASSES,
		default='panel-default')

	class Meta:
		verbose_name_plural='stopnie'
		verbose_name='stopień'
		ordering=['-importance']

	def __str__(self):
		return self.name



class UserProfile(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	send_mail = models.BooleanField(default = False)
	nick = models.CharField(max_length=30, blank=True, null=False, default='', verbose_name='nick profilu')
	rank = models.ForeignKey(Rank, verbose_name='stopień', null=True, blank=False, )
	player_id = models.CharField(blank=True, null=True, 
		default='', max_length=18, verbose_name='player ID',
		validators=[
        RegexValidator(
        	regex='^\d{17}$',
            message='Wpisano niepoprawny numer PID',
            code='niepoprawny PID'
        )])

	class Meta:
		verbose_name = "profil użytkownika"
		verbose_name_plural = "profile użytkowników"

	def __str__(self):
		return self.user.__str__()

	def mission_no(self):
		return self.user.entry_set.count()

	def slot_count(self):
		# qwe = self.user.entry_set
		# #top_slots = Slot.objects.annotate()
		# qwe_top = Slot.objects.annotate(times_played=Count('entry')).filter(entry__user=self.user)
		return ''



####mała funkcja

def get_default_rank():
	return Rank.objects.all().last()





####SIGNALS####

@receiver(post_save, sender=User)
def create_user_profile(sender, **kwargs):
	if kwargs.get('created', False):
		print(get_default_rank())
		up = UserProfile.objects.create(user=kwargs.get('instance'), rank=get_default_rank())		


@receiver(post_save, sender=UserProfile)
def rewrite_squadxml(sender, **kwargs):
	members = User.objects.filter(groups__name='Member')
	generate_squadxml(members)



from permission import add_permission_logic
from permission.logics import AuthorPermissionLogic
add_permission_logic(UserProfile, AuthorPermissionLogic(
	field_name='user',
	change_permission=True,
	delete_permission=False,
	))