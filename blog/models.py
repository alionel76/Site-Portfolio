from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

class UserProfile(AbstractUser):
    class Meta:
        verbose_name = "Profils Utilisateur"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Create your models here.

def get_default_user():
    return UserProfile.objects.first()


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre", unique=True)
    slug = models.SlugField(max_length=200, verbose_name="Slug", unique=True)
    author = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, default=get_default_user, verbose_name="Auteur")
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)
    content = models.TextField(verbose_name="Contenu")
    published = models.BooleanField(default=False, verbose_name="Publié")

    class Meta:
        verbose_name = "Articles de Blog"

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
