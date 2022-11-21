from django.shortcuts import render
from book_service.models import Book
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request,'book_service/home.html')

def all_books(request):
    books=Book.objects.all()
    if request.method=="POST":
        book_name=request.POST.get("book_name","")
        books=Book.objects.filter(title__contains=book_name)
    numOfbooks=books.count()
    
    return render(request,"book_service/all_books.html",{"books":books , "numOfbooks":numOfbooks})

