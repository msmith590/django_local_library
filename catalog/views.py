from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # Generate counts of Genres that 'History' in the name
    num_genre_history = Genre.objects.filter(name__icontains='history').count()

    # Generate counts of Books that contain 'Adventure' in the title
    num_books_adventure = Book.objects.filter(title__icontains='adventure').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genre_history': num_genre_history,
        'num_books_adventure': num_books_adventure,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
