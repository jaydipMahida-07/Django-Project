from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Category, Comment

def home(request):
    featured_articles = Article.objects.filter(is_published=True).order_by('-views')[:3]
    latest_articles = Article.objects.filter(is_published=True).order_by('-created_at')[:6]
    trending_articles = Article.objects.filter(is_published=True).order_by('-views')[:5]
    
    context = {
        'featured_articles': featured_articles,
        'latest_articles': latest_articles,
        'trending_articles': trending_articles,
    }
    return render(request, 'blog/home.html', context)

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, is_published=True)
    
    # Simple view counter
    article.views += 1
    article.save()
    
    context = {
        'article': article,
    }
    return render(request, 'blog/article_detail.html', context)

@login_required
def create_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        # Handle simple image upload if provided
        image = request.FILES.get('image')
        
        if title and content:
            article = Article.objects.create(
                author=request.user,
                title=title,
                content=content,
                image=image,
                is_published=True # Auto-publish for simplicity
            )
            return redirect('blog:article_detail', slug=article.slug)
    
    return render(request, 'blog/create_article.html')

def about(request):
    return render(request, 'blog/about.html')

def privacy(request):
    return render(request, 'blog/privacy.html')

def terms(request):
    return render(request, 'blog/terms.html')

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import json

def contact(request):
    return render(request, 'blog/contact.html')

@login_required
def toggle_like(request, slug):
    if request.method == 'POST':
        article = get_object_or_404(Article, slug=slug)
        user = request.user
        
        if user in article.likes.all():
            article.likes.remove(user)
            liked = False
        else:
            article.likes.add(user)
            liked = True
            
        return JsonResponse({
            'liked': liked,
            'count': article.likes.count()
        })
    return JsonResponse({'error': 'Invalid request'}, status=400)
