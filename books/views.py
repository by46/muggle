from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import generic

from .forms import NameForm
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


def add_book(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/books/thanks")
    else:
        form = NameForm()
    return render(request, 'books/name.html', {'form': form})


def thanks(request):
    return HttpResponse("thanks!")
