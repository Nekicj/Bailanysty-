from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('follow/<str:username>/', views.follow_user, name='follow_user'),
    path('unfollow/<str:username>/', views.unfollow_user, name='unfollow_user'),
    path('toggle-follow/<str:username>/', views.toggle_follow, name='toggle_follow'),
    path('followers/<str:username>/', views.followers_list, name='followers'),
    path('following/<str:username>/', views.following_list, name='following'),
]
