from django.shortcuts import render, redirect
from .models import Book

def index(request):
    response = redirect('books/')
    return response

def books_view(request):
    books = Book.objects.all()
    template = 'books/books_list.html'
    context = {
        'books': [{
            'name': b.name,
            'author': b.author,
            'pub_date': b.pub_date.strftime('%Y-%m-%d'),
        } for b in books]
    }
    return render(request, template, context)

def books_by_date(request, pub_date):
    books = Book.objects.order_by('pub_date')
    template = 'books/books_by_date.html'
    context = {
        'books': [{
            'name': b['name'],
            'author': b['author'],
            'pub_date': b['pub_date'].strftime('%Y-%m-%d'),
        } for b in books]
    }
    return render(request, template, context)
