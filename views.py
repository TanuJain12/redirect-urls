from django.shortcuts import render, redirect
from .models import Book
from .forms import BookUploadForm

def my_books(request):
    user = request.user.id
    books = Book.objects.filter(uploaded_by=user)
    return render(request, 'my_books.html', {'books': books})


def upload_books(request):
    if request.method == 'POST':
        form = BookUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.uploaded_by = request.user
            form.save()
            return redirect('my_books')
    else:
        form = BookUploadForm()
    return render(request, 'upload_books.html', {'form': form})

    

def my_books_wrapper(request):
    user = request.user.id
    if Book.objects.filter(uploaded_by=user).exists():
        return redirect('my_books')
    else:
        return redirect('upload_books')
    

