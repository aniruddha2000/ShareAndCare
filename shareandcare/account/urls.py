from django.conf import settings
from django.urls import path

from . import views

app_name = 'account'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('login', views.login_view, name='login'),
    path('signup', views.signup_view, name='signup'),
    path('logout', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit', views.edit_profile_view, name='edit_profile'),
    path('profile/password&update', views.update_password_view, name='update_password'),
]
