from django import forms
from blog.models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        #feilds = '__all__'
        exclude = ('post','user')