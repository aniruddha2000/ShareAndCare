from django.conf import settings
from django.urls import path

from . import views

app_name = 'homepage'
urlpatterns = [
    path('<username>', views.home_page_view, name='home'),
    path('post/<int:post_id>', views.home_page_post_view, name='homePostView'),
]
