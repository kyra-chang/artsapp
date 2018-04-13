from django import forms
from .models import Comment, Order
from .models import Profile

class ConfirmForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('order_confirm',)

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