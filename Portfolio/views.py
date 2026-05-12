from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from Portfolio import forms


class HomeView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ServiceView(TemplateView):
    template_name = 'services.html'

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = forms.ContactForm
    success_url = reverse_lazy('home')



