#from Django. urls import path
from django.urls import path
from .views import book_list
    
    #URL pattern maps the root URL /books/ to the book_list view
urlpatterns = [
    
        path('books/', book_list, name='book_list'),
        
       
        
]
