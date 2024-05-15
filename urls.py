from django.urls import path
from .views import my_books, upload_books, my_books_wrapper

urlpatterns = [
    path('my-books/', my_books, name='my_books'),
    path('upload-books/', upload_books, name='upload_books'),
    path('my-books-wrapper/', my_books_wrapper, name='my_books_wrapper'),
]
