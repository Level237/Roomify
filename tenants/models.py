from django.db import models
from django_tenants.models import TenantMixin,DomainMixin


class HotelTenant(TenantMixin):
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    auto_create_schema = True

    def __str__(self):
        return self.name
    
class Domain(DomainMixin):
    domain = models.CharField(max_length=253, unique=True, db_index=True)
    tenant = models.ForeignKey(HotelTenant, on_delete=models.CASCADE, related_name='domains')

    is_primary = models.BooleanField(default=True, db_index=True)

    def __str__(self):
        return f"{self.domain} ({self.tenant.name})"