from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Response

@receiver(post_save, sender = Response)
def new_comment_notify(sender, instance, created, **kwargs):
    if created:
        email_list = [instance.post.author.email,]

        send_mail(
            subject=f"New comment to your post \"{instance.post.title}\" | {instance.post.data}",
            message=f'{instance.author.username} commented on your post \"{instance.post.title}\". Let\'s check',
            from_email='olexiygolovko92@mail.ru',
            recipient_list=email_list
        )

@receiver(post_save, sender = Response)
def comment_accepted_notify(sender, instance, created, **kwargs):
    if not created and instance.accepted == True:
        email_list = [instance.author.email,]

        send_mail(
            subject=f"{instance.post.author.username} accepted your comment \"{instance.text}\"",
            message=f"{instance.post.author.username} accepted your comment \"{instance.text}\"",
            from_email='olexiygolovko92@mail.ru',
            recipient_list=email_list
        )
