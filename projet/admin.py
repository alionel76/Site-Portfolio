from django.contrib import admin
from projet.models import Projet

# Register your models here.

@admin.register(Projet)
class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'author', 'content', 'link', 'published',)
    list_display = ('title', 'slug', 'author', 'link', 'date_created', 'date_last_modified', 'published')
    list_editable = ('published', )
