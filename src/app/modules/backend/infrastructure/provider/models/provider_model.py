import uuid
from django.db import models

class ProviderModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False)
    email = models.TextField(blank=False)
    ruc = models.TextField(max_length=11,blank=False)
    phone = models.CharField(max_length=11, blank=False)
    address = models.CharField(max_length=500, blank=False)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'providers'
        verbose_name = 'Provider'
        verbose_name_plural = 'Providers'
        ordering = ['id']

    def __str__(self):
        return self.name