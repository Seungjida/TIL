from django import forms
from .models import Author, Book

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ('author',)