import uuid
from decimal import Decimal

from django.db import models

class MedicationsModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=255)
    description_simple = models.TextField(blank=True)
    description_all = models.TextField(blank=True)
    generical_name = models.CharField(max_length=255, blank=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    utility = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)


    class Meta:
        db_table = 'medications'
        verbose_name = 'Medication'
        verbose_name_plural = 'Medications'
        ordering = ['id']

    def __str__(self):
        return self.name


