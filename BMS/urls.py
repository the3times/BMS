"""BMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.LoginView.as_view(), name='login'),
    url(r'^logout/', views.logout, name='logout'),

    url(r'^$', views.index, name='index'),
    url(r'^book_list/', views.book_list, name='book_list'),
    url(r'^book_add/', views.BookAdd.as_view(), name='book_add'),
    url(r'^book_edit/(\d+)/', views.book_edit, name='book_edit'),
    url(r'^book_delete/', views.book_delete, name='book_delete'),

    url(r'^author_list/', views.author_list, name='author_list'),
    url(r'^author_add/', views.author_add, name='author_add'),
    url(r'^author_edit/(\d+)/', views.author_edit, name='author_edit'),
    url(r'^author_delete/', views.author_delete, name='author_delete'),
]
