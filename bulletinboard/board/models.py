from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    CAT = (('tanks', 'Tanks'),
           ('healers', 'Khila'),
           ('damage_dealers', 'DD'),
           ('dealers', 'Merchants'),
           ('gildmasters', 'Guildmasters'),
           ('quest_givers', 'Questgivers'),
           ('blacksmiths', 'Blacksmiths'),
           ('tanners', 'Tanners'),
           ('potion_makers', 'Potions brewers'),
           ('spell_masters', 'Spell Masters'))
    category = models.CharField(max_length=15, choices=CAT, verbose_name='Category')
    dateCreation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, verbose_name='Name')
    text = RichTextField()


class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Text')
    status = models.BooleanField(default=False)
    dateCreation = models.DateTimeField(auto_now_add=True)
