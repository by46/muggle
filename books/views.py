from django.views import generic

from .models import Book


# Create your views here.

class BookIndex(generic.ListView):
    template_name = 'books/index.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all()


class BookDetails(generic.DetailView):
    model = Book
    template_name = 'books/details.html'
