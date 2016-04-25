from django.db import models

class List(models.Model):
    pass


class Item(models.Model):
    text = models.TextField(default='', blank=False, null=False)
    list = models.ForeignKey(List, default=None, blank=True, null=True)