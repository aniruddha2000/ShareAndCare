from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models


@login_required(login_url='account:login')
def my_post_view(request):
    context = {
        'my_posts': models.FoodPost.objects.filter(user=request.user),
        'username': request.user
    }
    return render(request, 'foodpost/my_posts.html', context)
