from django.shortcuts import render
from book_service.models import Book
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request,'book_service/home.html')

def all_books(request):
    books=Book.objects.all()
    numOfbooks=books.count()
    
    return render(request,"book_service/all_books.html",{"books":books , "numOfbooks":numOfbooks})

