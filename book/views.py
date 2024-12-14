from django.shortcuts import render
from .models import Books
from django.views.generic import CreateView, ListView
from .forms import AddBookForm


class BookList(ListView):
    model = Books
    template_name = 'index.html'
    context_object_name = 'books' 



class BookCreate(CreateView):
    model = Books
    template_name = 'book_list.html'
    form_class = AddBookForm  # Form for adding a new book
    success_url = '/'  # Redirect after successful form submission


