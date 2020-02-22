from django.contrib import admin
from django.urls import path, reverse_lazy
from .views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many, BooksOnHandEdit, BooksOnHandList, RegisterView, CreateUserProfile 
from django.contrib.auth.views import LoginView, LogoutView 
from allauth.account.views import login, logout
from allauth.socialaccount.models import SocialAccount     

app_name = 'p_library'
urlpatterns = [
    path('author/create', AuthorEdit.as_view(), name='author_create'),
    path('authors', AuthorList.as_view(), name='author_list'),
    path('author/create_many', author_create_many, name='author_create_many'),
    path('author_books/create_many', books_authors_create_many, name='author_book_create_many'),
    path('friends/create', BooksOnHandEdit.as_view(), name='friend_create'),  
    path('friends', BooksOnHandList.as_view(), name='friends_list'),
    path('login/', login, name='login'),  
    path('logout/', logout, name='logout'),  
    path('register/', RegisterView.as_view(  
        template_name='register_account.html',  
		success_url=reverse_lazy('p_library:base')  
    ), name='register'),
]
