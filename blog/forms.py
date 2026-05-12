from django import forms

from blog.models import UserProfile, Post

"""
class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
"""


"""
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'content', 'published')
"""