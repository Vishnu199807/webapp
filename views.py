from django.shortcuts import render, get_object_or_404,redirect
from django.http import Http404
from django.views.generic import ListView
import json,requests,reverse
from django.contrib import admin
from .models import Book,Author,Category,Genre
from django.views.generic.edit import UpdateView
from .forms import BookForm
from .forms import AuthorForm
from django.views.generic.edit import CreateView
from django.core.management.base import BaseCommand




admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Author)
def home(request):
    return render(request, 'webapp/home.html')
def book_details():
    return None
def book_detail(request, book_id):

    try:
        with open('Book list.json') as file:
            book_list = json.load(file)
        book = next((b for b in book_list if b['id'] == book_id), None)
        if book:
            book = get_object_or_404(Book, id=book_id)
            return render(request, 'webapp/book_details.html', {'book': book})
        else:
            raise Http404("Book does not exist.")
    except FileNotFoundError:
        raise Http404("Book list file not found.")

def book_list(request):
    books = Book.objects.filter(is_available=True)
    return render(request, 'webapp/book_list.html', {'books': books})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'webapp/create_book.html', {'form': form})
def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book_id)
    else:
        form = BookForm(instance=book)

    return render(request, 'webapp/update_book.html', {'form': form, 'book': book})
from django.shortcuts import render, redirect


def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')  # Replace 'author_list' with the appropriate URL name for the author list
    else:
        form = AuthorForm()

    return render(request, 'webapp/create_author.html', {'form': form})



class UpdateBookView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/update_book.html'
    context_object_name = 'book'

    def get_success_url(self):
        return reverse('book_detail', kwargs={'book_id': self.object.id})

class AuthorListView(ListView):
    model = Author
    template_name = 'webapp/author_list.html'
    context_object_name = 'authors'

    def get_queryset(self):
        response = requests.get('http://random-data-api.com/api/v2/user?size=10')
        if response.status_code == 200:
            authors = response.json()
            return authors
        else:
            return []

class CreateAuthorView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'webapp/create_author.html'
    success_url = '/authors/'

class Command(BaseCommand):
    help = 'Print available books'

    def handle(self, *args, **options):
        books = Book.objects.filter(is_available=True)
        for book in books:
            self.stdout.write(book.title)