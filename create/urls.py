from . import views
from django.urls import path

urlpatterns = [
    path('create', views.CreateView.as_view(), name='create'),
]
