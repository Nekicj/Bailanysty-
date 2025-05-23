from django.db.models.signals import post_save
from django.dispatch import receiver


from posts.models import Comment, Like
from .models import Notification
from posts.models import Post
from users.models import CustomUser
from django.db.models.signals import post_save, m2m_changed

@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created and instance.author != instance.post.author:
        Notification.objects.create(
            user=instance.post.author,
            message=f"{instance.author.username} прокомментировал ваш пост",
            link=f"/post/{instance.post.id}/"
        )

#М2М ОЕС АРБУЗ
@receiver(m2m_changed, sender=Post.likes.through)
def create_like_notification(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":
        user = CustomUser.objects.get(pk=next(iter(pk_set)))
        # ОФАК 
        if user != instance.author:
            Notification.objects.create(
                user=instance.author,
                message=f"{user.username} лайкнул ваш пост",
                link=f"/post/{instance.id}/"
            )