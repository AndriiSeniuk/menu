from django.urls import path
from . import views

app_name = 'landing'

urlpatterns = [
    path('', views.menu_view, name='menu_list'),
]