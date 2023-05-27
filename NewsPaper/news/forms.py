from django import forms
from .models import Post
from django.core.exceptions import ValidationError
class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = [
           'post_author',
           'post_category',
           'title',
           'content',
           'post_rate'
       ]

   def clean(self):
       cleaned_data = super().clean()
       content = cleaned_data.get("content")
       title = cleaned_data.get("title")

       if title == content:
           raise ValidationError(
               "Описание не должно быть идентично названию."
           )

       return cleaned_data