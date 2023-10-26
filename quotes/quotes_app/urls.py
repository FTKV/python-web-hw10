from django.urls import path

from . import views


app_name = 'quotes_app'


urlpatterns = [
    path('', views.main, {"page_id": 1}, name='main'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('add_tag/', views.add_tag, name='add_tag'),
    path('author_info/<str:author_fullname_url>/', views.author_info, name='author_info'),
    path('tag/<str:tag_title>/', views.tag, {"page_id": 1}, name='tag'),
    path('top_tags/', views.top_tags, name='top_tags'),
    path('page/<int:page_id>/', views.main, name='main_'),
    path('tag/<str:tag_title>/page/<int:page_id>/', views.tag, name='tag_'),
]
