from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from playerprofile.models import UserProfile, Rank

# Register your models here.

#USER PROFILE
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name='profil'
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
admin.site.register(Rank)