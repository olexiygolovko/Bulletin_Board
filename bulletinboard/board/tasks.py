from django.contrib.auth.models import User
from django.core.mail import send_mail
from datetime import timedelta
from django.utils import timezone
from celery import shared_task

from .models import Post, Response


@shared_task
def respond_send_email(respond_id):
    respond = Response.objects.get(id=respond_id)
    send_mail(
        subject=f'MMORPG Billboard: new response to ad!',
        message=f'Good day, {respond.post.author}, ! There is a new response to your ad!\n'
                f'Read the response:\nhttp://127.0.0.1:8000/responses/{respond.post.id}',
        from_email='olexiygolovko92@mail.ru',
        recipient_list=[respond.post.author.email, ],
    )


@shared_task
def respond_accept_send_email(response_id):
    respond = Response.objects.get(id=response_id)
    print(respond.post.author.email)
    send_mail(
        subject=f'MMORPG Billboard: Your response has been accepted!',
        message=f'Good day, {respond.author}, Author of the ad {respond.post.title} I accepted your response!\n'
                f'View accepted responses:\nhttp://127.0.0.1:8000/responses',
        from_email='olexiygolovko92@mail.ru',
        recipient_list=[respond.post.author.email, ],
    )


@shared_task
def send_mail_monday_8am():
    now = timezone.now()
    list_week_posts = list(Post.objects.filter(dateCreation__gte=now - timedelta(days=7)))
    if list_week_posts:
        for user in User.objects.filter():
            print(user)
            list_posts = ''
            for post in list_week_posts:
                list_posts += f'\n{post.title}\nhttp://127.0.0.1:8000/post/{post.id}'
            send_mail(
                subject=f'News Portal: posts from the past week.',
                message=f'Good day, {user.username}!\nWe invite you to familiarize yourself with new advertisements,'
                        f'appeared in the last 7 days:\n{list_posts}',
                from_email='olexiygolovko92@mail.ru',
                recipient_list=[user.email, ],
            )
