from django import forms
from .models import *

class AddNewThread(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title','full_text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'full_text': forms.Textarea(attrs={'class': 'no-resize', 'cols': 100, 'rows': 15}),
        }

class EditThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title','full_text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'full_text': forms.Textarea(attrs={'class': 'no-resize', 'cols': 100, 'rows': 15}),
        }

class AddNewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'parent_comment']
        widgets = {
            'text': forms.Textarea(attrs={'cols': 150, 'rows': 15}),
            'parent_comment': forms.HiddenInput(),
        }

class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'cols': 150, 'rows': 15}),
        }