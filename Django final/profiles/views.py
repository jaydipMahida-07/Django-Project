from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from .models import Profile

def profile_detail(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    profile = user.profile
    articles = user.articles.filter(is_published=True).order_by('-created_at')
    
    context = {
        'profile_user': user,
        'profile': profile,
        'articles': articles,
    }
    return render(request, 'profiles/profile_detail.html', context)
