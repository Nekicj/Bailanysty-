from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from posts import views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.feed, name='feed'),
    path('create-post/', views.create_post, name='create_post'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('accounts/signup/', user_views.signup, name='signup'), 
    path('edit-profile/', user_views.edit_profile, name='edit_profile'), 

    path('users/', include('users.urls')),
    path('', include('posts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('notifications/', include('notifications.urls')),
    
    path('toggle-follow/<str:username>/', user_views.toggle_follow, name='toggle_follow'),
    path('followers/<str:username>/', user_views.followers_list, name='followers'),
    path('following/<str:username>/', user_views.following_list, name='following'),
    path('toggle-theme/', user_views.toggle_theme, name='toggle_theme'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)