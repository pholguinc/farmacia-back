import uuid
from django.utils import timezone

from django.db import models

class LaboratoryModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False)
    email = models.TextField(blank=False)
    ruc = models.TextField(max_length=11,blank=False)
    phone = models.CharField(max_length=11, blank=False)
    address = models.CharField(max_length=500, blank=False)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'laboratories'
        verbose_name = 'Laboratory'
        verbose_name_plural = 'Laboratories'
        ordering = ['id']

    def __str__(self):
        return self.name