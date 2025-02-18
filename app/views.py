from django.shortcuts import render, get_object_or_404
from .models import Book
from django.views.generic import ListView,DetailView

#Changed to generic views to simplify the code
class BookListView(ListView):
    model = Book
    template_name = "app/book_list.html"
    context_object_name = "books"

class BookDetailView(DetailView):
    model = Book
    template_name = "app/book_detail.html"
    context_object_name = "book"
