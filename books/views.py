from django.shortcuts import render, render_to_response
from .models import Books
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import CreateForm
from django.views.generic import CreateView, ListView, DetailView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings
from django.contrib import messages
from django.template import Context

def index(request):
    if request.user.is_authenticated:
        return render(request,'books/index.html')
    else:
        return render_to_response('books/index.html')

def aboutus(request):
    if request.user.is_authenticated:
        return render(request,'books/aboutUs.html')
    else:
        return render_to_response('books/aboutUs.html')

def search(request):
    if request.user.is_authenticated:
        query_results = Books.objects.all().filter(genre__iexact = request.GET.get('g', '')).exclude(user_id = request.user.id)
    else:
        query_results = Books.objects.all().filter(genre__iexact = request.GET.get('g', ''))
    return render(request,'books/books_view.html',{'query_results':query_results})

def searchbox(request):
    if request.user.is_authenticated:
        query_results = Books.objects.all().filter(name__iexact = request.GET.get('key', '')).exclude(user_id = request.user.id)
    else:
        query_results = Books.objects.all().filter(name__iexact = request.GET.get('key', ''))
    return render(request,'books/books_view.html',{'query_results':query_results})

class BooksCreate(CreateView):
    form_class = CreateForm
    model = Books
    success_url = reverse_lazy('books_list')

    def get_form_kwargs(self):
        kwargs = super(BooksCreate, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

@method_decorator(login_required, name='dispatch')    
class BooksList(ListView):
    model = Books
    context_object_name ='books'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BooksList, self).dispatch(*args, **kwargs)

def showbooks(request):
    if request.user.is_authenticated:
        query_results=Books.objects.all().exclude(user_id=request.user.id)
    else:
         query_results=Books.objects.all()
    return render(request, 'books/books_view.html',{'query_results':query_results})

class BooksView(DetailView):
    model = Books
    context_object_name ='books'

class BooksUpdate(UpdateView):
    model = Books
    fields =  ['name', 'image', 'price', 'author', 'genre', 'isbn', 'edition', 'publisher', 'publishyear']
    success_url = reverse_lazy('books_list')

class BooksDelete(DeleteView):
    model = Books
    success_url = reverse_lazy('books_list')