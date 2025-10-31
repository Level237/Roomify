
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from roles.models import Role

User = get_user_model()

@receiver(post_save, sender=User)
def assign_admin_role(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        role, _ = Role.objects.get_or_create(name="admin")
        instance.role = role
        instance.save()
