from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new_user', views.new_user),
    path('user_login', views.user_login),
    path('success', views.success),
    path('success/logout', views.logout),
]