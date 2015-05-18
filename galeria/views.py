from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from galeria.models import Album, Photo
from galeria.forms import PhotoForm
# Create your views here.

class AlbumList(ListView):
    queryset = Album.objects.order_by('name').all()
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super(AlbumList, self).get_context_data(**kwargs)
        # context['random_pic'] = self.object_list
        return context


class PhotoList(ListView):
    paginate_by = 9
    model = Photo
    #dojebac context tak zeby miec dostep do albumu

    def get_context_data(self, **kwargs):
        context = super(PhotoList, self).get_context_data(**kwargs)
        #context['album'] = self.object_list.first().album
        context['album'] = Album.objects.filter(pk=self.kwargs['pk']).first()
        # print(self.kwargs['pk'])
        return context

    def get_queryset(self):
        qs = super(PhotoList, self).get_queryset()
        return qs.filter(album__pk=self.kwargs['pk'])

class PhotoDetail(DetailView):
    model = Photo



class PhotoCreate(CreateView):
    form_class = PhotoForm
    template_name ='galeria/photo_form.html'

    def get_success_url(self):
        return self.object.get_absolute_url()



class HomeView(TemplateView):
    template_name='home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['carousel_album'] = Album.objects.filter(name='homepage').first()
        print(Album.objects.filter(name='homepage').first())
        return context

