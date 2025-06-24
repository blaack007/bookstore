from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html' 
    context_object_name = 'book_list'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html' 
    context_object_name = 'book'

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'description', 'categories', 'rate', 'views']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form) 

class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'description', 'categories', 'rate', 'views']

    def test_func(self):
        book = self.get_object()
        return self.request.user == book.user or self.request.user.is_superuser

class SignUpView(FormView):
    template_name = 'registration/signup.html' 
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')

    def test_func(self):
        book = self.get_object()
        return self.request.user == book.user or self.request.user.is_superuser
