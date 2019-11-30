from django.db import models


# Create your models here.
from rest_framework import reverse


class Interviewer(models.Model):
    name = models.CharField(max_length=20)
    room = models.CharField(max_length=6)

    def __str__(self):
        return str(self.id) + " " + self.name + ' ' + self.room

    # def get_absolute_url(self):
    #     return reverse