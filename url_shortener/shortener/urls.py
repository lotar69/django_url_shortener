from shortener.views import index, create, go
from django.urls import path

urlpatterns = [
    path('', index, name="index"),
    path('create', create, name="index"),
    path('<str:pk>', go, name="go")
]