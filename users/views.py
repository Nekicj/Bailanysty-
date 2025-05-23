from django.shortcuts import render,redirect,get_object_or_404
from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import Follow,CustomUser


from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(CustomUser, username=username)
    Follow.objects.get_or_create(follower=request.user, followed=user_to_follow)
    return redirect('profile', username=username)

@login_required
def unfollow_user(request, username):
    Follow.objects.filter(follower=request.user, followed__username=username).delete()
    return redirect('profile', username=username)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form})


@login_required
def toggle_follow(request, username):
    user_to_toggle = get_object_or_404(CustomUser, username=username)
    
    if request.user in user_to_toggle.followers.all():
        Follow.objects.filter(follower=request.user, followed=user_to_toggle).delete()
    else:
        Follow.objects.get_or_create(follower=request.user, followed=user_to_toggle)
    
    return redirect('profile', username=username)

@login_required
def followers_list(request, username):
    user = get_object_or_404(CustomUser, username=username)
    followers = user.followers.all()
    return render(request, 'users/followers.html', {
        'profile_user': user,
        'users': followers
    })

@login_required
def following_list(request, username):
    user = get_object_or_404(CustomUser, username=username)
    following = user.following.all()
    return render(request, 'users/following.html', {
        'profile_user': user,
        'users': following
    })

@login_required
def toggle_theme(request):
    """Toggle between light and dark theme for the user."""
    user = request.user
    user.theme = 'dark' if user.theme == 'light' else 'light'
    user.save()
    
    return redirect(request.META.get('HTTP_REFERER', 'feed'))
