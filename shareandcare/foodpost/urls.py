from django.conf import settings
from django.urls import path

from . import views

app_name = 'foodpost'
urlpatterns = [
    path('my-posts', views.my_post_view, name='mypost'),
    path('add-posts', views.add_post_view, name='addpost'),
    path('my-posts/<int:post_id>', views.my_post_detail_view, name='myPostDetail'),
    path('my-posts/<int:post_id>/edit', views.edit_post_view, name='editPost'),
    path('my-posts/<int:post_id>/delete', views.delete_post_view, name='deletePost'),
]
