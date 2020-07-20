import uuid

from django.db import models


# Create your models here.
class Subreddit(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    create_date = models.DateField()
    total_tasks = models.IntegerField(default=0)
    completed_tasks = models.IntegerField(default=0)


class Worker(models.Model):
    ip = models.CharField(max_length=30, primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True)


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subreddit = models.ManyToManyField(Subreddit)
    date = models.DateField()
    complete = models.BooleanField()
    claimed = models.BooleanField()
    claim_worker = models.ManyToManyField(Worker)
    last_modify = models.DateTimeField(auto_now=True)

