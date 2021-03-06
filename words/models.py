from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Words(models.Model):
    noun = models.CharField(max_length=100)
    define = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    player = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.noun

    def get_absolute_url(self):
        return reverse('words-detail', kwargs={'pk':self.pk})
