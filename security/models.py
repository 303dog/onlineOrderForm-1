from django.db import models


class LinkHash(models.Model):
    class Meta:
        db_table = 'hash'
    hash = models.TextField(max_length=255)
