from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    title = models.CharField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name="comments")
    comment_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"by {self.author}: {self.content} "


class Reply(models.Model):
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="replies")
    reply_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"by {self.author}: {self.content} "
