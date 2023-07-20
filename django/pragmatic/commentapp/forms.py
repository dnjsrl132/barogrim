from django.forms import ModelForm
from commentapp.models import Comments

class CommentCreationForm(ModelForm):
    class Meta:
        model=Comments
        fields=['content']