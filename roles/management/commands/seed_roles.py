from django.core.management.base import BaseCommand
from roles.models import Role

class Command(BaseCommand):
    help = "Seed initial roles into the database"
    
    def handle(self,*args, **kwargs):
        roles=[
            {"name": "admin"},
            {"name": "user"},
            {"name":  "manager"},
            {"name":"hotelier"}
        ]
        
        for role in roles:
            role , created = Role.objects.get_or_create(name=role["name"])
            if created:
                self.stdout.write(self.style.SUCCESS(f"Role '{role.name}' created"))
            else:
                self.stdout.write(self.style.WARNING(f" Role '{role.name}' already exist "))