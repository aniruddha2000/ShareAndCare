from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from . import forms, models


@login_required(login_url='account:login')
def my_post_view(request):
    args = {
        'my_posts': models.FoodPost.objects.filter(user=request.user),
        'username': request.user
    }
    return render(request, 'foodpost/my_posts.html', args)

@login_required(login_url='account:login')
def add_post_view(request):
    form = forms.FoodPostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('foodpost:mypost')
    args = {
        'form': form,
        'username': request.user
    }
    return render(request, 'foodpost/add_post.html', args)
