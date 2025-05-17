import uuid
from django.db import models

class LotModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    medication = models.ForeignKey(
        'MedicationsModel',
        on_delete=models.CASCADE,
        related_name='lots',
        null=False
    )

    provider = models.ForeignKey(
        'ProviderModel',
        on_delete=models.CASCADE,
        related_name='lots',
        null=False
    )



    class Meta:
        db_table = 'lots'
        verbose_name = 'Lot'
        verbose_name_plural = 'Lots'
        ordering = ['id']

    def __str__(self):
        return self.name