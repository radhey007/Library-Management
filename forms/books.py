from django import forms
from books.models import Categories

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name','active']