from django.http import Http404, HttpResponseRedirect
from django.views import generic

from .models import Book
from .forms import NameForm

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
            return HttpResponseRedirect("/thanks")
    else:
        form = NameForm()
    return Http404()

