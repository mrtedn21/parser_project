from django.db import models


class Bill(models.Model):
    client_name = models.CharField(max_length=256, blank=False)
    client_org = models.CharField(max_length=256, blank=False)
    number = models.IntegerField()
    sum = models.IntegerField()
    date = models.DateField()
    service = models.CharField(max_length=512, blank=False)
