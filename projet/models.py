from django.db import models
from django.utils.text import slugify
from blog.models import UserProfile


# Create your models here.

def get_default_user():
    return UserProfile.objects.first()


class Projet(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre", unique=True)
    slug = models.SlugField(max_length=200, verbose_name="Slug", unique=True)
    author = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, default=get_default_user, verbose_name="Auteur")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")
    date_last_modified = models.DateTimeField(auto_now=True, verbose_name="Modifie le")
    content = models.TextField(verbose_name="Contenu")
    link = models.URLField(verbose_name="Lien vers le projet", blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publié")

    class Meta:
        verbose_name = "Projet"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
