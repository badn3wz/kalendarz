from django.shortcuts import render, redirect
from permission.decorators import permission_required
from playerprofile.models import UserProfile
from django.views.generic import UpdateView, DetailView, RedirectView, ListView
from playerprofile.forms import ProfileForm
from django.core.urlresolvers import reverse_lazy, reverse

# Create your views here.

class AuthorRequiredMixin(object):
	def dispatch(self, request, *args, **kwargs):
		obj = self.get_object()
		result = super(AuthorRequiredMixin, self).dispatch(request, *args, **kwargs)
		if self.object.user != self.request.user:
			return redirect('index')
		return result


# @permission_required('playerprofile.change_userprofile', raise_exception=True)
class ProfileUpdateView(AuthorRequiredMixin, UpdateView):
	model = UserProfile
	form_class = ProfileForm
	class Meta:
		exclude = ['user']

	def get_success_url(self):
		return reverse_lazy('view_profile', kwargs={'pk':self.object.user.pk})


class ProfileView(DetailView):
	model = UserProfile

class OwnProfileView(RedirectView):
	def get_redirect_url(self, *args, **kwargs):
		return reverse_lazy('view_profile', kwargs={'pk': self.request.user.pk})



class UserList(ListView):
	queryset = UserProfile.objects.all().order_by('rank', 'user__username')

class MemberList(ListView):
	queryset = UserProfile.objects.filter(rank__importance__gte=0).order_by('rank', 'user__username')

class OwnProfileUpdateView(RedirectView):
	def get_redirect_url(self, *args, **kwargs):
		return reverse_lazy('update_profile', kwargs={'pk': self.request.user.pk})
