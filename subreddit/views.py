from django.core import serializers
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Subreddit


# Create your views here.
def subreddit_info(request, subreddit=""):
    if subreddit == "":
        raise Http404()
    sub = get_object_or_404(Subreddit, name=subreddit)
    context = {
        "name": sub.name,
        "total_tasks": sub.total_tasks,
        "completed_tasks": sub.completed_tasks,
        "percent_complete": (sub.total_tasks / sub.completed_tasks) * 100 if sub.completed_tasks != 0 else 0,
    }
    return render(request, "r/index.html", context=context)

def index(request):
    subreddit_list = Subreddit.objects.all()
    context = {
        "subreddit_list": subreddit_list
    }
    return render(request, "index.html", context=context)
