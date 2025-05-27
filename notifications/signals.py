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

#М2М АРБУЗ NE POST_SAVE FUU 
@receiver(m2m_changed, sender=Post.likes.through) 
def create_like_notification(sender, instance, action, pk_set, **kwargs): #instance - whose post was liked

    #if action == "post_add":
    #    for user_id in pk_set:
    #        user = CustomUser.objects.get(pk=user_id)
    #        if user != instance.author:
    #            Notification.objects.create(
    #            user=instance.author,
    #            message=f"{user.username} лайкнул ваш пост",
    #            link=f"/post/{instance.id}/"
    #        )

    if action == "post_add":
        user = CustomUser.objects.get(pk=next(iter(pk_set))) # первый id из множества
        # ОФК 
        if user != instance.author:
            Notification.objects.create(
                user=instance.author,
                message=f"{user.username} лайкнул ваш пост",
                link=f"/post/{instance.id}/"
            )