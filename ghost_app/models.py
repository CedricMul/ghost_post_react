from django.db import models

class GhostPost(models.Model):
    is_boast = models.BooleanField(default=True)
    content = models.CharField(max_length=240)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    total_votes = models.IntegerField(default=0)
    datetime = models.DateTimeField(auto_now_add=True)
