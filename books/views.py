from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html' 
    context_object_name = 'book_list'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html' 
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'description', 'rate', 'views'] 

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'description', 'rate', 'views'] 

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
