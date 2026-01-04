from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_article, name='create_article'),
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('contact/', views.contact, name='contact'),
    path('like/<slug:slug>/', views.toggle_like, name='toggle_like'),
    path('<slug:slug>/', views.article_detail, name='article_detail'),
]
