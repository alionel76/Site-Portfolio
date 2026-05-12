from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from blog.models import Post


class BlogHomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

class BlogCreateView(CreateView):
    model = Post
    fields = ('title', 'author', 'content', 'published')
    template_name = 'blog/create.html'
    success_url = reverse_lazy('blog-home')


class BlogDetailView(DetailView): #continuer ici
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'actual_post'


class BlogUpdateView(UpdateView):
    model = Post
    fields = ('title', 'author', 'content', 'published')
    template_name = 'blog/update.html'
    success_url = reverse_lazy('blog-home')

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog-home')
    context_object_name = 'actual_post'

