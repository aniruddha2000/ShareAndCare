from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from shareandcare.foodpost import models

from .filters import PostFilter


@login_required(login_url='account:login')
def home_page_view(request, username):
    user = get_object_or_404(User, username=username)
    all_posts = models.FoodPost.objects.exclude(user=request.user.id)
    args = {
        'username': user,
        'filter_posts': PostFilter(request.GET, queryset=all_posts),
    }
    return render(request, 'homepage/homepage.html', args)

@login_required(login_url='account:login')
def home_page_post_view(request, post_id):
    args = {
        'username': request.user,
        'post': models.FoodPost.objects.get(id=post_id),
    }
    return render(request, 'homepage/homepage_posts.html', args)
