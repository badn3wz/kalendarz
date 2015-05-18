from django import template
from django.contrib.auth.models import Group
register = template.Library()

@register.assignment_tag
def compare_users(slot_user, request_user):
    if slot_user == request_user:
        return True
    return False

@register.filter
def in_group(user, group):

    if user.groups.filter(name=group):
        return True
    else:
        return False
