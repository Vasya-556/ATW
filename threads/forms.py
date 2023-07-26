from django import forms
from .models import *
# class AddNewThread(forms.Form):
#     title = forms.CharField(max_length=250)
#     full_text = forms.CharField(widget=forms.Textarea(attrs={'cols': 150, 'rows': 15}))

class AddNewThread(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title','full_text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'full_text': forms.Textarea(attrs={'cols': 150, 'rows': 15}),
        }