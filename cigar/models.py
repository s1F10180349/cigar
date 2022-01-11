from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)
    like = models.IntegerField(default=0)

    def publish(self):
        self.publish_at = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title