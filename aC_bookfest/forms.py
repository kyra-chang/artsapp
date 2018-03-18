from django import forms
from .models import Document
from .models import Profile

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('year', 'major', 'age', 'gender',)