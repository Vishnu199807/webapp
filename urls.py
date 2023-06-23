"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
app_name = 'webapp'

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.home, name='home'),
    path('book/<str:book_id>/',views.book_details, name='book_details'),
    path('author-list/', views.AuthorListView.as_view(), name='author_list'),
    path('books/',views. book_list, name='book_list'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/<int:book_id>/',views. book_detail, name='book_detail'),
    path('books/<int:book_id>/update/',views. update_book, name='update_book'),
    path('authors/',views. AuthorListView.as_view(), name='author_list'),
    path('authors/create/',views.create_author, name='create_author'),
]














