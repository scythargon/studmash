from django.db import models


class Girl(models.Model):
    name = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    score = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='girls')