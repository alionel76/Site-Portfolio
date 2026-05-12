from django.contrib import admin
from blog.models import UserProfile, Post

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'username', 'email', 'is_staff', 'is_active', 'is_superuser')
    list_display = ('first_name', 'last_name', 'username', 'email', 'is_staff', 'is_active', 'is_superuser')
    list_editable = ('is_staff', 'is_active', 'is_superuser')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'author', 'content', 'published',)
    list_display = ('title', 'slug', 'author', 'date_created', 'date_last_modified', 'published')
    list_editable = ('published', )
