from django.urls import path
from . import views

urlpatterns = [
    path('<slug:subreddit>', views.subreddit_info)
]