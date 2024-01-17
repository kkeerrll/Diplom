from django.db import models

class Phone(models.Model):
    number = models.CharField(max_length=20)