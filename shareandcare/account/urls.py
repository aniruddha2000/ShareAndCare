from django.urls import path
from . import views
from django.conf import settings


app_name = 'account'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('login', views.login_view, name='login'),
    path('signup', views.signup_view, name='signup'),
]
