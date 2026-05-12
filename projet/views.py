from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from projet.models import Projet


# Create your views here.

class ProjetHomeView(ListView):
    model = Projet
    template_name = 'projet/index.html'
    context_object_name = 'projets'

class ProjetCreateView(CreateView):
    model = Projet
    fields = ('title', 'author', 'content', 'link', 'published')
    template_name = 'projet/create.html'
    success_url = reverse_lazy('projet-home')


class ProjetDetailView(DetailView): #continuer ici
    model = Projet
    template_name = 'projet/detail.html'
    context_object_name = 'actual_projet'


class ProjetUpdateView(UpdateView):
    model = Projet
    fields = ('title', 'author', 'content', 'link', 'published')
    template_name = 'projet/update.html'
    success_url = reverse_lazy('projet-home')

class ProjetDeleteView(DeleteView):
    model = Projet
    template_name = 'projet/delete.html'
    success_url = reverse_lazy('projet-home')
    context_object_name = 'actual_projet'

