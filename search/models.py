from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone


# Create your models here.


class inspect(models.Model):
    author_name = models.CharField(max_length=100, default="", blank=True)
    author_email = models.CharField(max_length=100, default="", blank=True)
    author_url = models.CharField(max_length=200, default="", blank=True)
    # Field name made lowercase.
    author_ip = models.CharField(max_length=100, default="", blank=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    date_gmt = models.DateTimeField(default=timezone.now, blank=True)
    history = models.TextField( default="", blank=True)
    searchitems = models.TextField(default="", blank=True)
    approved = models.BooleanField(max_length=20, default=False)
    searchpages = models.TextField(default="", blank=True)
    webrelatedsearch = models.TextField(default="", blank=True)
    type = models.CharField(max_length=20, default="", blank=True)
    morepic = models.TextField(default="", blank=True)
    morevid   = models.TextField(default="", blank=True)

    def __str__(self):
        return str(self.pk) + "----->" + self.author_name


