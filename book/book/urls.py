"""book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url

from book_management.views import BookRetrieveView, UpdateBookView, CreateBookView, DeleteBookView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^book/retrieve/(?P<id>[0-9]+)/?$', BookRetrieveView.as_view(), name='retrieve_book'),
    url(r'^book/update/(?P<id>[0-9]+)/?$', UpdateBookView.as_view(), name='update_book'),
    path('book/create/', CreateBookView.as_view(), name='create_book'),
    url(r'^book/delete/(?P<pk>\d+)/?$', DeleteBookView.as_view(), name='delete_book')
]
