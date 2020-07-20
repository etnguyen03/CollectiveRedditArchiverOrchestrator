from .models import Subreddit, Task
from rest_framework import serializers

class SubredditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subreddit
        fields = ['name', 'create_date']