from django.contrib import admin
from galeria.models import Album, Photo
# Register your models here.
from sorl.thumbnail.admin import AdminImageMixin

# class PhotoAdmin(AdminImageMixin, admin.ModelAdmin):
#     pass


admin.site.register(Album)
admin.site.register(Photo)