from django.urls import path
from . import views

app_name = 'quotes_app'

urlpatterns = [
    path('', views.main, name='main'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('add_tag/', views.add_tag, name='add_tag'),
    path('author_info/<int:author_id>', views.author_info, name='author_info'),
]