from django import forms
from .models import Book, Author
from django.utils import timezone


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

    def clean_birthdate(self):
        birthdate = self.cleaned_data.get('birthdate')
        if birthdate and birthdate > timezone.now().date():
            raise forms.ValidationError("Birthdate cannot be in the future.")
        return birthdate
