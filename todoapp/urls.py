from django.urls import path 
from .views import *

urlpatterns = [
    path('', home, name='home_view'),
    path('about/', about, name='about_view'),
    path('edit/<pk>', edit, name='edit_view'),
    path('delete/<pk>', delete, name='delete_view')
]
