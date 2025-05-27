from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Post, Comment
from .forms import PostForm, CommentForm
from users.models import CustomUser
from django.db.models import Q

# --- Decorators
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


def feed(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/feed.html', {
        'posts': posts,
        'comment_form': CommentForm()
    })

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})




def profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    posts = Post.objects.filter(author=user).prefetch_related('comments').order_by('-created_at')
    return render(request, 'posts/profile.html', {
        'profile_user': user,
        'posts': posts
    })



@login_required
@require_POST
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id) 
    user = request.user
    liked = False

    if user.is_authenticated:
        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)
        else:
            post.likes.add(user)
            liked = True
        return JsonResponse({
            'likes_count': post.likes.count(),
            'liked': liked
        })
    return JsonResponse({'error': 'Not authenticated'}, status=403)

@login_required
@require_POST
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        content = request.POST.get('text')
        if content.strip():
            comment = Comment(post=post, author=request.user, text=content)
            comment.save()
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest': #fetch or xmlhttprequest javascript
                return JsonResponse({
                    'status': 'success',
                    'comment_id': comment.id,
                    'author': comment.author.username,
                    'text': comment.text,
                    'created_at': comment.created_at.strftime('%b. %d, %Y, %I:%M %p')
                })
        
    return redirect('profile', username=post.author.username)


def search_posts(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(
        Q(text__icontains=query) |
        Q(author__username__icontains=query)
    ).order_by('-created_at')
    return render(request, 'posts/search.html', {'posts': posts, 'query': query})





@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/edit_post.html', {'form': form})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST': #not ajax
        post.delete()
        return redirect('profile', username=request.user.username)
    return render(request, 'posts/confirm_delete.html', {'post': post})

