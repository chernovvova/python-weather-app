from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import LoginUser, RegisterUser


app_name = 'users'

urlpatterns = [
    path('signin/', LoginUser.as_view(), name='signin'),
    path('signup/', RegisterUser.as_view(), name='signup'),
    path('signout/', LogoutView.as_view(), name='signout'),
]