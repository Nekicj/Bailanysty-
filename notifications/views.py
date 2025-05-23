from django.shortcuts import render, get_object_or_404,redirect
from .models import Notification
from django.contrib.auth.decorators import login_required

@login_required
def notifications_list(request):
    notifications = request.user.notifications.all().order_by('-created_at')
    return render(request, 'notifications/list.html', {'notifications': notifications})

@login_required
def mark_as_read(request, pk):
    notification = get_object_or_404(Notification, pk=pk, user=request.user)
    notification.read = True
    notification.save()
    return redirect('notifications')