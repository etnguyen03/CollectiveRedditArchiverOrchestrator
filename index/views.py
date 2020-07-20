from subreddit.models import Subreddit
from django.shortcuts import render


def index(request):
    subreddit_list = Subreddit.objects.all()
    context = {
        "subreddit_list": subreddit_list
    }
    return render(request, "index.html", context=context)
