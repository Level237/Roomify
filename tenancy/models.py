from django.db import models

# Create your models here.


class TenantBaseModal(models.Model):
    hotel=models.ForeignKey(
        'hotels.Hotel',
        on_delete=models.CASCADE,
        related_name="%(class)s_tenant"
    )
    
    class Meta:
        abstract = True
