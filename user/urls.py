from django.urls import path
from . import views as v

urlpatterns = [
    path('create/', v.createUser),
    path('login/', v.login),
    path('retrieve/', v.retrievePassword),
    path('searchbook/', v.userBook),
    path('addbook', v.addBook),


]


