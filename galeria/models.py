from django.db import models
from sorl.thumbnail import ImageField
from audit_log.models import AuthStampedModel
from django.core.urlresolvers import reverse, reverse_lazy

# Create your models here.

class Album(AuthStampedModel):
    name = models.CharField(max_length=100, verbose_name='nazwa')
    description = models.TextField(max_length=5000, blank=True, verbose_name='opis')


    class Meta:
        verbose_name = "album"
        verbose_name_plural = "albumy"
        ordering = ['-pk']

    def __str__(self):
        return self.name



class Photo(AuthStampedModel):
    name = models.CharField(max_length=100, verbose_name='nazwa')
    file = ImageField(upload_to='photos', blank=False, null=False)
    description = models.TextField(max_length=5000, blank=True, verbose_name='opis')
    album = models.ForeignKey(Album)

    class Meta:
        verbose_name = "zdjęcie"
        verbose_name_plural = "zdjęcia"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('photo_detail', kwargs={'pk':self.pk})

    