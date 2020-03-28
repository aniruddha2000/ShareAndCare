from django.urls import path
from . import views
from django.conf import settings


app_name = 'foodpost'
urlpatterns = [
    path('my-posts', views.my_post_view, name='mypost'),
]
