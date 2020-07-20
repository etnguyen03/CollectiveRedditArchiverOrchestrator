import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Subreddit(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    create_date = models.DateField()
    total_tasks = models.IntegerField(default=0)
    completed_tasks = models.IntegerField(default=0)


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     create_time = models.DateTimeField(auto_now_add=True)
#
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


class Worker(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.ManyToManyField(User)
    ip = models.GenericIPAddressField()
    create_time = models.DateTimeField(auto_now_add=True)


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subreddit = models.ManyToManyField(Subreddit)
    date = models.DateField()
    complete = models.BooleanField()
    claimed = models.BooleanField()
    claim_worker = models.ManyToManyField(Worker)
    sha256_hash = models.CharField(default="", max_length=100, help_text="The sha256 hash of the completed .tar.gz file.")
    last_modify = models.DateTimeField(auto_now=True)
