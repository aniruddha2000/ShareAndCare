from django.urls import path
from . import views
from django.conf import settings


app_name = 'homepage'
urlpatterns = [
    path('home/<username>', views.home_page_view, name='home'),
]
