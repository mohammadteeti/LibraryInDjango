
from django.urls import path ,include
from .views import home,all_books
urlpatterns = [
    path('',home,name='home'),
    path('all_books/',all_books,name='all_books')
    
]
