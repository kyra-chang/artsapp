from django import forms
from .models import Comment
from .models import Profile

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'photo', )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('year', 'major', 'age', 'gender',)