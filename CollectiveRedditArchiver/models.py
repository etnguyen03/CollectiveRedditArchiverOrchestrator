from django.db import models


# Create your models here.
class Subreddit(models.Model):
    name = models.CharField(max_length=20)
    create_date = models.DateField()


class Worker(models.Model):
    ip = models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now_add=True)


class Task(models.Model):
    subreddit = models.ForeignKey(Subreddit, on_delete=models.PROTECT)
    date = models.DateField()
    complete = models.BooleanField()
    claimed = models.BooleanField()
    claim_worker = models.ForeignKey(Worker, on_delete=models.PROTECT)
    last_modify = models.DateTimeField(auto_now=True)

