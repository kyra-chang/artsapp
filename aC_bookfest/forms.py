from django import forms
from .models import Comment, Order
from .models import Profile

class DummyForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ()

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'photo', )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('year', 'major', 'age', )