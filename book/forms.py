from django import forms
from .models import Books

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'  # Include all fields from the model
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter book title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 5, 
                'placeholder': 'Enter book description'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter author name'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter price'
            }),
            'publication_date': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date'
            }),
        }
