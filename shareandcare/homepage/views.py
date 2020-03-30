from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from shareandcare.foodpost import models


@login_required(login_url='account:login')
def home_page_view(request, username):
    user = get_object_or_404(User, username=username)
    args = {
        'username': user,
        'all_posts': models.FoodPost.objects.exclude(user=request.user),
    }
    return render(request, 'homepage/homepage.html', args)
