from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('aboutus', views.aboutus, name='aboutus'),
	path('list', views.BooksList.as_view(), name='books_list'),
    path('new', views.BooksCreate.as_view(), name='books_new'),
    path('view/<int:pk>', views.BooksView.as_view(), name='books_view'),
    path('edit/<int:pk>', views.BooksUpdate.as_view(), name='books_edit'),
    path('delete/<int:pk>', views.BooksDelete.as_view(), name='books_confirm_delete'),
    path('show',views.showbooks,name='show_books'),
    path('search',views.search,name='search'),
    path('searchbox',views.searchbox,name='searchbox'),
]